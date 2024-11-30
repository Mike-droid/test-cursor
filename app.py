from flask import Flask, render_template, request, redirect, url_for
from credit_card_manager import CreditCardManager

app = Flask(__name__)
manager = CreditCardManager()

@app.route('/')
def index():
    return render_template('index.html', cards=manager.cards)

@app.route('/add_card', methods=['POST'])
def add_card():
    alias = request.form['alias']
    credit_limit = float(request.form['credit_limit'])
    manager.add_card(alias, credit_limit)
    return redirect(url_for('index'))

@app.route('/add_purchase', methods=['POST'])
def add_purchase():
    alias = request.form['alias']
    amount = float(request.form['amount'])
    months = int(request.form['months'])
    for card in manager.cards:
        if card.alias == alias:
            card.add_purchase(amount, months)
            break
    return redirect(url_for('index'))

@app.route('/pay_debt', methods=['POST'])
def pay_debt():
    alias = request.form['alias']
    amount = float(request.form['amount'])
    for card in manager.cards:
        if card.alias == alias:
            card.pay_debt(amount)
            break
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)