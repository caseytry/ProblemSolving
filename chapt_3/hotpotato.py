from Queue import Queue


def hot_potato(name_list, num):
    #create queue
    sim_queue = Queue()
    #add names from the input to the queue
    for name in name_list:
        sim_queue.enqueue(name)
    
    #while the size of the queue is greater than 1
    while sim_queue.size() > 1:
        #iterating over a range that is the number provided as input
        for i in range(num):
            #dequeue a name, but then enqueue it right away
            sim_queue.enqueue(sim_queue.dequeue())
        
        #remove whomever is at the front of the queue after so many iterations
        sim_queue.dequeue()
    #return name that is remaining
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))