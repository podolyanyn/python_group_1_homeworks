class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def __getitem__(self, key):
        hash_value = hash(key) % self.size
        bucket = self.table[hash_value]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        hash_value = hash(key) % self.size
        bucket = self.table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def __contains__(self, key):
        hash_value = hash(key) % self.size
        bucket = self.table[hash_value]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def __len__(self):
        count = 0
        for bucket in self.table:
            count += len(bucket)
        return count

hash_table = HashTable(20)
hash_table['qwerty'] = 10
hash_table['qwer'] = 5
hash_table['asdf'] = 3

print('Length:', len(hash_table))
print('qwerty in hash_table:', 'qwerty' in hash_table)
print('qwert in hash_table:', 'qwert' in hash_table)
print('Value for "asdf":', hash_table['asdf'])