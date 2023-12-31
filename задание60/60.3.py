class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        keys = key.split('.')
        current_data = self.data
        for i, k in enumerate(keys):
            if k not in current_data:
                if i == len(keys) - 1:
                    current_data[k] = value
                else:
                    current_data[k] = {}
            current_data = current_data[k]

    def get(self, key):
        keys = key.split('.')
        current_data = self.data
        for k in keys:
            if k in current_data:
                current_data = current_data[k]
            else:
                return None
        return current_data

    def update(self, key, value):
        existing_data = self.get(key)
        if existing_data is not None:
            existing_data.update(value)

    def delete(self, key):
        keys = key.split('.')
        current_data = self.data
        for i, k in enumerate(keys):
            if k in current_data:
                if i == len(keys) - 1:
                    del current_data[k]
                else:
                    current_data = current_data[k]