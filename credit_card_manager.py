class CreditCard:
    def __init__(self, alias, credit_limit):
        self.alias = alias
        self.credit_limit = credit_limit
        self.balance = 0
        self.purchases = []

    def add_purchase(self, amount, months):
        if amount > self.credit_limit - self.balance:
            print("No hay suficiente crédito disponible.")
            return
        self.purchases.append((amount, months))
        self.balance += amount

    def calculate_monthly_payment(self):
        total_payment = 0
        for amount, months in self.purchases:
            total_payment += amount / months
        return total_payment

    def pay_debt(self, amount):
        if amount >= self.balance:
            self.balance = 0  # Pagar toda la deuda
        else:
            self.balance -= amount  # Pagar una parte de la deuda

class CreditCardManager:
    def __init__(self):
        self.cards = []

    def add_card(self, alias, credit_limit):
        card = CreditCard(alias, credit_limit)
        self.cards.append(card)

    def review_cards(self):
        total_monthly_payment = 0
        for card in self.cards:
            monthly_payment = card.calculate_monthly_payment()
            total_monthly_payment += monthly_payment
            available_credit = card.credit_limit - card.balance
            print(f"Tarjeta: {card.alias}, Límite de crédito: {card.credit_limit:.2f}, Deuda total: {card.balance:.2f}, "
                  f"Pago mensual: {monthly_payment:.2f}, Crédito disponible: {available_credit:.2f}")

        print(f"Deuda mensual total: {total_monthly_payment:.2f}")

    def total_debt(self):
        return sum(card.balance for card in self.cards)

    def pay_card_debt(self, alias):
        for card in self.cards:
            if card.alias == alias:
                print(f"Deuda actual de {card.alias}: {card.balance:.2f}")
                choice = input("¿Deseas pagar toda la deuda (T) o una parte (P)? ").strip().upper()
                if choice == 'T':
                    card.pay_debt(card.balance)  # Pagar toda la deuda
                    print(f"Se ha pagado toda la deuda de {card.alias}.")
                elif choice == 'P':
                    amount = float(input("Ingresa el monto a pagar: "))
                    if amount > card.balance:
                        print("El monto a pagar no puede ser mayor que la deuda actual.")
                    else:
                        card.pay_debt(amount)  # Pagar una parte de la deuda
                        print(f"Se ha pagado ${amount:.2f} de la deuda de {card.alias}.")
                else:
                    print("Opción no válida.")
                return
        print("Tarjeta no encontrada.")

def main():
    manager = CreditCardManager()
    while True:
        print("\nOpciones:")
        print("1. Revisar tarjetas de crédito")
        print("2. Agregar tarjeta de crédito")
        print("3. Agregar compra a una tarjeta existente")
        print("4. Pagar deuda de una tarjeta")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            manager.review_cards()
            print(f"Deuda total: {manager.total_debt()}")
        elif choice == '2':
            alias = input("Ingresa el alias de la tarjeta: ")
            credit_limit = float(input("Ingresa el límite de crédito: "))
            manager.add_card(alias, credit_limit)
        elif choice == '3':
            print("Tarjetas disponibles:")
            for card in manager.cards:
                print(f"- {card.alias}")
            alias = input("Ingresa el alias de la tarjeta a la que deseas agregar una compra: ")
            for card in manager.cards:
                if card.alias == alias:
                    amount = float(input("Ingresa el monto de la compra: "))
                    months = int(input("Ingresa el número de meses (1, 3, 6, 9, 12, 15, 18): "))
                    card.add_purchase(amount, months)
                    break
            else:
                print("Tarjeta no encontrada.")
        elif choice == '4':
            print("Tarjetas disponibles:")
            for card in manager.cards:
                print(f"- {card.alias}")
            alias = input("Ingresa el alias de la tarjeta de la que deseas pagar la deuda: ")
            manager.pay_card_debt(alias)
        elif choice == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
