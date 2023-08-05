import sys
import warnings
from src.api_methods import graphs, pixels
from typing import Iterable


warnings.simplefilter("ignore")

def exit_program():
    sys.exit()


def show_interface(interface:dict):
    print('Here are possible methods')
    for method in interface.values():
        print(f'{method["label"]}: {method["description"]}')


graphs_interface = {
    'C': {
        'label': 'C',
        'description': 'Create new graph',
        'callable': graphs.create_new_graph
    },
    'L': {
        'label': 'L',
        'description': 'List all the graphs',
        'callable': graphs.extract_and_show_graph_data
    },
    'D': {
        'label': 'D',
        'description': 'Delete graph',
        'callable': graphs.delete_graph
    },
    'Q': {
        'label': 'Q',
        'description': 'Exit program',
        'callable': exit_program
    }
}

pixels_interface = {
    'C': {
        'label': 'C',
        'description': 'Create new pixel',
        'callable': pixels.post_pixel
    },
    'G': {
        'label': 'G',
        'description': 'Get pixel',
        'callable': pixels.get_pixel
    },
    'U': {
        'label': 'U',
        'description': 'Update pixel',
        'callable': pixels.update_pixel
    },
    'D': {
        'label': 'D',
        'description': 'Delete pixel',
        'callable': pixels.delete_pixel
    }
}


main_interface = {
    'G': {
        'label': 'G',
        'description': 'go to graphs interface',
        'callable': show_interface
    },
    'P': {
        'label': 'P',
        'description': 'go to pixels interface',
        'callable': show_interface
    },
    'Q': {
            'label': 'Q',
            'description': 'Exit program',
            'callable': exit_program
    }
}


def prompt_user(valid_options:Iterable):
    user_choice = input("Select option:> ").upper()
    while user_choice not in valid_options:
        user_choice = input("Select option:> ").upper()
    return user_choice


def main():
    while True:
        show_interface(main_interface)
        user_choice = prompt_user(main_interface.keys())
        if user_choice == 'G':
            show_interface(graphs_interface)
            user_choice = prompt_user(graphs_interface.keys())
            function_to_call = graphs_interface[user_choice]['callable']
            function_to_call()
        elif user_choice == 'P':
            show_interface(pixels_interface)
            user_choice = prompt_user(pixels_interface.keys())
            function_to_call = pixels_interface[user_choice]['callable']
            function_to_call()
        elif user_choice == 'Q':
            exit_program()


if __name__ == '__main__':
    main()