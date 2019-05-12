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
            self.head.prev = None

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
        if self.head is None:
            print("Empty!")
            return

        temp = self.head
        while temp is not None and temp.next is not None:
            print("Time:"+str(temp.time)+" Type:"+str(temp.type))
            temp = temp.next

        print("Time:" + str(temp.time) + " Type:" + str(temp.type))
        while temp is not None:
            print("Time:" + str(temp.time) + " Type:" + str(temp.type))
            temp = temp.prev


class Packet:
    def __init__(self,arrival_time):
        self.arrival_time = arrival_time


class Buffer:
    def __init__(self,size):
        self.size = size
        self.length = 0
        self.queue = []

    def insert(self,packet):
        self.queue.append(packet)
        self.length += 1

    def remove(self):
        if len(self.queue) is 0:
            print("Nothing to remove in this buffer!")
        else:
            self.queue.pop(0)
            self.length -= 1

    def need_drop(self):
        if self.length == self.size:
            return True
        else:
            return False


# 1. Initialize
GEL = DLL()




GEL.printList()
