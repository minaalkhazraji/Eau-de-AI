class Graph:
    def __int__(self):
        self.adjacency_list = {}


    def add_perfume(self, perfume):
        if perfume not in self.adjacency_list:
            self.adjacency_list[perfume] = []

    def addEdge(self, perfume1,perfume2):
        if perfume1 != perfume2:
            self.adjacency_list[perfume1].append(perfume2)
            self.adjacency_list[perfume2].append(perfume1)

