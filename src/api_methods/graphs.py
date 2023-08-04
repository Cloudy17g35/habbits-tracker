import requests
from src.authentication import get_headers
from src import endpoints


def create_new_graph() -> None:
    headers = get_headers()
    endpoint = endpoints.graphs_endpoint
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


def _get_graphs_data(endpoint, headers) -> dict or None:
    response = requests.get(endpoint, headers=headers)
    if response.ok:
        graphs = response.json()
        return graphs
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def extract_and_show_graph_data():
    headers = get_headers()
    endpoint = endpoints.graphs_endpoint
    graphs_data = _get_graphs_data(endpoint, headers)
    if graphs_data is None:
        raise ValueError("graph data cannot be None")
    graphs = graphs_data['graphs']
    for graph in graphs:
        graph_id = graph['id']
        graph_name = graph['name']
        graph_unit = graph['unit']
        graph_type = graph['type']
        graph_color = graph['color']
        graph_url = get_graph_link(endpoint, graph_id)

        print(f"Graph ID: {graph_id}")
        print(f"Graph Name: {graph_name}")
        print(f"Graph Unit: {graph_unit}")
        print(f"Graph Type: {graph_type}")
        print(f"Graph Color: {graph_color}")
        print(graph_url)
        print()


def get_graph_link(graphs_endpoint: str, graph_id: str) -> str:
    return f'{graphs_endpoint}/{graph_id}.html'


def delete_graph():
    headers = get_headers()
    endpoint = endpoints.graphs_endpoint
    graph_id = input('Provide graph id that you want to delete:> ')
    delete_endpoint = f'{endpoint}/{graph_id}'
    response = requests.delete(delete_endpoint, headers=headers)
    if not response.ok:
        print('Something went wrong')
    print(f'{response.text}')
