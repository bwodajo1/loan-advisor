# LoanAdvisor 

An AI-powered loan calculator that breaks down your payments and lets you ask plain-English questions about your loan using Claude.

**Live Demo:** https://loan-advisor-3.onrender.com

---

## What It Does

Most loan calculators just give you a monthly payment number. LoanAdvisor goes further:

- Calculates your exact monthly payment using the standard amortization formula
- Generates a full month-by-month breakdown of principal vs. interest
- Visualizes your balance payoff over time with an interactive chart
- Lets you chat with an AI assistant that knows your specific loan details — ask things like *"how much interest do I pay in year 1?"* or *"what happens if I refinance at 5%?"*

---

## Screenshots


---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI | Anthropic Claude (claude-sonnet-4-6) |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Deployment | Render |

---

## How It Works

1. User enters loan amount, interest rate, and term
2. Flask backend calculates monthly payment using the amortization formula:

```
M = P × [r(1+r)^n] / [(1+r)^n - 1]
```

Where `P` = principal, `r` = monthly interest rate, `n` = number of payments

3. Full amortization schedule is returned and rendered as a table and chart
4. For AI chat, the user's loan summary is injected into Claude's system prompt as context, enabling specific answers about their actual numbers rather than generic advice

---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/bwodajo1/loan-advisor.git
cd loan-advisor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set your Anthropic API key**
```bash
export ANTHROPIC_API_KEY=your_key_here
```

Get a key at [console.anthropic.com](https://console.anthropic.com)

**4. Run the app**
```bash
python app.py
```

**5. Open in browser**
```
http://localhost:5000
```

---

## Project Structure

```
loan-advisor/
├── app.py              # Flask backend — routes and AI chat endpoint
├── calculator.py       # Core loan math — payment, amortization, summary
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
└── templates/
    └── index.html      # Frontend — form, chart, table, AI chat UI
```

---

## Key Implementation Details

**calculator.py** handles all the math as pure functions with no side effects — easy to test and reuse independently of Flask.

**AI context injection** — rather than a generic chatbot, the system prompt is dynamically built with the user's actual loan figures on every request, so Claude answers specifically about their loan rather than giving generic financial information.

**Amortization schedule** — generated month by month, tracking how each payment splits between principal and interest. Early payments are mostly interest; later payments are mostly principal — the chart makes this visually clear.

---

## What I'd Add Next

- [ ] Extra monthly payment calculator — show interest saved by paying more each month
- [ ] Loan comparison tool — compare two loans side by side
- [ ] Refinancing calculator — model the break-even point for refinancing
- [ ] Save and share loan scenarios
- [ ] Mobile-responsive layout improvements

---

## Author

Binyam Wodajo — [GitHub](https://github.com/bwodajo1) | [Email](mailto:bwodajo@umd.edu)
