from src import interfaces
import os

def clear_terminal():
    os.system('clear')  # For macOS and Linux
    # Alternatively, you can use 'cls' on Windows: os.system('cls')


def main():
    while True:
        clear_terminal()
        interfaces.show_interface(interfaces.main_interface)
        user_choice = interfaces.prompt_user(interfaces.main_interface.keys())
        if user_choice == 'G':
            clear_terminal()
            interfaces.show_interface_prompt_user_and_call_function(interface=interfaces.graphs_interface)
            input('PRESS ANY KEY TO BACK TO MAIN MENU')
        elif user_choice == 'P':
            clear_terminal()
            interfaces.show_interface_prompt_user_and_call_function(interface=interfaces.pixels_interface)
            input('PRESS ANY KEY TO BACK TO MAIN MENU')
        elif user_choice == 'Q':
            interfaces.exit_program()


if __name__ == '__main__':
    main()

