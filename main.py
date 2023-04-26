from pprint import pprint
import plotly.graph_objects as go
import networkx as nx
from matplotlib import pyplot as plt
from collections import deque


def print_graph(graph, color_of_nodes):
    my_pos = nx.spring_layout(graph, seed=100)
    nx.draw(graph, pos=my_pos, with_labels=True, node_color=color_of_nodes)
    plt.show()


def main():
    print("Поиск в ширину")
    print("###Cоздание графа###")
    ###################Ввод графа###################
    num_of_vert = int(input("Введите количество вершин графа: "))
    massive_of_vert = {i: set() for i in range(num_of_vert)}
    mas = []
    for i in range(num_of_vert):
        mas.append(i)

    print("Список доступных вершин:", mas, "\n")

    print("Введите ребра графа: ")
    element_1 = ''
    element_2 = ''

    while element_1 != '.' or element_2 != '.':
        element_1 = input("Введите первую вершину: ")
        element_2 = input("Введите вторую вершину: ")
        print("\n")
        if element_1 == '.' or element_2 == '.':
            print("Создание ребер графа закончено.")
            break

        else:
            element_1 = int(element_1)
            element_2 = int(element_2)
            massive_of_vert[element_1].add(element_2)
            massive_of_vert[element_2].add(element_1)

    print(massive_of_vert)
    graph = nx.Graph(massive_of_vert)
    graph.add_nodes_from(massive_of_vert.keys())

    for k, v in massive_of_vert.items(): #Создание дорог к вершинам графа
        graph.add_edges_from(([(k, t) for t in v]))

    print("Построенный граф отображен на экране")
    color_of_nodes = ["green"] * num_of_vert #Создание массива цветов вершин графа
    print_graph(graph, color_of_nodes)

    distances = [None] * num_of_vert # Создание массива дистанций вершиин
    start_vert = 0
    print("Начальная вершина:", start_vert)
    distances[start_vert] = 0
    distances_dig = {i: set() for i in range(num_of_vert)} #Тот же массив дистанций, преобразованный в словарь
                                                            #для удобного вывода
    queue = deque([start_vert]) # Создание очереди

    print("Очередь: ")
    #Реализация самого метода ПВШ
    while queue:
        print(queue)
        cur_vert = queue.popleft()
        for neigh_vert in massive_of_vert[cur_vert]:
            if distances[neigh_vert] is None:
                distances[neigh_vert] = distances[cur_vert] + 1
                distances_dig[distances[neigh_vert]].add(distances[distances[cur_vert]])
                queue.append(neigh_vert)

    #Присваение значений массива дистанций словарю дистанций (для удобного вывода)
    for i in range(num_of_vert):
        distances_dig[i] = distances[i]

    #Раскрашивание вершин графа и отображение
    for i in range(num_of_vert):
        for j in range(num_of_vert):
            if distances[i] == distances[j]:
                color_of_nodes[j] = "red"

        print_graph(graph, color_of_nodes)

    print("Таблица расстояний: ")
    pprint(distances_dig, width=1)


main()
