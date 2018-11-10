class node():
  def __init__(self, data=None):
    self.data = data
    self.next = None
  
class LinkedList():
  def __init__(self):
    self.head = None
  
  def printing(self):
    printval = self.head
    while printval:
      print(printval.data)
      printval = printval.next

  def remove_dupl(self):
    pointer = self.head
    while pointer:
      current = pointer.next
      prev = pointer
      while current is not None:
        if current.data == pointer.data:
          current = current.next
          prev.next = current
        else:
          prev = current
          current = current.next
      pointer = pointer.next


    # while current:
    #   if prev.data == current.data:
    #     current = current.next
    #     prev.next = current
    #   else:
    #     prev = current
    #     current = current.next
    #     prev.next = current

x = LinkedList()
x.head = node(200)
data2 = node(200)
data3 = node(59)
data4 = node(2)
data5 = node(400)
data6 = node(20)
data7 = node(20)
data8 = node(20)

x.head.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7
data7.next = data8

x.remove_dupl()
x.printing()
