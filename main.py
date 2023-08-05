from src import interfaces
from typing import Iterable


def prompt_user(valid_options:Iterable):
    user_choice = input("Select option:> ").upper()
    while user_choice not in valid_options:
        user_choice = input("Select option:> ").upper()
    return user_choice


def main():
    while True:
        interfaces.show_interface(interfaces.main_interface)
        user_choice = prompt_user(interfaces.main_interface.keys())
        if user_choice == 'G':
            interfaces.show_interface(interfaces.graphs_interface)
            user_choice = prompt_user(interfaces.graphs_interface.keys())
            function_to_call = interfaces.graphs_interface[user_choice]['callable']
            function_to_call()
        elif user_choice == 'P':
            interfaces.show_interface(interfaces.pixels_interface)
            user_choice = prompt_user(interfaces.pixels_interface.keys())
            function_to_call = interfaces.pixels_interface[user_choice]['callable']
            function_to_call()
        elif user_choice == 'Q':
            interfaces.exit_program()


if __name__ == '__main__':
    main()