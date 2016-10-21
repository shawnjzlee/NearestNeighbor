import time
import sys
import math

def weakSort(data):
    
    timeStart = time.time();
    
    print "=====================================================================TimeStart(Select): " + str(timeStart)
    
    distance = 100000.0
    
    for i in range(0,len(data)-1):
        
        num1 = float(data[i][0])
        num2 = float(data[i][1])
        
        for j in range(i+1,len(data)-1):
            
            num3 = float(data[j][0])
            num4 = float(data[j][1])
            
            if ((num3 - num1)**2 + (num4 - num2)**2) ** .5 < distance:
                distance = ((num3 - num1)**2 + (num4 - num2)**2) ** .5
    
    
    timeEnd = time.time() - timeStart
    
    print "TimeEnd: " + str(timeEnd)
    
    minute = int(timeEnd / 60)
    sec = int(timeEnd % 60)
    ms = (timeEnd * 1000) % 1000
    
    print str(minute) +" m " +str(sec) +" s " + str(ms) + " ms"
    
    return distance

def divideSort(data):
    
    distance = 10000.0
    dataR = []
    dataL = []
    
    distanceL = 10000.0
    distanceR = 10000.0
    
    avgX = 0.0
    
    if len(data) > 0:
        for i in range(0,len(data)-1):
            
            avgX = avgX + float(data[i][0])
        
        avgX = avgX / len(data)
    
    if len(data) > 4:
        for i in range(0,len(data)-1):
            if float(data[i][0]) >= avgX:
                dataR.append(data[i])
            else:
                dataL.append(data[i])
        
        distanceL = divideSort(dataL)  
        distanceR = divideSort(dataR)
        
        if distanceL < distanceR:
            distance = distanceL
        else:
            distance = distanceR
        
        if distanceR is None:
            distance = distanceL
        if distanceL is None:
            distance = distanceR
        
        for i in range(0,len(data)-1):
        
            if float(data[i][0]) - avgX < (distance/2.0):
                num1 = float(data[i][0])
                num2 = float(data[i][1])
        
                for j in range(i+1,len(data)-1):
            
                    if float(data[j][0]) - avgX < (distance/2.0):
                        num3 = float(data[j][0])
                        num4 = float(data[j][1])
            
                        if ((num3 - num1)**2 + (num4 - num2)**2) ** .5 < distance:
                            distance = ((num3 - num1)**2 + (num4 - num2)**2) ** .5
                            
        return distance
            
        
        
    else:
        for i in range(0,len(data)-1):
        
            num1 = float(data[i][0])
            num2 = float(data[i][1])
        
            for j in range(i+1,len(data)-1):
            
                num3 = float(data[j][0])
                num4 = float(data[j][1])
            
                if ((num3 - num1)**2 + (num4 - num2)**2) ** .5 < distance:
                    distance = ((num3 - num1)**2 + (num4 - num2)**2) ** .5
                    
        return distance
            
    
    
    
def main():
    fileName = sys.argv[1]
    fileIn = open(fileName,'r')
    
    data = []
    
    for word in fileIn.readlines():
        data.append(word.split())
    
    distance = weakSort(data)
    
    timeStart = time.time();
    
    print "=====================================================================TimeStart(Divide): " + str(timeStart)
    
    distance1 = divideSort(data)
    
    timeEnd = time.time() - timeStart
    
    print "TimeEnd: " + str(timeEnd)
    
    minute = int(timeEnd / 60)
    sec = int(timeEnd % 60)
    ms = (timeEnd * 1000) % 1000
    
    print str(minute) +" m " +str(sec) +" s " + str(ms) + " ms"
    
    length = len(fileName)
    length = length - 4
    
    fileName = fileName[:length]
    fileName += "_distance.txt"
    
    fileOut = open(fileName,'w')
    
    if distance == distance1:
        fileOut.write(str(distance))
        print "Successful write!"
    else:
        print "ERROR IN DISTANCE"
        print "Distance in Brute: " + str(distance)
        print "Distance in Recur: " + str(distance1)
        
        
    return



main()