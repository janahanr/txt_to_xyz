import math

coord= open("data.xyz", "w") #this is the xyz file to hold the data
data= open("dataset.txt", "r")

xCtr = 0.2 * 20 #20 bc we have 20 measurements 
xVal = 0 #keep track of x value

raddiff= 360/512 * (math.pi/180)

for line in data:
    meas = line.split("\t")
    print(meas)
    rad= raddiff * int(meas[0])
    i=1
    while(xVal <= xCtr):
        dist = int(meas[i])/1000
        y= dist * math.cos(rad)
        z= dist * math.sin(rad)
        coord.write(str(-z) + " " + str(-y) + " " + str(xVal) + '\n')
        xVal = xVal + 0.2
        i+=1
    xVal=0

coord.close()
data.close()


