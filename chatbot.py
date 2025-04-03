from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json
import re
import config
from database import store_mistake  # ✅ Import database function

# Initialize AI Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=config.GOOGLE_API_KEY)

# ✅ Scenario Prompt Template
scenario_prompt = PromptTemplate(
    input_variables=["native_language", "learning_language", "proficiency"],
    template="""
    You are a language tutor creating a real-world scenario for a {learning_language} learner.
    The user speaks {native_language} and is at a {proficiency} level.

    - Generate a practical conversation scenario (e.g., ordering food, asking for directions).
    - Keep it natural and aligned with the user’s proficiency level.
    - Avoid explanations—just provide the scenario.

    Example Output:
    "You are in a café in Spain. You want to order a coffee in Spanish."
    """
)

# ✅ Chat Prompt Template (For Conversation & Mistakes)
chat_prompt = PromptTemplate(
    input_variables=["history", "native_language", "learning_language", "proficiency", "user_input"],
    template="""
    You are an AI language tutor. The user speaks {native_language} and is learning {learning_language} at a {proficiency} level.

    - Engage in a conversation in {learning_language}.
    - Detect grammatical mistakes and provide corrections.
    - Explain errors clearly.
    - Keep responses friendly and encouraging.

    Respond in JSON format:
    {{
        "flag": true/false,   
        "original": "{user_input}",
        "corrected": "<corrected sentence if mistake found, otherwise empty>",
        "explanation": "<brief explanation of mistake, otherwise empty>",
        "response": "<AI's conversational response>"
    }}

    Conversation History: {history}
    User: {user_input}
    AI:
    """
)

# Create AI Chatbot Chains
chatbot_chain = LLMChain(llm=llm, prompt=chat_prompt)
scenario_chain = LLMChain(llm=llm, prompt=scenario_prompt)

# ✅ Function to generate scenario
def generate_scenario(native_language, learning_language, proficiency):
    response = scenario_chain.invoke({
        "native_language": native_language,
        "learning_language": learning_language,
        "proficiency": proficiency
    })
    
    if isinstance(response, dict):
        return response.get("text", "Scenario could not be generated.")

    return response

# ✅ Function to chat with AI
def chat_with_ai(user_input, native_language, learning_language, proficiency, history=""):
    response = chatbot_chain.invoke({
        "history": history,
        "native_language": native_language,
        "learning_language": learning_language,
        "proficiency": proficiency,
        "user_input": user_input
    })

    if isinstance(response, dict):
        ai_text = response.get("text", "")

        try:
            # ✅ Clean response (remove markdown-style JSON markers)
            ai_text = re.sub(r"```json\n|```", "", ai_text).strip()
            
            # ✅ Parse JSON safely
            parsed_response = json.loads(ai_text)
            
            # ✅ Ensure required fields exist
            result = {
                "flag": parsed_response.get("flag", False),
                "original": parsed_response.get("original", user_input),
                "corrected": parsed_response.get("corrected", ""),
                "explanation": parsed_response.get("explanation", ""),
                "response": parsed_response.get("response", "AI response not available.")
            }

            # ✅ Store mistakes in database
            if result["flag"]:  # If mistake detected
                store_mistake(result["original"], result["corrected"], result["explanation"])
                print("✅ Mistake stored in database!")

            return result
            
        except json.JSONDecodeError:
            print("❌ JSON Parsing Error! Raw AI response:", ai_text)

    return {
        "flag": False,
        "original": user_input,
        "corrected": "",
        "explanation": "",
        "response": "AI response could not be processed."
    }
