"""Min Max Stack Construction"""
class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        last_index = len(self.stack) - 1
        return self.stack[last_index]

    def pop(self):
        last_index = len(self.stack) - 1
        value_pop = self.stack[last_index]
        del self.stack[last_index]
        return value_pop

    def push(self, number):
        self.stack.append(number)

    def getMin(self):
        minimum = min(self.stack)
        return minimum

    def getMax(self):
        maximum = max(self.stack)
        return maximum
