//
//  Event.h
//  network_simulation
//
//  Created by Lei Zuo on 2019/4/27.
//  Copyright © 2019 ECS 152A. All rights reserved.
//


#ifndef Event_h
#define Event_h

class Event {
    int event_time;
    int event_type;  // 1 is arrival event and 2 is departure event
    Event * next;
    Event * prev;
    
public:
    Event(int event_time, int event_type, Event * next, Event * prev);
};

#endif /* Event_h */
