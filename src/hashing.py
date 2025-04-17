# hashing algorithm
import hashlib

def hash_string(string):
    return hashlib.sha256(string.encode()).hexdigest()


if __name__ == "__main__":
    print(hash_string("hello"))