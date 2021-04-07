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
