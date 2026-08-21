class Customer:
    def __init__(self, customer_id, name, email, phone, id_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.id_number = id_number

    def __repr__(self):
        return f"Customer(ID={self.customer_id}, Name='{self.name}')"


class Currency:
    def __init__(self, currency_code, currency_name, symbol):
        self.currency_code = currency_code  # e.g., USD, EUR
        self.currency_name = currency_name  # e.g., US Dollar
        self.symbol = symbol                # e.g., $

    def __repr__(self):
        return f"Currency({self.currency_code} - {self.currency_name})"


class ExchangeRate:
    def __init__(self, rate_id, base_currency, target_currency, rate, updated_at):
        self.rate_id = rate_id
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = rate
        self.updated_at = updated_at

    def __repr__(self):
        return f"ExchangeRate({self.base_currency}/{self.target_currency} = {self.rate})"


class Transaction:
    def __init__(self, transaction_id, customer_id, source_currency, target_currency, source_amount, target_amount, rate, timestamp):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.source_currency = source_currency
        self.target_currency = target_currency
        self.source_amount = source_amount
        self.target_amount = target_amount
        self.rate = rate
        self.timestamp = timestamp

    def __repr__(self):
        return f"Transaction(ID={self.transaction_id}, {self.source_amount} {self.source_currency} -> {self.target_amount} {self.target_currency})"