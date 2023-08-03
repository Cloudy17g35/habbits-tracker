import os
from environs import Env
from src import api_methods

# Load environment variables from .env file
env = Env()
env.read_env()

# Get environment variables from .env file
USERNAME = os.environ.get('USERNAME')
TOKEN = os.environ.get('TOKEN')

# List of environment variables to check
env_variables_to_check = [
    USERNAME or None,
    TOKEN or None
]


# Function to check if environment variables are set
def check_env_variables(env_variables_list: list):
    if None in env_variables_list:
        raise ValueError("Environment variables weren't retrieved properly")


# Function to get API endpoints
def get_api_endpoints():
    pixela_endpoint = 'https://pixe.la/v1/users'
    api_endpoints = {
        # This is the general endpoint to create new graphs or get existing ones
        'graphs_endpoint': f'{pixela_endpoint}/{USERNAME}/graphs'
    }
    return api_endpoints

def get_headers(token):
    headers = {'X-USER-TOKEN': token}
    return headers


graphs_interface = {
    'C': {
        'label': 'C',
        'description': 'Create new graph',
        'callable': api_methods.create_new_graph
    },
    'L': {
        'label': 'L',
        'description': 'List all the graphs',
        'callable': api_methods.extract_and_show_graph_data
    },
    'D': {
        'label': 'D',
        'description': 'Delete graph',
        'callable': api_methods.delete_graph
    }
}


def show_graphs_interface_for_user(graphs_interface:dict):
    print('Here are possible methods:')
    for method in graphs_interface.values():
        print(f'{method["label"]}: {method["description"]}')


def main():
    endpoints = get_api_endpoints()
    graphs_endpoint = endpoints['graphs_endpoint']
    headers = get_headers(TOKEN)
    show_graphs_interface_for_user(graphs_interface)
    user_choice = input("Please choose one of possible methods:").upper()
    # graphs_interface keys are upper case
    while user_choice.upper() not in graphs_interface.keys():
        user_choice = input("Please choose one of possible methods:")
    function_to_call = graphs_interface[user_choice]['callable']
    function_to_call(graphs_endpoint, headers)


if __name__ == '__main__':
    main()