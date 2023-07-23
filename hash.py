# HashTable class using chaining. Code from Webinar
class ChainingHashTable:
    # Constructor with optional initial capacity parameter set to 10
    # Assigns all buckets with an empty list
    # O(n) linear
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table
    # O(1) constant time
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where the package will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in hash table
    # Returns the package if found, None otherwise
    # O(1) constant time
    def search(self, key):
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # removes an item with matching key from the hash table
    # O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
