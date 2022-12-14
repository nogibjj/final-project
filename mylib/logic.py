from connect_db import connect_db,close_db

def query_specific(cursor,input_cat="Generation",input_name="9"):
    query = f"SELECT * from pokedex WHERE {input_cat}={input_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result




if __name__ == '__main__':
    conn,cursor = connect_db()
    result = query_specific(cursor)
    print("Query 1 result")
    print(result)
    close_db(conn)
