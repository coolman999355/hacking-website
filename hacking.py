from flask import Flask, request, render_template_string
import smtplib
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Pay</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
        }

        .card {
            background: #1e293b;
            padding: 25px;
            border-radius: 12px;
            width: 340px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 6px 0;
            border: none;
            border-radius: 5px;
        }

        button {
            width: 100%;
            padding: 10px;
            background: #22c55e;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }

        .tag {
            font-size: 12px;
            color: #94a3b8;
        }
    </style>
</head>
<body>

<div class="card">
    <h2>🔒 Secure Payment</h2>
    <p class="tag">Encrypted Demo System</p>

    <form method="POST">
        <input name="card_number" placeholder="Credit Card Number">
        <input name="cvv" placeholder="CVV">
        <input name="expiry" placeholder="Expiry Date (MM/YY)">
        <input name="card_holder" placeholder="Card Holder Name">
        <button type="submit">Pay Now</button>
    </form>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        card_number = request.form.get("card_number")
        cvv = request.form.get("cvv")
        expiry = request.form.get("expiry")
        card_holder = request.form.get("card_holder")

        print("=== Payment Submitted ===")
        print(f"Card Holder: {card_holder}")
        print(f"Card Number: {card_number}")
        print(f"Expiry: {expiry}")
        print(f"CVV: {cvv}")
        print("=========================")

        return f"""
        <html>
        <body style="font-family:Arial;text-align:center;margin-top:100px;">
            <h1>✅ Payment Processing...</h1>
            <p>Card Holder: {card_holder}</p>
            <p>Card Number: {card_number}</p>
            <p>Expiry: {expiry}</p>
            <p>CVV: {cvv}</p>
            <h2>💳 Approved (DEMO)</h2>
            <a href="/">Go back</a>
        </body>
        </html>
        """

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
