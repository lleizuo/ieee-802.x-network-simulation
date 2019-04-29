//
//  Event.cpp
//  network_simulation
//
//  Created by Lei Zuo on 2019/4/27.
//  Copyright © 2019 ECS 152A. All rights reserved.
//


#include "Event.h"

Event::Event(int event_time, int event_type, Event * next, Event * prev) {
    this->event_time = event_time;
    this->event_type = event_type;
    this->next = next;
    this->prev = prev;
}

