class Stack(object):
    stack = []

    def Pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def Peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def Push(self, element):
        self.stack.append(element)

    def Count(self):
        return len(self.stack)
