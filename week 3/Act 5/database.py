import sqlite3
from models import Customer, Currency, ExchangeRate, Transaction

class DatabaseManager:
    def __init__(self, db_name="money_exchange.db"):
        self.db_name = db_name
        self.initialize_database()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def initialize_database(self):
        """Creates necessary tables if they do not exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 1. Customers Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    phone TEXT,
                    id_number TEXT UNIQUE NOT NULL
                )
            ''')

            # 2. Currencies Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS currencies (
                    currency_code TEXT PRIMARY KEY,
                    currency_name TEXT NOT NULL,
                    symbol TEXT
                )
            ''')

            # 3. Exchange Rates Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS exchange_rates (
                    rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    base_currency TEXT,
                    target_currency TEXT,
                    rate REAL NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (base_currency) REFERENCES currencies(currency_code),
                    FOREIGN KEY (target_currency) REFERENCES currencies(currency_code)
                )
            ''')

            # 4. Transactions Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    source_currency TEXT,
                    target_currency TEXT,
                    source_amount REAL NOT NULL,
                    target_amount REAL NOT NULL,
                    rate REAL NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY (source_currency) REFERENCES currencies(currency_code),
                    FOREIGN KEY (target_currency) REFERENCES currencies(currency_code)
                )
            ''')
            conn.commit()

    def add_customer(self, customer: Customer):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO customers (name, email, phone, id_number)
                VALUES (?, ?, ?, ?)
            ''', (customer.name, customer.email, customer.phone, customer.id_number))
            conn.commit()
            return cursor.lastrowid

    def add_currency(self, currency: Currency):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO currencies (currency_code, currency_name, symbol)
                VALUES (?, ?, ?)
            ''', (currency.currency_code, currency.currency_name, currency.symbol))
            conn.commit()

    def set_exchange_rate(self, base: str, target: str, rate: float):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO exchange_rates (base_currency, target_currency, rate)
                VALUES (?, ?, ?)
            ''', (base, target, rate))
            conn.commit()

    def get_latest_rate(self, base: str, target: str):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT rate FROM exchange_rates 
                WHERE base_currency = ? AND target_currency = ? 
                ORDER BY updated_at DESC LIMIT 1
            ''', (base, target))
            row = cursor.fetchone()
            return row[0] if row else None

    def record_transaction(self, tx: Transaction):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO transactions (customer_id, source_currency, target_currency, source_amount, target_amount, rate)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (tx.customer_id, tx.source_currency, tx.target_currency, tx.source_amount, tx.target_amount, tx.rate))
            conn.commit()
            return cursor.lastrowid