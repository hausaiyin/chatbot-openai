![image](https://github.com/user-attachments/assets/4edb01f9-acfe-46fd-aac4-8a79fb527563)

# 🤖 Chatbot With OpenAI (Multi-Model Support + LangSmith Tracking)

This is a smart chatbot built with **Streamlit**, **LangChain**, and **OpenAI**.  
You can choose from **multiple GPT models** and **track your conversations with LangSmith** for better debugging and analysis.

---

## ✅ Features

- 🔐 **Secure API key input** via sidebar (no need to hardcode)
- 🔄 **Model selection** between `gpt-4`, `gpt-4-turbo`, and `gpt-4o`
- 🎛️ **Customize output** using temperature and max token sliders
- 🧠 Uses **LangChain** prompt templates and output parsing
- 📊 **Tracks all runs via LangSmith (LangChain’s tracing tool)**  
- ⚡ Interactive, clean UI built with **Streamlit**
- 🛠️ Handles errors gracefully

---

## 📦 Installation

### 1. Clone the Repository

```bash
cd chatbot-with-openai
2. Install Dependencies
Make sure Python 3.8+ is installed.

bash
Copy code
pip install -r requirements.txt
3. Create .env File for LangSmith
Create a .env file in the root with your LangSmith API key:

ini
Copy code
LANGCHAIN_API_KEY=your_langsmith_api_key_here
🔐 Your OpenAI API key can be entered during runtime in the sidebar.

🚀 How to Run
bash
Copy code
streamlit run main.py

🧪 LangSmith Tracking (Optional but Powerful)
This app supports LangSmith run tracking for each conversation.
Make sure your .env contains:

env
Copy code
LANGCHAIN_API_KEY=your_langsmith_api_key_here
And you'll see all interactions in your LangSmith dashboard.


📁 Project Structure
bash
Copy code
├── main.py               # Streamlit chatbot script
├── requirements.txt     # Required packages
├── .env                 # API key for LangSmith (LangChain tracking)
🙌 Contribution
Found a bug or have a feature request?
Open an issue or submit a PR — all contributions are welcome!

🛡️ Disclaimer
This app is for demo/educational use. Always keep your API keys secure and follow usage guidelines.

⚙️ Built With
OpenAI

LangChain

LangSmith

Streamlit
