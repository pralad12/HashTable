
class HashTable():

    def __init__(self, initial_size, h):
        self.hf = h
        self.array = [None] * initial_size
        self.collisions = 0
        self.s = 0

    def size(self):
        print(self.s)

    def put(self, key, value):
        keyNum = int(key)
        array_location = self.hf(keyNum)
        if self.array[array_location] is None:
            self.array[array_location] = (keyNum, value)
            self.s += 1
        elif self.array[array_location][0] == keyNum:
            self.array[array_location] = (keyNum, value)
        else:
            counter = 0
            while counter < len(self.array):
                if self.array[array_location] is not None:
                    array_location = self.hf(array_location + 1)
                    self.collisions += 1
                counter += 1
            self.array[array_location] = (keyNum, value)
            self.s += 1

    def get(self, key):
        keyNum = int(key)
        array_location = self.hf(keyNum)
        array_len = len(self.array)
        if self.array[array_location] is not None:
            if self.array[array_location][0] == keyNum:
                return self.array[array_location][1]
        else:
            counter = 0
            while counter < array_len:
                array_location = self.hf(array_location + 1)
                if self.array[array_location] is not None:
                    if self.array[array_location][0] == keyNum:
                        return self.array[array_location][1]
                counter += 1
            return None

    def delete(self, key):
        keyNum = int(key)
        array_location = self.hf(keyNum)
        array_len = len(self.array)
        if self.array[array_location] is not None:
            if self.array[array_location][0] == keyNum:
                self.array[array_location] = None
                self.s -= 1
        else:
            counter = 0
            while counter < array_len:
                array_location = self.hf(array_location + 1)
                if self.array[array_location] is not None:
                    if self.array[array_location][0] == keyNum:
                        self.array[array_location] = None
                        self.s -= 1
                counter += 1

    def probe(self, key):
        keyNum = int(key)
        array_location = self.hf(keyNum)
        array_len = len(self.array)
        if self.array[array_location] is not None:
            if self.array[array_location][0] == keyNum:
                return True
        else:
            counter = 0
            while counter < array_len:
                array_location = self.hf(array_location + 1)
                if self.array[array_location] is not None:
                    if self.array[array_location][0] == keyNum:
                        return True
                counter += 1
        return False

    def all_keys(self):
        to_return = []
        for i in range(len(self.array)):
            if self.array[i] is not None:
                key_val = self.array[i][0]
                to_return.append(key_val)
        return to_return
