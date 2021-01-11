def new(num_buckets= 256):
    aMap = []
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    # hash() 內建哈希值
    return hash(key)% len(aMap)


def get_bucket(aMap, key):
    bucket_id = hash_key(aMap,key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    bucket = get_bucket(aMap,key)
    # enumerate 將數據下標及數據表示出來 (0,"Spring"),(1,"Summer")
    for i , kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k ,v
    return -1, key, default

def get(aMap, key, default=None):
    i, k , v = get_slot(aMap, key, default=default)
    return v


def set(aMap, key, value):
    bucket = get_bucket(aMap,key)
    i, k , v = get_slot(aMap, key)

    if i >= 0:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))

# xrange 不會直接生成一串list，而是每個產生一個值，range是一次產生所有值，因此xrange運行較快 記憶體小
def delete(aMap, key):
    bucket = get_bucket(aMap,key)
    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key ==k:
            del bucket[i]
            break

def list(aMap):
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k,v)
