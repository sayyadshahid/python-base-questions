# Hashing is the process of converting data into a fixed-size value (hash),
# and it works only on hashable (immutable) data types like strings, numbers, and tuples.
 


table_size = 5
hash_table = [[] for _ in range(table_size)]

def insert(key, value):
    index = key % table_size
    hash_table[index].append((key, value))
    

def search(key):
    index = key % table_size
    for k, v in hash_table[index]:
        if k == key:
            return v
    return "Not Found"

insert(12, "A")
insert(22, "B")
insert(32, "C")

print(search(20))   # Output: B


# A hash table uses a hash function to convert keys into indices. If multiple keys map to the same index, collisions occur, which can be handled using chaining or probing techniques.