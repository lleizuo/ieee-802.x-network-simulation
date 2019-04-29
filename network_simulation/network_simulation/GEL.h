//
//  GEL.h
//  network_simulation
//
//  Created by Lei Zuo on 2019/4/28.
//  Copyright © 2019 ECS 152A. All rights reserved.
//

#ifndef GEL_h
#define GEL_h

#include "Event.h"

class GEL {
    Event * head;
    
public:
    void insert(int event_time, Event * new_event);
};


#endif /* GEL_h */
