class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.cap = capacity
        self.data = {}

    def get(self, key: str) -> str:
        if key not in self.data:
            return ""
        
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            self.data.pop(key)

        self.data[key] = value

        if len(self.data) > self.cap:
            oldest = next(iter(self.data))
            self.data.pop(oldest)

    def rem(self, key: str) -> None:
        if key in self.data:
            self.data.pop(key)