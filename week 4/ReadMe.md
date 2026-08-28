Activities diagram

Custom: 
start with register profile, after registered can view exchange rate.
1. Register profile first.
2. Registered can view exchange rate.

Staff:
view the exchange rate, and manage currency.

<img width="1213" height="1297" alt="image" src="https://github.com/user-attachments/assets/cd0b8f9a-b7e9-41db-9cd2-8b55e6d8a48d" />

Use case
Actor-Customer
1. Register Profile
    Customers register identity details (Name, Legal ID, Contact info)
2. View Exchange Rates
    Views the latest active conversion rates for various currency pairs.
3. Modify Profile --extend->  Register Profile
    Customers modify their identity details(Name, Contact info).


Actor-Staff
1. Update Rates --include-> view exchange rate
    Inputs or updates conversion rates into the database.
2. Manage Currency
    Support global currencies (e.g., USD, EUR, JPY).
3. View Exchange Rates
    Views the latest active conversion rates for various currency pairs.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2e6cc5bd-0b2c-48b2-bf4d-1a5846efd4ca" />



