__author__ = 'yuki'
#coding UTF-8

import numpy
from MLayer import *

class Filter(object):
    def __init__(self):
        pass

    #Input:input layer
    #Output:output layer
    #sCount:number of scale in Input
    #Step:width to move the filter
    def ComputeS1Layer(self, Input, Output, sCount):
        print "\n S1" 
        for s in range(sCount):
            print "Computing scale", s, "..."
            inputimg = Input.get_array(s)
            outputimg = Output.get_array(s)
            size = Input.get_size(s)
            for o in range(self.oCount):
                for x in range(0, size - self.xyCount + 1):
                    for y in range(0, size - self.xyCount + 1):
                        outputimg[x, y, o] = self.ComputeUnit(inputimg[x:x + self.xyCount, y:y + self.xyCount], o)

    def ComputeC1Layer(self, Input, Output, sCount, Step):
        print "\n C1" 
        for s in range(sCount):
            print "Computing scale", s, "..."
            i_img1 = Input.get_array(s)
            i_img2 = Input.get_array(s + 1)
            outputimg = Output.get_array(s)
            size = Input.get_size(s)
            space = 1.0 * Input.get_xySpace(s) / Input.get_xySpace(s + 1)
            
            for o in range(self.oCount):
                o_x = 0
                for x in range(0, size - self.xyCount + 1, Step):
                    x2 = x + self.xyCount
                    u_x1 = int(x * space)
                    u_x2 = int((x + self.xyCount) * space)
                    o_y = 0
                    for y in range(0, size - self.xyCount + 1, Step):
                        y2 = y + self.xyCount
                        u_y1 = int(y * space)
                        u_y2 = int((y + self.xyCount) * space)
                        outputimg[o_x, o_y, o] = self.ComputeUnit(i_img1[x:x2, y:y2, o], i_img2[u_x1:u_x2, u_y1:u_y2, o])
                        o_y = o_y + 1
                    o_x = o_x + 1
