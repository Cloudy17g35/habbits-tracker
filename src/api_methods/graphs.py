import requests

def create_new_graph(endpoint: str, headers: dict) -> None:
    """
    Create a new graph on Pixela.

    Args:
        endpoint (str): The API endpoint URL for creating a new graph.
        headers (dict): The request headers including authentication token.

    Returns:
        None
    """
    graph_config = {
        'id': input("Graph ID:> "),
        'name': input("Graph name:> "),
        'unit': input('Graph unit (commits, minutes, kilometers):> '),
        'type': input('Type (int, float):> '),
        'color': 'ajisai'  # setting the default color
    }

    response = requests.post(endpoint, headers=headers, json=graph_config)
    response_text = response.text
    if not response.ok:
        print('Something went wrong')
    print(response_text)


def get_graphs_data(endpoint: str, headers: dict) -> dict or None:
    """
    Retrieve a list of all graphs from Pixela.

    Args:
        endpoint (str): The API endpoint URL for retrieving all graphs.
        headers (dict): The request headers including authentication token.

    Returns:
        dict or None: A dictionary containing information about all graphs,
                     or None if there was an error in the request.
    """
    response = requests.get(endpoint, headers=headers)

    if response.ok:
        graphs = response.json()
        return graphs
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def extract_and_show_graph_data(graphs_endpoint: str, headers: dict):
    """
    Extract and display graph data from the API response.

    Args:
        graphs_endpoint (str): The API endpoint URL for retrieving all graphs.
        headers (dict): The request headers including authentication token.

    Returns:
        None
    """
    graphs_data = get_graphs_data(endpoint=graphs_endpoint, headers=headers)
    if graphs_data is None:
        raise ValueError("graph data cannot be None")
    graphs = graphs_data['graphs']
    for graph in graphs:
        graph_id = graph['id']
        graph_name = graph['name']
        graph_unit = graph['unit']
        graph_type = graph['type']
        graph_color = graph['color']
        graph_url = get_graph_link(graphs_endpoint, graph_id)

        print(f"Graph ID: {graph_id}")
        print(f"Graph Name: {graph_name}")
        print(f"Graph Unit: {graph_unit}")
        print(f"Graph Type: {graph_type}")
        print(f"Graph Color: {graph_color}")
        print(graph_url)
        print()


def get_graph_link(graphs_endpoint: str, graph_id: str) -> str:
    """
    Generate the URL for a specific graph.

    Args:
        graphs_endpoint (str): The base URL of the graph endpoints.
        graph_id (str): The ID of the graph.

    Returns:
        str: The URL for the specific graph.
    """
    return f'{graphs_endpoint}/{graph_id}.html'


def delete_graph(graphs_endpoint: str, headers: dict):
    """
    Delete a graph on Pixela.

    Args:
        graphs_endpoint (str): The base URL of the graph endpoints.
        headers (dict): The request headers including authentication token.

    Returns:
        None
    """
    graph_id = input('Provide graph id that you want to delete:> ')
    delete_endpoint = f'{graphs_endpoint}/{graph_id}'
    response = requests.delete(delete_endpoint, headers=headers)
    if not response.ok:
        print('Something went wrong')
    print(f'{response.text}')
