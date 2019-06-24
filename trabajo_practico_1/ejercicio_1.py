import numpy as np

# Construir una función que reciba un grafo y en función del grafo indique como hacer un
# recorrido euleriano en caso de que sea conexo y que devuelva una lista con el orden de los
# nodos del recorrido


class Graph:

    def __init__(self, dictionary):
        self.nodes = dictionary.keys()
        self.edges = dictionary.values()
        self.graph = dictionary
        self.matrix = self.build_matrix()

    def fit_partial(self):
        return Graph(self.graph)

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

    def vecinos(self, key):
        vecinos = self.graph[key]
        return vecinos

    def build_matrix(self):
        keys = sorted(self.graph.keys())
        size = len(keys)

        matrix = np.array([[0] * size for i in range(size)])

        for a, b in [(keys.index(a), keys.index(b)) for a, row in self.graph.items() for b in row]:
            matrix[a][b] = 2 if (a == b) else 1

        return matrix

    def is_connected(self, nodos_encontrados=None, nodo_inicial=None):

        if nodos_encontrados is None:
            nodos_encontrados = set()
        gdict = self.graph
        nodos = list(gdict.keys())
        if not nodo_inicial:
            nodo_inicial = nodos[0]

        nodos_encontrados.add(nodo_inicial)
        if len(nodos_encontrados) != len(nodos):
            for nodo in gdict[nodo_inicial]:
                if nodo not in nodos_encontrados:
                    if self.is_connected(nodos_encontrados, nodo):
                        return True
        else:
            return True
        return False

    def node_grade(self, key):
        return 'even' if (len(self.vecinos(key)) % 2) == 0 else 'odd'


    # A DFS based function to count reachable vertices from v

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count = count + self.DFSCount(i, visited)
        return count

        # The function to check if edge u-v can be considered as next edge in

    # Euler Tour
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:

        #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            ''' 
             2) If there are multiple adjacents, then u-v is not a bridge 
                 Do following steps to check if u-v is a bridge 

            2.a) count of vertices reachable from u'''
            visited = {node: False for node in self.nodes}
            count1 = self.DFSCount(u, visited)

            '''2.b) Remove edge (u, v) and after removing the edge, count 
                vertices reachable from u'''
            self.del_edge(u, v)
            visited = {node: False for node in self.nodes}
            count2 = self.DFSCount(u, visited)

            # 2.c) Add the edge back to the graph
            self.add_edge(u, v)

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True

    # Print Euler tour starting from vertex u
    def printEulerUtil(self, u, recorrido=[]):
        # Recur for all the vertices adjacent to this vertex
        #print(u)
        #print(self.graph)

        recorrido.append(u)
        for v in self.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                #print("%s-%s " % (u, v))
                self.del_edge(u, v)
                self.printEulerUtil(v, recorrido)
        return recorrido

    '''The main function that print Eulerian Trail. It first finds an odd 
   degree vertex (if there is any) and then calls printEulerUtil() 
   to print the path '''

    def printEulerTour(self):
        # Find a vertex with odd degree
        u = list(self.nodes)[0]
        for i in list(self.nodes):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        print(" ")
        return self.printEulerUtil(u)



    def find_euler_path(self):

        if not self.is_connected():
            print('El grafo no esta conectado')
            return []

        grades = [self.node_grade(key) for key in self.nodes]
        if 'odd' in grades:
            print('Existen nodos con grado impar')
            return []

        print('OK')
        grafo_temp = Graph(self.graph)
        return grafo_temp.printEulerTour()





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
    grafo.add_edge('D', 'C')
    grafo.add_edge('A', 'D')
    print(grafo.graph)
    print(50 * '-')

    grafo = grafo.fit_partial()
    print(grafo.build_matrix())

    print(grafo.find_euler_path())
