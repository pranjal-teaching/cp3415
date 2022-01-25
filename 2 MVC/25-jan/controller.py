from mysql.connector import connect

host = 'localhost'
user = 'root'
password = 'password'


def get_rows(query):
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            mysql_cursor.execute(query)
            column_names = mysql_cursor.column_names
            rows = mysql_cursor.fetchall()
            return column_names, rows


q1 = "SELECT * FROM fantastic_games.players;"
col_names, rows = get_rows(q1)

print(col_names)
print(rows)
