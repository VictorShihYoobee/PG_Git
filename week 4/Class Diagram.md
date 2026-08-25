I design 1 class diagram, and 5 main classes:

<img width="730" height="256" alt="image" src="https://github.com/user-attachments/assets/91a4d564-cffd-4de2-81a1-ab30b6307cc2" />

# Relationships

• Customer 1 ─── n Transaction (Association): A customer can make multiple transactions.

• Currency 1 ─── n ExchangeRate (Aggregation): A currency's Exchange rates vary over time.

• Currency 1 ─── n Transaction (Aggregation): Each transaction references a currency. A currency can included in different tranctions.

• ExchangeService ..> Transaction & ExchangeRate (Dependency): calculations and rate updates.

# Represented Functionality

Calculates converted values using $\text{convertedAmount} = \text{sourceAmount} \times \text{appliedRate}$, 
processes transactions, updates exchange rates, and manages currencies. 

# UML diagram shows below:

<img width="866" height="446" alt="image" src="https://github.com/user-attachments/assets/ec51a23e-eeca-4b2b-bb6b-af5c52eecc0f" />

