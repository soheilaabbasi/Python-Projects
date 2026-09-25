![alt text](images/banner.png)
# 💱 Currency Converter

A simple and user-friendly **Currency Converter** built with Python and Streamlit.

This application allows users to convert an amount from one currency to another using exchange rates provided by the **ExchangeRate-API**. The application has a web-based interface built with Streamlit and also supports running the converter directly from the command line.

---

## ✨ Features

* 💱 Convert between a large number of currencies
* 🌐 Get exchange rates from the ExchangeRate-API
* ⚡ Automatically update the conversion when the amount or currency changes
* 🔄 Swap base and target currencies with one click
* 🔃 Refresh exchange rates manually
* 💾 Cache exchange rates for 3 hours to reduce unnecessary API requests
* 💰 Display currency symbols and names
* 📊 Show the current exchange rate
* 🖥️ Simple and responsive Streamlit interface
* 💻 Can also be used from the command line

---

## 🖼️ Application

The application provides a simple interface where you can:

1. Select the currency you want to convert **from**
2. Select the currency you want to convert **to**
3. Enter the amount
4. View the current exchange rate
5. See the converted amount

The application also includes buttons for:

* 🔄 Swapping the selected currencies
* 🔃 Refreshing the exchange rate

---

## 📁 Project Structure

```text
Currency-Converter/
   ├── images/
   │     └── banner.png
   ├── src/
   │     ├── app.py
   │     ├── Currency_Convertor.py
   │     └── constants.py
   │
   ├── README.md
   └── requirements.txt  
```

### `app.py`

The main application file.

It uses **Streamlit** to create the web interface and handles:

* Currency selection
* Amount input
* Currency swapping
* Exchange-rate refreshing
* Displaying conversion results
* Displaying currency names and symbols

---

### `Currency_Convertor.py`

This file contains the main currency conversion logic.

It is responsible for:

* Getting exchange rates from the API
* Converting amounts
* Caching exchange rates
* Clearing the cache
* Providing a command-line version of the converter

Main functions:

```python
get_exchange_rate(base_currency, target_currency)
```

Gets the exchange rate between two currencies.

```python
convert_currency(amount, exchange_rate)
```

Converts an amount using the provided exchange rate.

```python
clear_cache()
```

Clears all cached exchange rates.

---

### `constants.py`

This file contains the application's currency data.

It includes:

```python
CURRENCIES
```

A list of supported currency codes.

For example:

```text
USD
EUR
GBP
JPY
CAD
AUD
INR
TRY
...
```

It also contains:

```python
CURRENCY_INFO
```

which provides the name and symbol for commonly used currencies.

Example:

```python
"USD": {
    "name": "US Dollar",
    "symbol": "$"
}
```

---

## 🛠️ Technologies Used

This project is built using:

