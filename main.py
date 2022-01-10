from mysql.connector import connect
from secret_data import HOSTNAME, USER_NAME, PASSWORD


def get_select_query_result(query):
    result = []
    with connect(host=HOSTNAME, user=USER_NAME, password=PASSWORD) as dbconnection:
        with dbconnection.cursor() as cursor:
            try:
                cursor.execute(query)
                for row in cursor:
                    result.append(row)
            except Exception as e:
                print(f'{query} did not execute correctly.\nHere is the error info:\n{e}')
    return result


my_query = """SELECT 
    actor_id, first_name, last_name
FROM
    sakila.actor
WHERE
    first_name LIKE 'A%';"""
actors = get_select_query_result(my_query)
for actor in actors:
    print(actor)
