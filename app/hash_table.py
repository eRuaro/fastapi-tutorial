class HashTable:
    def __init__(self):
        self.hash_table = {}

    def add(self, key, value):
        """
        Adds or replaces a key-value pair to the hash table.
        """
        self.hash_table[key] = value

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.
        """
        self.hash_table.pop(key, None)

    def get(self, key):
        """
        Returns the value given a key from the hash table
        """
        return self.hash_table.get(key)
    