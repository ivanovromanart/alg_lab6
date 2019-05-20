class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.head = -1

    def push(self, v):
        if self.head == (len(self.storage) - 1):
            raise StackOverflowError()
        else:
            self.head += 1
            self.storage[self.head] = v

    def pop(self):
        if self.head == -1:
            raise StackIsEmptyError()
        else:
            a = self.storage[self.head]
            self.storage[self.head] = 0
            self.head -= 1
            return a

    def __len__(self):
        return self.head + 1