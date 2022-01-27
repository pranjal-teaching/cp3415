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


def get_player_info(player_id):
    """
    returns player name and age as a tuple for any given player_id
    :param player_id: id of the player
    :return: (name, age)
    """
    # Use the get_rows() function
    query = f"SELECT * FROM fantastic_games.players WHERE player_id = {player_id}"
    col_names, rows = get_rows(query)
    return rows[0][1], rows[0][2]



print(get_player_info(1))
