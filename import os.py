import os
dir = "newfiles"
parent_dir = "D:\python"
path = os.path.join(parent_dir, dir)
os.makedirs(path)
for i in range(10):
    dir1 = path+"\\newfile" + str(i+1) + ".txt"
    f = open(dir1, "w")
    f.write("data"* 1000*i)
    f.close()   