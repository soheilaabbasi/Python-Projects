# 🦙 Ollama Chatbot with Streamlit & Ollama

A simple and interactive AI chatbot built with **Python**, **Streamlit**, and **Ollama**.
The chatbot uses a locally running Large Language Model (LLM) to generate responses without requiring an external AI API.

---

## ✨ Features

* Interactive chat interface
* Powered by an LLM running locally with Ollama
* Built with Streamlit
* Runs locally without sending prompts to an external AI service
* Easy to change the AI model
* Maintains chat messages during the Streamlit session
* Simple Python project structure

---

## 🛠️ Technologies

* **Python 3**
* **Streamlit**
* **Ollama**
* **Qwen3:1.7b**
* **Requests**

---

## 📁 Project Structure

```text
12-ChatBot/
│
├── src/
│   ├── app.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

The application uses **Streamlit** to create the chat interface and **Ollama** to run the language model locally.

The communication flow is:

```text
User
  ↓
Streamlit Chat UI
  ↓
Python Application
  ↓
Ollama API
  ↓
Qwen3 Model
  ↓
Generated Response
  ↓
Streamlit
```

Ollama runs locally and exposes its API at:

```text
http://localhost:11434
```

The application sends the user's prompt to Ollama and displays the generated response in the chat interface.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd 12-Chat
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## 📥 Install Python Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

Download and install Ollama from its official website:

https://ollama.com/

After installation, make sure Ollama is available from your terminal:

```bash
ollama --version
```

---

## 🤖 Download the AI Model

This project can use a Qwen3 model running through Ollama.

For a lightweight model:

```bash
ollama pull qwen3:1.7b
```

For a larger model:

```bash
ollama pull qwen3:4b
```

You can check the models installed on your system with:

```bash
ollama list
```

---

## ▶️ Run the Chatbot

First, make sure Ollama is running.

You can test the model directly:

```bash
ollama run qwen3:1.7b
```

Then start the Streamlit application:

```bash
streamlit run src/app.py
```

Streamlit will provide a local address, usually:

```text
http://localhost:8501
```

Open that address in your browser.

---

## 🔧 Changing the Model

The model name is specified in `app.py`.

For example:

```python
msg = call_llama('qwen3:1.7b', prompt)['response']
```

You can change it to another model installed in Ollama:

```python
msg = call_llama('qwen3:4b', prompt)['response']
```

Make sure the model has already been downloaded:

```bash
ollama pull qwen3:4b
```

---

## 📄 `utils.py`

The `utils.py` file is responsible for communicating with the `Ollama API`.

The application sends a request to:

```text
http://localhost:11434/api/generate
```

A simplified example of the request is:

```python
data = {
    "model": model,
    "prompt": prompt,
    "stream": False
}
```

The generated response is then returned to the Streamlit application.

---

## 📄 `app.py`

The `app.py` file creates the `Streamlit user interface`.

It:

1. Creates the chatbot interface.
2. Stores messages in `st.session_state`.
3. Displays previous messages.
4. Accepts new user prompts.
5. Sends prompts to Ollama.
6. Displays the generated response.

---

## 🧪 Check Installed Ollama Models

To see all installed models:

```bash
ollama list
```

Example:

```text
NAME                ID              SIZE
qwen3:1.7b          ...             ...
qwen3:4b            ...             ...
```

To remove a model you no longer need:

```bash
ollama rm qwen3:4b
```

For example, if you only want to keep the smaller model, you can remove the larger one to free disk space.

---

## ⚡ Performance

The chatbot's response speed depends mainly on:

* The size of the selected model
* CPU performance
* Available RAM
* Whether a GPU is available
* The length of the prompt
* The amount of context sent to the model

Smaller models such as:

```text
qwen3:1.7b
```

generally require fewer resources than:

```text
qwen3:4b
```

If responses are slow, using a smaller model can help.

---


## 🚀 Future Improvements

Possible improvements for this project include:

* [ ] Add streaming responses
* [ ] Improve error handling
* [ ] Add a model selector to the Streamlit sidebar
* [ ] Add a "Clear Chat" button
* [ ] Send the full conversation history to the model
* [ ] Add system prompts
* [ ] Add chat history persistence
* [ ] Add support for multiple Ollama models
* [ ] Improve the UI
* [ ] Add typing/loading indicators

---

## 📚 Learning Goals

This project is useful for learning:

* Python
* Streamlit
* REST APIs
* JSON
* HTTP requests
* Local LLMs
* Ollama
* Chatbot development
* Session state management
