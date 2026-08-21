from database import DatabaseManager
from models import Customer, Currency, Transaction

def main():
    db = DatabaseManager()

    print("=== 1. Setting up Currencies ===")
    db.add_currency(Currency("USD", "US Dollar", "$"))
    db.add_currency(Currency("EUR", "Euro", "€"))
    db.add_currency(Currency("JPY", "Japanese Yen", "¥"))

    print("=== 2. Setting up Exchange Rates ===")
    db.set_exchange_rate("USD", "EUR", 0.92)
    db.set_exchange_rate("USD", "JPY", 155.50)

    print("=== 3. Registering a Customer ===")
    customer = Customer(None, "Alice Smith", "alice@example.com", "+123456789", "ID987654321")
    customer_id = db.add_customer(customer)
    print(f"Registered Customer with ID: {customer_id}")

    print("=== 4. Executing Currency Exchange Transaction ===")
    source_curr = "USD"
    target_curr = "EUR"
    amount_to_exchange = 500.0  # USD

    rate = db.get_latest_rate(source_curr, target_curr)
    if rate:
        converted_amount = amount_to_exchange * rate
        tx = Transaction(None, customer_id, source_curr, target_curr, amount_to_exchange, converted_amount, rate, None)
        tx_id = db.record_transaction(tx)
        print(f"Transaction Successful! ID: {tx_id}")
        print(f"Exchanged {amount_to_exchange} {source_curr} to {converted_amount:.2f} {target_curr} at rate {rate}.")
    else:
        print("Exchange rate not found.")

if __name__ == "__main__":
    main()