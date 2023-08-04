# module to load and check env variables

import os
from environs import Env


def _load_env_variables():
    # Load environment variables from .env file
    env = Env()
    env.read_env()

    # Get environment variables from .env file
    USERNAME = os.environ.get('USERNAME')
    TOKEN = os.environ.get('TOKEN')

    env_variables = {
        'USERNAME': USERNAME,
        'TOKEN': TOKEN
    }

    return env_variables


env_variables = _load_env_variables()

# Function to check if environment variables are set
def check_env_variables(env_variables_list: list):
    if None in env_variables_list:
        raise ValueError("Environment variables weren't retrieved properly")


USERNAME = env_variables['USERNAME']
TOKEN = env_variables['TOKEN']


env_variables_to_check = [
    USERNAME or None,
    TOKEN or None
]

check_env_variables(env_variables_to_check)

