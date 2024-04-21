#This file handles all logic related to data traversal using our data structures:
#Graph or Hash

class Perfume:
    def __init__(self, name, notes, price, occasions):
        self.name = name
        self.notes = set(notes) #create a set of a bunch of notes
        self.price = price
        self.occasions = set(occasions)

class Hash:

    def __init__(self):
        self.hash_table = {}

    def add_perfume(self, perfume):
        for note in perfume.notes:
            if note not in self.hash_table:
                self.hash_table[note] = [perfume]

            else:
                self.hash_table[note].append(perfume)

class Graph:
    def __init__(self):
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
            self.graph.add_perfume(perfume)
            self.add_similar_edges(perfume)


    def add_similar_edges(self, perfume):
        #checks for similar perfumes amongst existing perfumes
        existing_perfumes = list(self.graph.adjacency_list.keys())
        for existing_perfume in existing_perfumes:
            if any(note in existing_perfume.notes for note in perfume.notes):
                self.graph.add_edge(perfume, existing_perfume)

    def recommend(self, notes, minPrice, maxPrice, ocassions, method):
        if method == 'graph':
            return self.recommend_graph(notes, minPrice, maxPrice, ocassions)
        elif method == 'hash':
            return self.recommend_hash(notes, minPrice, maxPrice, ocassions)

    def recommend_graph(self, notes, minPrice, maxPrice, occasions):
        from collections import deque

        set_of_notes = set(notes.split(', '))
        set_of_occasions = set(occasions.split(', '))

        initial_matches = []
        for note in set_of_notes:
            if note in self.hash.hash_table:
                initial_matches.extend(self.hash.hash_table[note])

        # filtering out based on user pref

        initial_matches = [perfume for perfume in initial_matches if
                           minPrice <= perfume.price <= maxPrice and set_of_occasions.intersection(perfume.occasions)]

        # bfs through queue
        queue = deque(initial_matches)
        visited = set(initial_matches)
        recommended = []

        # loop until 10 recommendations are found
        while queue and len(recommended) < 10: # this means there is a limit to 10 reccs
            current = queue.popleft()
            if current not in visited:
                recommended.append(current)
                visited.add(current)

            for adjacent in self.graph.find_edge(current):
                if adjacent not in visited:
                    queue.append(adjacent)

        return recommended

    def recommend_hash(self, notes, minPrice, maxPrice, occasions):

        set_of_notes = set(notes.split(', '))
        set_of_occasions = set(occasions.split(', '))
        perfume_match = set()
        for note in set_of_notes:
            if note in self.hash.hash_table:
                perfume_match.update(self.hash.hash_table[note])

        reccommendedList = [perfume for perfume in perfume_match if
                   minPrice <= perfume.price <= maxPrice and set_of_occasions.intersection(perfume.occasions)]
        return reccommendedList if reccommendedList else []
#have to work on recc graph and recc hash
# check price range parsing works

