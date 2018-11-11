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

  def merge(self,y):
    p = self.head
    q = y.head
    s = None

    if p is None:
      return q
    
    if q is None:
      return p

    if p.data <= q.data:
      s = p
      p = s.next
    else:
      s = q
      q = s.next

    new_head = s
    while p and q:
      if p.data <= q.data:
        s.next = p
        s = p
        p = s.next
      else:
        s.next = q
        s = q
        q = s.next
    
    if not p:
      s.next = q
    if not q:
      s.next = p
    
    return new_head
    



x = LinkedList()
x.head = node(10)
data2 = node(20)
data3 = node(59)
data4 = node(60)
data5 = node(80)
data6 = node(120)
data7 = node(150)
data8 = node(200)

x.head.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7
data7.next = data8

y = LinkedList()
y.head = node(1)
data2 = node(2)
data3 = node(59)
data4 = node(60)
data5 = node(61)
data6 = node(90)
data7 = node(100)
data8 = node(200)

y.head.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7
data7.next = data8



x.merge(y)
x.printing()
