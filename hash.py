class Hash:

    def __init__(self):
        self.hashtable = {}

    def add_perfume(self, perfume):
        for note in perfume.notes:
            if note not in self.hash_table:
                self.hash_table[note] = [perfume]

            else:
                self.hashtable[note].append(perfume)