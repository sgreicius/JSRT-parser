import numpy as np
from os import listdir
from os.path import isfile, join

"""
obj_name - object names

lung - 'entire lung'
right lung fixed
right lung
left lung fixed
left lung
heart fixed
heart
right clavicle fixed
right clavicle
left clavicle fixed
left clavicle
""" 

def get_paths(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def get_pft_coordinates(file_name, obj_name):
    ret = []
        
    if not os.path.isfile(file_name):
        return ret
    
    with open(file_name) as openfileobject:
        t = 0
        file = []
        s = []
        ss = []
        for i, line in enumerate(openfileobject, start=1):
            file.append(line)
            br1 = line.find("{")
            br2 = line.find("}")

            if line.find(";") == -1:
                if br1 == 0:
                    s.append(i)
                elif br2 == 0:
                    s.append(i)

                if len(s) == 2:
                    ss.append(s)
                    s = []

        for i, line in enumerate(ss, start=1):
            slive = file[line[0]:line[1]]
            if obj_name + ']' in slive[0]:                
                for m, linem in enumerate(slive, start=1):
                    
                    if linem.find("{") != -1:
                        t = linem.replace(",", "", 1)
                        tt1 = re.findall(r"[-+]?\d*\.\d+|\d+", t)
                        tt1[0] = float(tt1[0])
                        tt1[1] = float(tt1[1])
                        
                        if len(tt1) > 0:
                            ret.append((tt1[0], tt1[1]))
    
    return ret

def print_pft_coordinates(path_to_gt, paths):
    print("=== START ===")
    
    for file_name in paths:  
        
        pfs_file_name = path_to_gt + file_name

        if not os.path.isfile(pfs_file_name):
            print("File doesn't exist: %s" % pfs_file_name)
        else:
            print("File: %s" % file_name)            
            print(get_pft_coordinates(pfs_file_name, 'lung') )            

        print()

    print("=== END  ===")
        
path_to_ground_truth = "[PATH TO GROUND TRUTH]\\scratch\\fold1\\points\\"
paths = get_paths(path_to_ground_truth)

print_pft_coordinates(path_to_ground_truth, paths)