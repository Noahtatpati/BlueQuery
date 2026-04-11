import re

def extract_number(text):
    match = re.search(r'\d+', text)
    return match.group() if match else None


def generate_sql(query: str) -> str:
    q = query.lower()

    base = ""
    conditions = []
    order = ""
    limit = ""

    number = extract_number(q)

    if "customer" in q:
        base = "SELECT * FROM customers"
    elif "product" in q:
        base = "SELECT * FROM products"
    elif "order" in q:
        base = "SELECT * FROM orders"
    else:
        return "-- Could not identify table"

    if ("greater than" in q or "more than" in q) and number:
        if "spent" in q:
            conditions.append(f"total_spent > {number}")
        if "price" in q:
            conditions.append(f"price > {number}")

    if ("less than" in q or "below" in q) and number:
        if "spent" in q:
            conditions.append(f"total_spent < {number}")
        if "price" in q:
            conditions.append(f"price < {number}")

    if "after" in q and number:
        conditions.append(f"year > {number}")

    if "top" in q or "highest" in q:
        if "price" in q:
            order = "ORDER BY price DESC"
        elif "spent" in q:
            order = "ORDER BY total_spent DESC"

    if "lowest" in q:
        if "price" in q:
            order = "ORDER BY price ASC"

    if "top" in q and number:
        limit = f"LIMIT {number}"

    sql = base

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    if order:
        sql += " " + order

    if limit:
        sql += " " + limit

    sql += ";"

    return sql
