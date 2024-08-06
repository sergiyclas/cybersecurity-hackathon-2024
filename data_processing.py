alghorithm = "1 line, 2 line, 5 line"

import heapq
import json
import os
from datetime import datetime
from typing import List, Dict

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

COUNT_HOURS = 2

CURRENT_TIME = datetime.now()
CURRENT_DAY = CURRENT_TIME.strftime('%Y-%m-%d')
CURRENT_HOUR = int(CURRENT_TIME.strftime('%H'))
print(CURRENT_DAY, CURRENT_HOUR)

file_path_current = os.path.join('data', 'current_16_01_45_40.json')
file_path_historical = os.path.join('data', 'historical_16_01_45_40.json')
file_path_predict_weather = os.path.join('data', 'predict_weather_16_01_45_46.json')
file_path_tth = os.path.join('data', 'tth_06_02_07_43.json')


def parser_data(path: str):
    with open(path, 'r') as file:
        data = json.load(file)
        needed_data = {}
        for i in range(COUNT_HOURS):
            hour = str(CURRENT_HOUR + i) + ':00'
            needed_data[CURRENT_HOUR + i] = data[CURRENT_DAY][hour]

    return needed_data


def write_output_to_file(result, output_file_name="result"):
    file = open(output_file_name, 'w')
    file.write(str(result))
    file.close()


needed_data_current = parser_data(file_path_current)
needed_data_historical = parser_data(file_path_historical)
needed_data_predict_weather = parser_data(file_path_predict_weather)
print(needed_data_current)
print(needed_data_historical)
print(needed_data_predict_weather)


def visualization(graph: Dict[str, int]):
    nodes = set()
    for key in graph.keys():
        u, v = map(int, key.split('_'))
        nodes.add(u)
        nodes.add(v)

    nodes = sorted(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}

    n = len(nodes)
    graph_mx = np.zeros((n, n))

    for key, weight in graph.items():
        u, v = map(int, key.split('_'))
        i, j = node_index[u], node_index[v]
        graph_mx[i, j] = weight
        graph_mx[j, i] = weight

    adj_matrix = np.array(graph_mx)
    G = nx.Graph()
    n = adj_matrix.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Визначення позицій вершин для кращої візуалізації
    pos = nx.spring_layout(G)

    # Візуалізація графа
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")

    # Додавання підписів до ребер з вагами
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


def minimum_spanning_tree(graph: dict[str, Dict[str, int]]):
    used = set()
    res = 0
    start_node = (0, 0)
    min_heap = [start_node]
    # res_lst = []
    # prev = None

    while min_heap:
        current_weight, current_vertex = heapq.heappop(min_heap)

        if current_vertex not in used:
            used.add(current_vertex)
            res += current_weight
            # if not res_lst:
            #     prev = 'start_point'
            # else:
            #     prev = res_lst[-1][1]
            # res_lst.append((prev, current_vertex, current_weight))

            for vertex, weight in graph[current_vertex].items():
                if weight > 0 and vertex not in used:  # weight > 0, інакше будуть від'ємні цикли
                    heapq.heappush(min_heap, (weight, vertex))

    # print(res_lst)
    return res


def run(n: int, edges: List[str, str, int]):  # типу з вершини А до вершини Б є N МВт
    graph = {i: {} for i in range(n)}
    graph_mx = {f'{i}_{j}': k for i, j, k in edges}
    different_vertexes = [i for i, *_ in edges]
    different_vertexes += [i for _, i, __ in edges]
    different_vertexes = set(different_vertexes)

    for i in range(n):
        for j in range(n):
            graph[different_vertexes[i]][different_vertexes[j]] = graph_mx[
                f'{different_vertexes[i]}_{different_vertexes[j]}']

    return minimum_spanning_tree(graph)
