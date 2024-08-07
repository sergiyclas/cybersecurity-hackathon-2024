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
