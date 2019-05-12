class Event:
    def __init__(self, next = None, prev = None, time = None, type = None):
        self.next = next # reference to next event in DLL
        self.prev = prev # reference to previous event in DLL
        self.time = time
        self.type = type


class DLL:
    def __init__(self):
        self.head = None

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next

    def insert(self,new_time,new_type):
        new_event = Event(time=new_time,type=new_type)

        # empty linked list
        if self.head is None:
            new_event.prev = None
            new_event.next = None
            self.head = new_event
        # not empty linked list
        else:
            if self.head.time > new_time:
                new_event.prev = None
                new_event.next = self.head
                self.head.prev = new_event
                self.head = new_event
                return
            temp: Event = self.head
            while temp.next is not None:
                if temp.time <= new_time < temp.next.time:
                    new_event.prev = temp
                    new_event.next = temp.next
                    temp.next.prev = new_event
                    temp.next = new_event
                    return
                temp = temp.next
            temp.next = new_event
            new_event.prev = temp
            new_event.next = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print("Time:"+str(temp.time)+" Type:"+str(temp.type))
            temp = temp.next


llist = DLL()
llist.insert(3,1)
llist.insert(2,5)
llist.insert(3,1)
llist.insert(339,7)
llist.insert(339,7)
llist.insert(2,5)
llist.insert(2,5)
llist.insert(339,7)
llist.printList()

llist.remove_first()
llist.remove_first()
llist.remove_first()
llist.remove_first()
llist.printList()
