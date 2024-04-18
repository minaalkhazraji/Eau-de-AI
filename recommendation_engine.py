class Perfume:
    def __init__(self, name, notes, price, occasions):
        self.name = name
        self.notes = set(notes) #create a set of a bunch of notes
        self.price = price
        self.occasions = set(occasions)

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

    def add_edge(self, perfume1,perfume2):
        if perfume1 != perfume2:
            self.adjacency_list[perfume1].append(perfume2)
            self.adjacency_list[perfume2].append(perfume1)

    def find_edge(self, perfume):
        #get similar perfumes from graph
        return self.adjacency_list.get(perfume, [])

class RecommendationEngine:
    def __init__(self, perfumes):
        self.perfumes = perfumes
        self.hash = Hash()
        self.graph = Graph()
        self.build_methods()

    def build_methods(self):
        for perfume in self.perfumes:
            self.hash.add_perfume(perfume)
            self.graph.add_edge(perfume)
            self.add_similar_edges(perfume)

    def add_similar_edges(self, perfume):
        #checks for similar perfumes amongst existing perfumes
        existing_perfumes = list(self.graph.adjacency_list.keys())
        for existing_perfume in existing_perfumes:
            if any(note in existing_perfume.notes for note in perfume.notes):
                self.graph.add_edge(perfume, existing_perfume)

    def recommend(self, notes, price_range, ocassions, method):
        if method == 'graph':
            return self.recommend_graph(notes, price_range, ocassions)
        elif method == 'hash':
            return self.recommend_hash(notes, price_range, ocassions)

    def recommend_graph(self, notes, price_range, ocassions):
        #graph recommendation logic

    def recommend_hash(self, notes, price_range, ocassions):
        #hash recommendation logic