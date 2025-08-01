# 💬 Echolingo Bot - Multilingual AI Assistant

Echolingo is a smart, multilingual AI assistant with a modern web interface. It can understand questions in text or voice and provide answers in a wide variety of languages, which it can also speak aloud.

## ✨ Key Features

* **Multilingual Responses:** Ask a question and get an answer in one of many supported languages, including English, Spanish, French, Hindi, Chinese, and more.
* **Voice-to-Text Input:** Use your microphone to ask questions directly without typing.
* **Text-to-Speech Output:** Listen to the generated answers spoken aloud in the selected language.
* **Secure Backend:** Built with a Python Flask backend to protect the API key, ensuring it is never exposed in the browser.
* **Modern Interface:** A clean, responsive user interface styled with Tailwind CSS.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, JavaScript, Tailwind CSS
* **AI Model:** Google Generative AI (Gemini)
* **Browser APIs:** Web Speech API (Speech Recognition & Speech Synthesis)

## ⚙️ Setup and Installation

To run this project on your local machine, follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/echolingo-ai-assistant.git](https://github.com/YourUsername/echolingo-ai-assistant.git)
    cd echolingo-ai-assistant
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create your environment file for the API key:**
    * Find the `.env.example` file (if you have one) or create a new file named `.env`.
    * Open the `.env` file and add your Google AI API Key like this:
        ```
        API_KEY="YOUR_SECRET_API_KEY_HERE"
        ```

## 🚀 How to Run

1.  Execute the main Flask application in your terminal:
    ```bash
    python app.py
    ```
2.  The terminal will show that a server is running. Open your web browser and go to the following address:
    **`http://127.0.0.1:5000`**

You can now interact with the Echolingo Bot! To stop the server, go back to your terminal and press `Ctrl+C`.
