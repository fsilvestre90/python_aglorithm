import random

class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next  = None

class BrokenLinkedList:
  root = None
  def __init__(self):
    head = random.randint(3, 7)
    n = None
    for i in range(head):
      tmp = LinkedListNode(i)
      if n is not None:
        n.next = tmp
      else:
        self.root = tmp
      n = tmp
    tail = random.randint(3, 7)
    circle = n
    for i in range(tail):
      v = head + i
      tmp = LinkedListNode(v)
      n.next = tmp
      n = tmp
    n.next = circle

a = BrokenLinkedList()
n = a.root


def isBrokenLinkedList(incoming):
    runner = incoming.root
    walker = incoming.root

    while runner.next is not None and walker.next is not None:
        runner = runner.next
        runner = runner.next
        print("Runner at {}".format(runner.value))
        walker = walker.next
        print("Walker at {}".format(walker.value))
        if runner == walker:
            return True


print(isBrokenLinkedList(a))
