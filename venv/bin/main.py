import random
import math
import sys


class Event:
    def __init__(self, next=None, prev=None, time=None, type=None):
        self.next = next  # reference to next event in DLL
        self.prev = prev  # reference to previous event in DLL
        self.time = time
        self.type = type  # 1: arrival 2: departure


class DLL:
    def __init__(self):
        self.head = None

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def insert(self, new_time, new_type):
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

    def print_list(self):
        if self.head is None:
            print("Empty!")
            return

        print("-----start-----")
        temp = self.head
        while temp is not None and temp.next is not None:
            print("Time:"+str(temp.time)+" Type:"+str(temp.type))
            temp = temp.next

        print("Time:" + str(temp.time) + " Type:" + str(temp.type))
        # while temp is not None:
        #     print("Time:" + str(temp.time) + " Type:" + str(temp.type))
        #     temp = temp.prev

        print("-----end-----")


class Packet:
    def __init__(self, service_time):
        self.service_time = service_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def insert(self, packet):
        self.queue.append(packet)

    def remove(self):
        if len(self.queue) is 0:
            print("Nothing to remove in this buffer!")
        else:
            self.queue.pop(0)

    def need_drop(self):
        if len(self.queue) == self.size:
            return True
        else:
            return False


flag = input("Regular or extra credit? (r / e) : ")

if flag == "e":
    print("We go extra credit mode: Pareto distribution!")
else:
    if flag == "r":
        print("We go regular mode: Negative exponential distribution!")
    else:
        print("I don't understand. I will go regular mode anyway.")
        flag = "r"


def nedt(rate):  # negative exponentially distributed time
    u = random.uniform(0, 1)
    if flag == "e":
        return pareto(rate)
    return (-1 / float(rate)) * math.log(1 - u)


def pareto(rate):  # pareto distribution
    u = random.uniform(0, 1)
    alpha = 100
    my_lambda = (alpha - 1) / float(rate)
    return my_lambda * (pow(1 - u, -1 / alpha) - 1)


# 1. Initialize
buffer_size = input("Please enter the buffer size (type i for infinite buffer) : ")
arrival_rate = input("Please enter the arrival rate (lambda) : ")
service_rate = input("Please enter the service rate (mu) : ")

if buffer_size == "i":
    buffer_size = int(sys.maxsize)

time = 0  # current time
busy_time = 0  # count of the time the server is busy
packets_dropped = 0  # number of packets dropped
GEL = DLL()
buffer = Buffer(buffer_size)
length = 0  # number of packets in the queue
get_busy_time = 0  # record the start of one busy time
busy = False  # record the current server state
queue_length_areas = 0  # record the sum of the areas

GEL.insert(time + nedt(arrival_rate), 1)

# 2. Loop
for i in range(100000):
    # GEL.print_list()
    event = Event(time=GEL.head.time, type=GEL.head.type)  # make a copy then remove
    GEL.remove_first()
    queue_length_areas += (event.time - time) * max(0, length - 1)  # length
    if event.type == 1:  # arrival
        # set current time to be the event time
        time = event.time
        # schedule the next event
        next_arrival_time = time + nedt(arrival_rate)
        new_packet = Packet(nedt(service_rate))
        GEL.insert(next_arrival_time, 1)  # create new arrival event and insert it into the event list
        # process the arrival event
        if length == 0:
            GEL.insert(time + new_packet.service_time, 2)
            length += 1
            busy = True
            get_busy_time = time
        else:
            if length - 1 < int(buffer_size):
                buffer.insert(new_packet)
                length += 1
            else:
                packets_dropped += 1
    else:  # departure
        time = event.time
        length -= 1
        if length > 0:
            GEL.insert(time + buffer.queue[0].service_time, 2)
            buffer.remove()
        else:
            busy = False
            busy_time += (time - get_busy_time)

if busy:
    busy_time += (time - get_busy_time)

# 3. output statistics
# GEL.print_list()
print("---------- Experiment result ----------")
print("Total time : " + str(time))
print("Utilization : " + str(busy_time / time))
print("Mean queue length : " + str(queue_length_areas / time))
print("Lost packets : " + str(packets_dropped))
print("---------- End of the result ----------")


