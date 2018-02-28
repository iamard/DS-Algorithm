class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data, end = " ")
            curr = curr.next
        
    def appendData(self, data):
        node = Node(data)
        
        if (self.head is None):
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node

def mergeList(list1, list2):
    if list1.head is None:
        return list2
    elif list2.head is None:
        return list1
    else:
        list1  = list1.head
        list2  = list2.head
        result = LinkedList()
        curr   = Node(0)
        result.head = curr
        while list1 or list2:
            if list1 is None:
                curr.next = list2
                list2 = list2.next
            elif list2 is None:
                curr.next = list1
                list1 = list1.next
            elif list1.data <= list2.data:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            curr.next = None
        result.head = result.head.next
        return result

if __name__ == "__main__":
    # 10->20->30->40->50
    list1 = LinkedList()
    list1.appendData(10)
    list1.appendData(20)
    list1.appendData(30)
    list1.appendData(40)
    list1.appendData(50)
 
    # 5->15->18->35->60
    list2 = LinkedList()
    list2.appendData(5)
    list2.appendData(15)
    list2.appendData(18)
    list2.appendData(35)
    list2.appendData(60)
            
    list3 = mergeList(list1, list2)
    list3.printList()