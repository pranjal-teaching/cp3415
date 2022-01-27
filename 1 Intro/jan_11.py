from mysql.connector import connect
from prettytable import PrettyTable
from secret_data import HOSTNAME, USER_NAME, PASSWORD


def get_select_query_result(query):
    """
    run query and return the result set along with the column headers
    """
    result = []
    with connect(host=HOSTNAME, user=USER_NAME, password=PASSWORD) as dbconnection: # Step 1
        with dbconnection.cursor() as cursor:   # Step 2
            try:
                cursor.execute(query) # Step 3
                result.append(cursor.column_names)
                result += cursor.fetchall()
            except Exception as e:
                print(f'query failed. Error info:\n{e}')
    return result


my_query = """SELECT * FROM fantastic_games.game """

results = get_select_query_result(my_query)
x = PrettyTable()
x.field_names = results[0]
for row in results[1:]:
    x.add_row(row)
print(x)
