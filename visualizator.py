import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Dict

def visual(raw_trans_to_sub: Dict[str, str], transformator_to_every: Dict[str, List[str]], all_priority_queues: Dict[int, List], hour: int):
    # Створення графу
    G = nx.DiGraph()

    # Додавання вузлів
    for transformer, substation in raw_trans_to_sub.items():
        G.add_edge(substation, transformer)

    for transformer, consumers in transformator_to_every.items():
        for consumer in consumers:
            G.add_edge(transformer, consumer)

    # Додавання ваги
    for weight, substation, transformer in all_priority_queues[hour]:
        G[substation[0]][transformer]['weight'] = weight

    # Покращений розташунок вузлів із збільшеною відстанню між ними
    pos = nx.spring_layout(G, seed=42, k=1.5, iterations=50)

    # Візуалізація
    plt.figure(figsize=(18, 12))

    # Відображення вузлів
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', edgecolors='black')

    # Відображення ребер
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.7, edge_color='grey', arrows=True, arrowsize=12)

    # Відображення міток вузлів
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Відображення значень ребер
    edge_labels = {(s, t): f'{G[s][t]["weight"]:.2f}' for s, t in G.edges() if 'weight' in G[s][t]}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

    plt.title("Електромережа: Трансформатори, Підстанції та Споживачі", fontsize=15)
    plt.axis('off')
    plt.show()