* **Python**
* **Streamlit**
* **Requests**
* **Cachetools**
* **ExchangeRate-API**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/currency-converter.git
```

Then move into the project directory:

```bash
cd currency-converter
```

---

### 2. Create a virtual environment

It is recommended to use a virtual environment.

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

Install the required Python packages:

```bash
pip install streamlit requests cachetools
```

---

## 🚀 Running the Application

To start the Streamlit application, run:

```bash
streamlit run src/app.py
```

After running the command, Streamlit will provide a local URL, usually similar to:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

---

## 💻 Command-Line Usage

The `Currency_Convertor.py` file can also be executed directly without Streamlit.

Run:

```bash
python Currency_Convertor.py
```

The program will ask you for:

```text
Enter base currency:
Enter target currency:
Enter amount:
```

For example:

```text
Enter base currency: USD
Enter target currency: EUR
Enter amount: 100
```

The program will then display the converted amount and the time when the exchange rate was retrieved.

Example output:

```text
100 USD is 92.50 EUR
Last updated: 2026-09-25 19:30:00
```

> The exact exchange rate and converted amount depend on the current rate provided by the API.

---

## 🌐 Exchange Rate API

This project uses the following API endpoint:

```text
https://api.exchangerate-api.com/v4/latest/{base_currency}
```

For example, if the base currency is USD:

```text
https://api.exchangerate-api.com/v4/latest/USD
```

The API returns exchange rates for different currencies based on the selected base currency.

The application then retrieves the required target currency rate from the API response.

---

## ⚡ Caching

To reduce unnecessary API requests, the project uses `TTLCache` from the `cachetools` package.

The cache is configured as:

```python
cache = TTLCache(maxsize=100, ttl=3*60*60)
```

This means:

* Maximum **100** cached items can be stored.
* Each cached exchange rate remains available for **3 hours**.
* After 3 hours, the cached value expires and a new API request can be made.

This helps reduce repeated requests when the same currency pair is requested multiple times.

---

## 🔄 Refreshing Exchange Rates

The Streamlit application provides a **Refresh Rate** button.

When the button is clicked, the cache is cleared:

```python
clear_cache()
```

After clearing the cache, the next conversion request retrieves a fresh exchange rate from the API.

---

## 🔄 Swapping Currencies

The application includes a **Swap Currencies** button.

For example, if the selected currencies are:

```text
USD → EUR
```

clicking the swap button changes them to:

```text
EUR → USD
```

This is handled using Streamlit's session state.

---

## 💰 Supported Currencies

The project contains a large list of supported currency codes in `constants.py`.

Some examples include:

| Code | Currency           |
| ---- | ------------------ |
| USD  | US Dollar          |
| EUR  | Euro               |
| GBP  | British Pound      |
| JPY  | Japanese Yen       |
| CNY  | Chinese Yuan       |
| CAD  | Canadian Dollar    |
| AUD  | Australian Dollar  |
| CHF  | Swiss Franc        |
| INR  | Indian Rupee       |
| TRY  | Turkish Lira       |
| AED  | UAE Dirham         |
| SAR  | Saudi Riyal        |
| KRW  | South Korean Won   |
| BRL  | Brazilian Real     |
| RUB  | Russian Ruble      |
| ZAR  | South African Rand |

The complete list of supported currency codes is available in `constants.py`.

---

## 🧩 How the Application Works

The general flow of the application is:

```text
User
  │
  ▼
Streamlit Interface
  │
  ├── Select Base Currency
  │
  ├── Select Target Currency
  │
  └── Enter Amount
  │
  ▼
get_exchange_rate()
  │
  ▼
Cache
  │
  ├── Cached rate available
  │       │
  │       └── Use cached rate
  │
  └── No cached rate
          │
          ▼
      ExchangeRate-API
          │
          ▼
      Exchange Rate
          │
          ▼
convert_currency()
          │
          ▼
Converted Amount
```

---

## 🧮 Conversion Formula

The conversion is performed using a simple multiplication:

```text
Converted Amount = Amount × Exchange Rate
```

For example, if:

```text
Amount = 100
Exchange Rate = 0.92
```

then:

```text
100 × 0.92 = 92
```

So:

```text
100 USD → 92 EUR
```

The actual exchange rate changes over time.

---

## 📋 Requirements

The project requires Python and the following packages:

```text
streamlit
requests
cachetools
```

You can install them using:

```bash
pip install streamlit requests cachetools
```

---

## ⚠️ Error Handling

If the API request does not return a successful response, the application displays an error message:

```text
❌ Error fetching exchange rate.
```

This prevents the application from attempting to perform a conversion when a valid exchange rate could not be retrieved.

---

## 📝 Notes

* Exchange rates are obtained from an external API.
* Internet access is required when a fresh exchange rate needs to be retrieved.
* Cached rates can be used without making another API request until the cache expires.
* The exchange rate is based on the data returned by the API at the time of the request.
* Currency names and symbols displayed in the application are defined in `CURRENCY_INFO`.
* Currencies that are not included in `CURRENCY_INFO` can still appear in the currency list; their code is used as the fallback display name.

---

## 🔮 Possible Future Improvements

Some possible improvements for future versions include:

* 📈 Add historical exchange-rate charts
* 📅 Allow users to select a specific date
* ⭐ Add favorite currencies
* 🌙 Add dark/light theme customization
* 📱 Improve the mobile layout
* 🔐 Add more robust API error handling
* ⏳ Display a loading indicator while fetching exchange rates
* 🧪 Add automated unit tests
* 📊 Add a conversion history
* 🌍 Add more detailed currency information
* 📦 Add a `requirements.txt` file for easier installation

---

## 👨‍💻 Author

Created as a Python project for learning and practicing:

* Python
* API requests
* Streamlit
* Caching
* Functions and modules
* Session state
* Web application development

---

## 📄 License

This project can be used for educational and personal purposes.

If you plan to publish the project publicly, you can add a specific open-source license such as MIT License.

---

## ⭐ Final

If you find this project useful, feel free to ⭐ star the repository and use it as a starting point for building more advanced currency and financial applications.
