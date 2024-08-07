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