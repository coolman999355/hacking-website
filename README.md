# hacking-website
# 🔒 hacking demo

⚠️ **IMPORTANT WARNING**
This project is for **educational purposes only**.  
It is NOT a real payment system and must NOT be used to collect real credit card information.

Collecting or storing real payment data without proper security, encryption, and legal compliance is dangerous and illegal in many cases.

---

## 📌 About the Project

This is a simple Flask web app that simulates a “payment form” UI.

It demonstrates:
- Flask routing (`GET` and `POST`)
- HTML form handling
- Basic styling with CSS
- Displaying submitted form data

When the form is submitted, the data is printed in the console and displayed back on a results page.

---

## 🚀 Features

- Modern styled payment form UI
- Input fields for:
  - Card number
  - CVV
  - Expiry date
  - Card holder name
- Displays submitted data (demo only)
- Simple Flask backend

---

## 🧠 Tech Stack

- Python 🐍
- Flask 🌐
- HTML + CSS 🎨
- smtplib (imported but not used)

---

## 📂 Project Structure


project/
│
├── app.py
└── README.md


---

## ⚙️ Installation

### 1. Install dependencies
```bash
pip install flask
2. Run the app
python app.py
3. Open in browser
http://127.0.0.1:5000
🧪 How It Works
User opens the page
Fills in the form
Clicks Pay Now
Server receives data via POST request
Data is printed in terminal
Confirmation page is shown
🔐 Security Notice

This project:

❌ Does NOT encrypt data
❌ Does NOT process real payments
❌ Does NOT store data securely
❌ Should NOT be used with real credit cards

For real payment systems, use:

Stripe
PayPal API
PCI-DSS compliant services
📚 Learning Goals

This project helps you understand:

Flask basics
Form handling
Backend + frontend interaction
