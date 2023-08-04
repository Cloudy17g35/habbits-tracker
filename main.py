import sys
from src.api_methods import graphs

def exit_program():
    sys.exit()


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


def show_graphs_interface_for_user(graphs_interface:dict):
    print('Here are possible methods:')
    for method in graphs_interface.values():
        print(f'{method["label"]}: {method["description"]}')


def main():
    while True:
        show_graphs_interface_for_user(graphs_interface)
        user_choice = input("Please choose one of possible methods:").upper()
        while user_choice.upper() not in graphs_interface.keys():
            user_choice = input("Please choose one of possible methods:").upper()
        function_to_call = graphs_interface[user_choice]['callable']
        function_to_call()


if __name__ == '__main__':
    main()