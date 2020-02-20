from cv2 import *
import math
import sys
from tkinter import *
from colour import *

src = VideoCapture(sys.argv[1])
nFrames = int(src.get(CAP_PROP_FRAME_COUNT))
srcW = int(src.get(CAP_PROP_FRAME_WIDTH))
srcH = int(src.get(CAP_PROP_FRAME_HEIGHT))
print('Frames: '+str(nFrames))
print('Resolution: '+str(srcW)+'x'+str(srcH))

#nFrames = 100
#srcW = 100
#srcH = 100

nF = math.floor(nFrames/100)*10
nH = math.floor(srcH/100)*10
nW = math.floor(srcW/100)*10

main = Tk()
disp = Canvas(main, width=nW*10, height=nH*10)
disp.pack()

result = []
for h in range(nH):
    result.append([])
    for w in range(nW):
        result[h].append([])
        for i in range(3):
            result[h][w].append(0)
print("created resultset")


print(str(nF)+':'+str(nH)+':'+str(nW))

ret = True
#while(ret):
try:
    for f in range(0,nF,10):
        src.set(CAP_PROP_POS_FRAMES,f-1)
        ret, frame = src.read()
        for h in range(0,nH):
            for w in range(0,nW):
#                print("data: "+str(h)+"x"+str(w)+": "+str(frame[h][w]))
                for i in range(3):
                    result[h][w][i] += (frame[h][w][i] / 25) 
except Exception as e:
    print(str(f)+','+str(w)+','+str(h))
    print(frame[h][w])
    print(e)
else:
    print("created average")


for h in range(nH):
    for w in range(nW):
        for i in range(3):
            result[h][w][i] = result[h][w][i] / nFrames 
        try:
            disp.create_rectangle(w*10,h*10,w*10+10,h*10+10,outline='',fill=Color(rgb=tuple(result[h][w])))
        except:
            print(result[h][w])
print("done")



#   val = 
#   disp.create_line(0,x,500,x, fill=val)
#    print(frame[0][0])
#    break


main.bind("<Escape>",exit)
main.mainloop()


