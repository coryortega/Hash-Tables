# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with capacity buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # (key: value) pair
        pair = LinkedPair(key, value)
        # hashing the key to find the bucket
        index = self._hash_mod(key)

        # If a key exists:
        if self.storage[index]:
            # The next node is set to that index
            pair.next = self.storage[index]
            # And that index equals the key/value pair
            self.storage[index] = pair
            # While pair exists
            while pair:
                # setting each pair equal to its next node
                pair = pair.next
        # if no key exists
        else:
            # Set that index in storage to equal that pair
            self.storage[index] = pair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Hashed key for the index
        index = self._hash_mod(key)
        # The item in storage with that index
        item = self.storage[index]

        # If item exists
        if item:
            # If linked list, loop through pairs
            if item.next:
                # Set "current pair" to that item
                current_pair = item
                
                # While "current pair" exists
                while current_pair:
                    # If the key within that pair is the same as the input key
                    if current_pair.key == key:
                        # That item in storage equals none
                        # item = current_pair.next
                        current_pair.next = None
                    # Cycle through
                    current_pair = current_pair.next
            else:
                # That index in storage equals None
                self.storage[index] = None
        # Else input key doesn't exist
        else:
            print("That item does not exist")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Hashed input key
        index = self._hash_mod(key)
        # The value of the pair with that index
        item = self.storage[index]
        # If the current item exists
        if item:
            # If that key/value pairs key is equal to the input key
            if item.key == key:
                # Return that pairs value
                return item.value
            # Else if there is multiple pairs stored at the index, loop through them, and find the one requested
            elif item.next:
                # "Current pair" equals that key/value
                current_pair = item
                # While that key/value exists
                while current_pair:
                    # If that key equals the input key
                    if current_pair.key == key:
                        # Return that pairs value
                        return current_pair.value
                    # Cycle through remaining pairs
                    current_pair = current_pair.next
        # Else 
        else:
            # Return None
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Times the existing capacity by 2
        self.capacity *= 2
        # "Old storage" equals the existing storage
        old_storage = self.storage
        # Add an empty place for each capacity
        self.storage = [None] * self.capacity

        # For each pair in the "Old Storage"
        for pair in old_storage:
            # Current Pair" equals that pair
            current_pair = pair
            
            # While that pair exists
            while current_pair:
                # Insert that key/value pair
                self.insert(current_pair.key, current_pair.value)
                # Cycle through existing pairs
                current_pair = current_pair.next 



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
