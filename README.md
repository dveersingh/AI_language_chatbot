# 🌍 AI-Powered Language Learning Chatbot

## 📌 Overview
This is an **AI-powered language learning chatbot** that helps users practice a new language by engaging in real-world conversational scenarios. The chatbot provides grammatical corrections, explanations, and interactive feedback to improve language skills.

## 🏗️ System Architecture
```
+-----------------+
|  Streamlit UI  |
+-----------------+
        |
        v
+-------------------+
|  Chatbot Logic   |
+-------------------+
        |
        v
+-------------------+
|  LangChain (LLM) |
+-------------------+
        |
        v
+-------------------+
|  Gemini AI Model |
+-------------------+
        |
        v
+----------------+
|  SQLite (DB)  |
+----------------+
```

## 📋 Features
✅ **Interactive Language Chatbot** - AI-powered chat that corrects grammar mistakes.
✅ **Scenario-Based Learning** - Generates real-world conversational scenarios.
✅ **Mistake Tracking** - Stores and displays previous mistakes for learning.
✅ **Multi-Language Support** - Supports at least 10 languages.
✅ **User-Friendly UI** - Built with Streamlit for an intuitive experience.

## ⚙️ Requirements
- Python 3.10+
- Streamlit
- LangChain
- Google Gemini API key
- SQLite (for mistake tracking)

## 📥 Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/dveersingh/AI_language_chatbot.git
   cd AI_language_chatbot
   ```

2. **Create a Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the **Google API Key** in Streamlit:
   - **For Local Setup**:
     1. Create a `.streamlit/secrets.toml` file in your project root.
     2. Add the following content:
        ```toml
        [general]
        GOOGLE_API_KEY = "your_actual_api_key"
        ```
     3. Alternatively, you can set it via environment variables:
        ```sh
        export GOOGLE_API_KEY=your_actual_api_key
        ```
        Or on Windows (PowerShell):
        ```powershell
        $env:GOOGLE_API_KEY="your_actual_api_key"
        ```
   - **For Streamlit Community Cloud**:
     1. Go to **App Settings** → **Advanced Settings**.
     2. Under **Secrets**, add:
        ```
        GOOGLE_API_KEY = your_actual_api_key
        ```
     3. Click **Save**.


5. **Initialize Database**
   ```bash
   python database.py
   ```

## 🚀 How to Run
```bash
streamlit run app.py
```
Then, open the browser at `http://localhost:8501/`.

## 🛠️ How It Works
1. **User selects native & learning languages**.
2. **AI generates a real-world scenario**.
3. **User interacts with the chatbot**.
4. **AI detects and corrects mistakes**.
5. **Mistakes are stored in a database**.
6. **Users can review past mistakes for learning**.

## 📌 Future Improvements
- Support for voice input/output.
- Enhanced personalization based on progress.
- More advanced mistake analytics.

## 🤝 Contributing
Feel free to fork, modify, and submit pull requests! 🚀

## 📜 License
MIT License. See `LICENSE` file for details.

## 🔗 Contact
For any issues or suggestions, reach out via [GitHub Issues](https://github.com/dveersingh/AI_language_chatbot/issues).

