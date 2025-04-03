import streamlit as st
from chatbot import chat_with_ai, generate_scenario
from database import get_mistakes, store_mistake, clear_mistakes
import config

#  Page Config
st.set_page_config(page_title="🌍 AI Language Tutor", page_icon="📚", layout="wide")

# Sidebar for Language Selection
st.sidebar.header("🗣️ Language Settings")
native_language = st.sidebar.selectbox("Your native language:", list(config.SUPPORTED_LANGUAGES.keys()))
learning_language = st.sidebar.selectbox("Language you want to learn:", list(config.SUPPORTED_LANGUAGES.keys()))

# Ensure different languages are selected
if native_language == learning_language:
    st.sidebar.warning("Native and learning languages should be different.")
    st.stop()

proficiency = st.sidebar.radio("Your proficiency level:", ["Beginner", "Intermediate", "Advanced"])

#  Tab Layout
tab1, tab2 = st.tabs(["💬 Chat", "📖 Mistake History"])

#  TAB 1: Chatbot Interface
with tab1:
    st.title("🌍 AI-Powered Language Learning Chatbot")

    #  Generate Scenario
    scenario = generate_scenario(native_language, learning_language, proficiency)
    st.subheader("📝 Scenario:")
    st.write(scenario)

    #  User Input
    user_input = st.text_input("Type your response in the learning language:")

    if st.button("Submit"):
        if user_input:
            ai_response = chat_with_ai(user_input, native_language, learning_language, proficiency)

            # Show AI response
            st.write("🤖 **AI:**", ai_response.get("response", "I don't know how to respond."))

            #  Mistake Handling
            if ai_response["flag"]:
                st.error("❌ Mistake detected!")
                st.write(f"🔹 **Your input:** {ai_response['original']}")
                st.write(f"✅ **Corrected:** {ai_response['corrected']}")
                st.write(f"📌 **Explanation:** {ai_response['explanation']}")

                # ✅ Store mistake in database
                store_mistake(ai_response["original"], ai_response["corrected"], ai_response["explanation"])
            else:
                st.success("✅ No mistakes detected!")

#  TAB 2: Mistake History
with tab2:
    st.title("📖 Mistake Tracker")

    # Retrieve Mistakes
    mistakes = get_mistakes()

    if mistakes:
        st.subheader("Your Mistakes:")
        for i, (user_input, correct_response, explanation) in enumerate(mistakes, start=1):
            with st.expander(f"🔹 Mistake {i}"):
                st.write(f"❌ **Your Input:** {user_input}")
                st.write(f"✅ **Corrected:** {correct_response}")
                st.write(f"📖 **Explanation:** {explanation}")

                #  Retry Mistake
                if st.button(f"🔄 Retry '{user_input}'", key=f"retry_{i}"):
                    st.session_state["retry_input"] = user_input
                    st.experimental_rerun()

    else:
        st.info("🎉 No mistakes found! Keep practicing.")

    #  Clear Mistakes Button
    if st.button("🗑️ Clear Mistakes"):
        clear_mistakes()
        st.success("Mistakes cleared successfully!")
        st.experimental_rerun()
