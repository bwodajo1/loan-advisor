from flask import Flask, request, jsonify, render_template
import anthropic
from calculator import loan_summary, amortization_schedule

app = Flask(__name__)
client = anthropic.Anthropic()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    try:
        principal = float(data["principal"])
        annual_rate = float(data["annual_rate"])
        years = int(data["years"])
    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Invalid input: {e}"}), 400
    summary = loan_summary(principal, annual_rate, years)
    schedule = amortization_schedule(principal, annual_rate, years)
    return jsonify({"summary": summary, "schedule": schedule})


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    loan_data = data.get("loan_data", {})
    if not loan_data:
        return jsonify({"error": "No loan data provided"}), 400
    system_prompt = f"""You are a helpful, honest financial assistant specializing in loans and mortgages.
The user has a loan with these details:
- Principal: ${loan_data['principal']:,.2f}
- Annual interest rate: {loan_data['annual_rate']}%
- Term: {loan_data['years']} years
- Monthly payment: ${loan_data['monthly_payment']:,.2f}
- Total amount paid: ${loan_data['total_paid']:,.2f}
- Total interest paid: ${loan_data['total_interest']:,.2f}

Answer questions clearly and specifically using their actual numbers.
Be honest about costs — don't sugarcoat how much interest they're paying.
Keep answers concise (2-4 sentences unless a detailed breakdown is needed).
Do not give personalised financial advice — always suggest consulting a financial advisor for major decisions."""
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return jsonify({"response": message.content[0].text})


if __name__ == "__main__":
    app.run(debug=True)