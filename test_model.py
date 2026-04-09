from model import generate_sql
from database import run_query

query = "show all customers"

sql = generate_sql(query)
result = run_query(sql)

print("Input:", query)
print("Generated SQL:", sql)
print("Result:", result)