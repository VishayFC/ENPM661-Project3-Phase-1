import numpy as np
import cv2

out = cv2.VideoWriter('Dijsktra_output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 60, (400,300))
#defining the queue class to use as a data structure
class queue():
    def __init__(self):
        self.pending = list()

    def add(self, child, ind):
        self.pending.insert(ind, child)

    def remove(self):
        if self.pending:
            return self.pending.pop()
        return None

    def peek(self):
        if self.pending:
            return self.pending[-1]

    def size1(self):
        return len(self.pending)

    def isempty(self):
        if self.pending == []:
            return True
        return False

#created node class in order to save current node and it's parent
class node():
    def __init__(self, current, parent): #, cost):
        self.current = current
        self.parent = parent

#defining obstacles as well as the boundaries of the map
#st[0] = y coordinate in cartesian space     st[1] = x coordinate in cartesian space
def obstacles(st):
    radius = 10
    clearance = 5
    cl = radius + clearance
    s1 = 0.7
    s2 = -1.42814
    x1 = np.arctan(s1)
    x2 = np.arctan(s2)
    d1 = np.cos(np.pi - x1)
    d2 = np.cos(np.pi - x2)
    a = -(cl / d1)
    b = -(cl / d2)
    if (((st[1]) - (90+1)) ** 2) + ((st[0] - (70+1)) ** 2) <= ((35+cl)**2):
        canvas[canvas_size[0]-1-st[0]][st[1]][0] = 255
        #print("coordinate is in circle")
        return None

    elif (((st[1] - (246+1)) / (60+cl)) ** 2) + (((st[0] - (145+1)) / (30+cl)) ** 2) <= 1:
        canvas[canvas_size[0]-1-st[0]][st[1]][0] = 255
        #print("coordinate is in ellipse")
        return None
    
    elif (st[0] <= ((280+1) + cl) and st[1]>=((200+1)-cl) and st[0]>=((230+1)-cl) and st[1]<=((230+1)+cl)) and not (st[0]<=((270+1)-cl) and st[1]>=((210+1)+cl) and st[0]>=((240+1)+cl) and st[1]<=((230+1)+cl)):
        canvas[canvas_size[0]-1-st[0]][st[1]][0] = 255
        #print("coordinate is in C shape")
        return None

    elif (-0.7*st[1]+1*st[0])>=(73.4-a) and (st[0]+1.42814*st[1])>=(172.55-b) and (-0.7*st[1]+1*st[0])<=(99.81+a) and (st[0]+1.42814*st[1])<=(429.07+b):
        canvas[canvas_size[0]-1-st[0]][st[1]][0] = 255
        #print("coordinate is in rectangle")
        return None

    elif (st[1] >= ((canvas_size[1]-1) - cl)) or (st[1] <= cl+1):
        canvas[canvas_size[0]-1-st[0]][st[1]][0] = 255
        #print("coordinate is out of the map boundary")
        return None

    elif (st[0] <= cl+1) or (st[0] >= ((canvas_size[0] -1) - cl)):
        canvas[canvas_size[0]-1-st[0]][st[1]][0] = 255
        #print("coordinate is out of the map boundary")
        return None
        
    else :
        return st


#removes from the queue
def removing_from_queue():
    
    check = queue1.remove()
    cs = duplicate_costqueue.pop()
    return check, cs