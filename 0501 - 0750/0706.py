class MyHashMap:

    def __init__(self):
        self.hash = dict()

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        return self.hash.get(key, -1)

    def remove(self, key: int) -> None:
        self.hash.pop(key, None)
