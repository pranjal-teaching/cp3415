from mysql.connector import connect

host = 'localhost'
user = 'root'
password = 'password'

# Step 1: Create Connection Object
mysql_connection_object = connect(host=host, user=user, password=password)

# Step 2: Create a cursor object
mysql_cursor = mysql_connection_object.cursor()

# Step 3: Execute a simple query
query = "show databases"
mysql_cursor.execute(query)
print(mysql_cursor.column_names)
for row in mysql_cursor:
    print(row)

# Step 4: Commit Changes (when you make changes for example insert etc.)
mysql_connection_object.commit()

# Step 5: Close cursor and connection
mysql_cursor.close()
mysql_connection_object.close()
