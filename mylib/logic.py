def query_all(cursor):
    query = "SELECT * from pokedex"
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
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def filter_by(cursor,input_cat,input_name,filter_str):
    if input_cat == "":
        query = f"SELECT {filter_str} from pokedex"
    else:
        query = f"SELECT {filter_str} from pokedex WHERE {input_cat}={input_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result