class ListNode:
    def __init__(self, data=-1):
        self.data = data
        self.next = None
      
    # O(N)
    def __iter__(self):
        # Make the node iterable
        current = self
        while current:
            yield current.data
            current = current.next

    # O(N)
    def __str__(self):
        elements = []
        current = self
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
  
    # O(N)
    def __len__(self):
        count = 0
        current = self
        while current:
            count += 1
            current = current.next
        return count