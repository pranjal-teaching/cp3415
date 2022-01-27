from controller import *


def display_options():
    print('1. Get Player Info By PlayerID')
    print('2. Display All Players')
    print('3. Get Game Info')
    print('4. Display All Games')
    print('0. Exit')


def main():
    while True:
        display_options()
        choice = int(input('Enter Choice: '))
        if choice == 1:
            player_id = int(input('Enter Player ID: '))
            player_name, player_age = get_player_info(player_id)
            print(f'Player Name = {player_name}\tPlayer Age: {player_age}')
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 0:
            break
        input('Hit enter to continue\t')


if __name__ == "__main__":
    main()
