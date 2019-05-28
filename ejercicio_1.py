

# Construir una función que reciba un grafo y en función del grafo indique como hacer un
# recorrido euleriano en caso de que sea conexo y que devuelva una lista con el orden de los
# nodos del recorrido


class Graph:

    def __init__(self, dictionary):
        self.nodes = dictionary.keys()
        self.edges = dictionary.values()
        self.graph = dictionary

    def add_node(self, new_node):
        self.graph[new_node] = []

    def del_node(self, node_to_remove):
        self.graph.pop(node_to_remove, None)

    def add_edge(self, source, target):
        self.graph[source].append(target)
        self.graph[target].append(source)

    def del_edge(self, source, target):
        self.graph[source].remove(target)
        self.graph[target].remove(source)

    def vecinos(self, n, m):
        pass


if __name__ == '__main__':
    print('hello')

    dictionary = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B']
    }

    grafo = Graph(dictionary)

    print('Creo un grafo \n%s' % grafo)
    print(50*'-')
    print('Estos son los nodos del grafo: \n%s' % grafo.nodes)
    print(50 * '-')
    print('Estos son las aristas del grafo: \n%s' % grafo.edges)
    print(50 * '-')
    print('Este es el grafo completo: \n%s' % grafo.graph)
    print(50 * '-')

    grafo.add_node('D')
    print(grafo.graph)
    print(50 * '-')

    grafo.del_node('D')
    print(grafo.graph)
    print(50 * '-')

    grafo.add_node('D')
    grafo.add_edge('D', 'B')
    print(grafo.graph)
    print(50 * '-')

    grafo.del_edge('D', 'B')
    print(grafo.graph)
    print(50 * '-')

