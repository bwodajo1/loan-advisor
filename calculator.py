def monthly_payment(principal, annual_rate, years):
    r = annual_rate / 100 / 12
    n = years * 12
    if r == 0:
        return round(principal / n, 2)
    payment = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return round(payment, 2)


def amortization_schedule(principal, annual_rate, years):
    r = annual_rate / 100 / 12
    n = years * 12
    payment = monthly_payment(principal, annual_rate, years)
    schedule = []
    balance = principal
    for month in range(1, n + 1):
        interest = round(balance * r, 2)
        principal_paid = round(payment - interest, 2)
        balance = round(balance - principal_paid, 2)
        if balance < 0:
            balance = 0.0
        schedule.append({
            "month": month,
            "payment": payment,
            "principal": principal_paid,
            "interest": interest,
            "balance": balance,
        })
    return schedule


def loan_summary(principal, annual_rate, years):
    payment = monthly_payment(principal, annual_rate, years)
    n = years * 12
    total_paid = round(payment * n, 2)
    total_interest = round(total_paid - principal, 2)
    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "monthly_payment": payment,
        "total_paid": total_paid,
        "total_interest": total_interest,
        "n_payments": n,
    }