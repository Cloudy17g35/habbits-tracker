from src.env_handler import TOKEN


def get_headers(token=TOKEN):
    headers = {'X-USER-TOKEN': token}
    return headers


headers = get_headers(TOKEN)