![alt text](images/connectivity-checker.png)
# 🌐 Website Availability Checker

A simple website availability checker built with Python and Streamlit.

This application allows users to add website URLs to a list and check whether each website is responding successfully.

## ✨ Features

-  Add website URLs to a list
-  Clear the entire URL list
-  Automatically format URLs with `https://www.`
-  Check website availability
-  Display unsuccessful requests
-  Store URLs and their statuses using Streamlit Session State
-  Simple and user-friendly web interface

## 📁 Project Structure

```
Site-Connectivity-Checker/
│
├── images/
│   └── connectivity-checker.png
│
├── src/
│   └── app.py
│
├── README.md
│
└── requirements.txt
```

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests

## 📦 Requirements

The project dependencies are listed in `requirements.txt`:

- requests==2.34.2
- streamlit==1.63.0

## 🚀 Installation

### 1. Clone the repository

`git clone <YOUR_REPOSITORY_URL>`

Then move into the project directory:

`cd 11-Site-Connectivity-Checker`

### 2. Create and activate a virtual environment

For example, using `Conda`:

`conda create -n site-checker python=3.14`

Activate the environment:

`conda activate site-checker`

### 3. Install the required packages

`pip install -r requirements.txt`

## ▶️ Run the Application

Since `app.py` is located inside the `src` directory, run the application with:

`streamlit run src/app.py`

After running the command, Streamlit will start the application and provide a local URL that can be opened in a browser.

## 🖥️ How to Use

### 1. Enter a Website URL

Enter a website URL in the input box.

For example:

`google.com`

### 2. Click "Add URL"

The application automatically formats the URL.

For example:

`google.com`

becomes:

`https://www.google.com`

### 3. Add More Websites

You can add multiple websites to the list.

### 4. Click "Check All"

The application sends a request to each website and checks its HTTP status code.

For example:

```
https://www.google.com     ✅
https://www.github.com     ✅
https://stackoverflow.com  ❌
```

A website that returns HTTP status code `200` is considered available by this application.

### 5. Click "Clear List"

The `Clear List` button removes all websites from the current list.

## 🔍 How It Works

The application uses the `requests` library to send HTTP GET requests to websites.
```
response = requests.get(
    url,
    timeout=5,
    headers=headers
)
```

The response status code is then checked. If the status code is `200`, the website is considered available. Otherwise, the result is displayed as unavailable.
```
if response.status_code == 200:
    return True
else:
    return False
```
The result is displayed in the Streamlit interface using:

```
✅ for available websites
❌ for unsuccessful requests
```

The application also uses a User-Agent header and a 5-second timeout for requests.

## 💾 Session State

The application uses Streamlit's `session_state` to keep track of URLs and their statuses.

The list of URLs is stored in:

`st.session_state.urls`

The status of each URL is stored using keys such as:
```
status_0
status_1
status_2
```

This allows the application to keep the URLs and their results while Streamlit reruns the script after user interactions.

## ⚠️ HTTP Status Codes

This project currently considers only HTTP status code `200` as a successful response.

Examples:
```
200 → ✅
403 → ❌
404 → ❌
500 → ❌
```

## 📌 Example

Suppose the following websites are added:
```
google.com
github.com
python.org
```

After clicking `Check All`, the application may display:

```
https://www.google.com     ✅
https://www.github.com     ✅
https://www.python.org     ✅
```


## 📚 What I Learned

This project demonstrates several Python and Streamlit concepts:

- Python functions
- String manipulation
- HTTP requests
- HTTP status codes
- Exception handling with `try` and `except`
- Streamlit UI components
- Streamlit `session_state`
- Lists
- Loops
- `enumerate()`
- Conditional expressions
- Basic web requests

## 👤 Author

Created as a Python and Streamlit practice project.