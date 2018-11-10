# delete all numbers > 100 in linkedl

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

  def remove_greater(self, data_a):
    current = self.head
    prev = current

    while self.head.data > data_a:      
      self.head = current.next
      current = current.next
  
    while current:
      if current.data > data_a:
        current = current.next 
        prev.next = current     
      else:
        prev = current
        current = current.next
      
    if current is None:
      return


    

x = LinkedList()
x.head = node(10)
data2 = node(200)
data3 = node(59)
data4 = node(2)
data5 = node(400)
data6 = node(20)
data7 = node(20)
data8 = node(200)

x.head.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7
data7.next = data8

x.remove_greater(100)
x.printing()
