
def query_all(cursor):
    query = f"SELECT * from pokedex"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query_specific(cursor,input_cat="Generation",input_name="9"):
    query = f"SELECT * from pokedex WHERE {input_cat}={input_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def order_by(cursor,input_cat,input_name,order_cat,order_rule):
    if input_cat == "":
        query = f"SELECT * from pokedex ORDER BY {order_cat} {order_rule}"
    else:
        query = f"SELECT * from pokedex WHERE {input_cat}={input_name} ORDER BY {order_cat} {order_rule}"
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    