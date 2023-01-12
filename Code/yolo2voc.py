#Create the ground truth files(VOC-xyrb)
import os
#設定來源位置與目標位置
srcfile = "C:/Users/Axuy312/Desktop/vsat_hw2/val_labels"
dstfile = "C:/Users/Axuy312/Desktop/vsat_hw2/val_labels(VOC_xyrb)"
for file in os.listdir(srcfile):
    rf = open(os.path.join(srcfile, file), 'r')
    wf = open(os.path.join(dstfile, file), 'w')
    for line in rf.readlines():
        item = line.split(' ')
        c = int(item[0])
        x = int((float(item[1]) - float(item[3])/2.0)*1920.0)
        y = int((float(item[2]) - float(item[4])/2.0)*1080.0)
        r = int((float(item[1]) + float(item[3])/2.0)*1920.0)
        b = int((float(item[2]) + float(item[4])/2.0)*1080.0)
        wf.write(f"car {x} {y} {r} {b}\n")
    rf.close()
    wf.close()
    
    