class Hash:

    def __init__(self):
        self.hashtable = {}

    def add_perfume(self, perfume):
        for note in perfume.notes:
            if note not in self.hash_table:
                self.hash_table[note] = [perfume]

            else:
                self.hashtable[note].append(perfume)

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

