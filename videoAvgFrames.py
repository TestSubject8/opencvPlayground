from cv2 import *
import math
import sys
from tkinter import *
from colour import *

try:
    log = sys.argv[2]
except:
    log = False

src = VideoCapture(sys.argv[1])
nFrames = int(src.get(CAP_PROP_FRAME_COUNT))
srcW = int(src.get(CAP_PROP_FRAME_WIDTH))
srcH = int(src.get(CAP_PROP_FRAME_HEIGHT))
print('Frames: '+str(nFrames))
print('Resolution: '+str(srcW)+'x'+str(srcH))

#nFrames = 100
#srcW = 100
#srcH = 100

fuzz = 100

nF = math.floor(nFrames/100)*fuzz
nH = math.floor(srcH/100)*fuzz
nW = math.floor(srcW/100)*fuzz

main = Tk()
mainHeight = 50
disp = Canvas(main, width=nF, height=mainHeight)
disp.pack()

#result = [0,0,0]
#for h in range(nH):
#    result.append([])
#    for w in range(nW):
#        result[h].append([])
#        for i in range(3):
#            result[h][w].append(0)
#print("created resultset")


print(str(nF)+':'+str(nH)+':'+str(nW))

def bucket(frame, simple=True):
    global nF, nW, nH
    result = [0,0,0]
    buckets = [[0,0,0]]
    try:
        for h in range(0,nH):
            for w in range(0,nW):
                insert = True
                for value in buckets:
                    distance = 0
                    for i in range(3):
                        distance += abs(value[i]-frame[h][w][i])
                    # distance 400 has noticable colours - 600 gives just two - 450 is the best
                    if distance <= 200:
                        insert = False
#                    else:
#                        insert = True
                if insert:
                    pixel = [0,0,0]
                    for i in range(3):
                        pixel[i] = frame[h][w][i]
                    buckets.append(pixel)
            if log:
                print(len(buckets))
        if simple:
            for pixel in buckets:
                for i in range(3):
                    result[i] += pixel[i]
                for i in range(3):
                    result[i] /= (len(buckets) * 255)
            return result
        else:
            return buckets
    except Exception as e:
        if (log):
            print("Bucket"+str(e))

def simpleAvg(frame):
    global nF, nW, nH
    result = [0,0,0]
    try:
        for h in range(0,nH):
            for w in range(0,nW):
#        if (log):
#            print("data: "+str(h)+"x"+str(w)+": "+str(frame[h][w]))
                for i in range(3):
                    result[i] += (frame[h][w][i]) 
        for i in range(3):
            result[i] = result[i] /  ( nH * nW * 255)
    except Exception as e:
        print(str(f)+','+str(w)+','+str(h))
        print(frame[h][w])
        print("simpleAvg: "+str(e))
    return result
    
def simpleDraw(src):
    global nF, nW, nH
    for f in range(nF):
        try:
            src.set(CAP_PROP_POS_FRAMES, f-1)
            ret, frame = src.read()
            #res = simpleAvg(frame)
            res = bucket(frame)
#            if(log):
#                print("Got value %1.2f - %1.2f - %1.2f for frame %4d" % (res[0], res[1], res[2], f))
            disp.create_rectangle(f,0,f,mainHeight,outline='',fill=Color(rgb=tuple(res)))
        except Exception as e:
            print(res)
            print("Frames: "+str(e))
    
    
    print("done")


def bucketDraw(src):
    global nF, nW, nH
    for f in range(nF):
        try:
            if not f%fuzz :
                print("Frame %d of %d\r" %(f, nF), end ='')
            src.set(CAP_PROP_POS_FRAMES, f-1)
            ret, frame = src.read()
            #res = simpleAvg(frame)
            buckets = bucket(frame,False)
            nB = len(buckets)
            for i in range(nB):
                if(log):
                    print("Got value " + str(buckets[i]) + " for " + str(f))
                for j in range(3):
                    buckets[i][j] /= float(255.0)
                start = (mainHeight / nB) * i
                end = (mainHeight / nB) * (1 + i)
                if(log):
                    print("Drawing " + str(buckets[i]) + " from " + str(start) + " to " + str(end))
                disp.create_rectangle(f,start,f,end,outline='',fill=Color(rgb=tuple(buckets[i])))
        except Exception as e:
            print(buckets)
            print("Bucket Draw: "+str(e))
    
    
    print("done")


bucketDraw(src)

#   val = 
#   disp.create_line(0,x,500,x, fill=val)
#    print(frame[0][0])
#    break


main.bind("<Escape>",exit)
main.mainloop()


