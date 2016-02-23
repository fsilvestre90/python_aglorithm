class Queue(object):
    queue = []

    def Pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def Peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def Push(self, element):
        self.queue.append(element)
