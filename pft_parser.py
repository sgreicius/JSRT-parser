from os import listdir
from os.path import isfile, join
import os.path
import re
import timeit

class Pft_Object:
    def __init__(self):
        self.label = None
        self.lineDisplay = None
        self.lineMode = None
        self.pointColor = None
        self.pointDisplay = None
        self.pointMode = None
        self.pointSize = None
        self.pointWidth = None
        self.points = []
            
    def __repr__(self):
        attrs = vars(self)
        return '<' + ','.join("%s: %s" % item for item in attrs.items()) + '>\n'
        
    def add_point(self, point):
        self.points.append(point)

def get_paths(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def get_pft_parts(file_name, part_search = None):
    parsed_objects = []
        
    if not os.path.isfile(file_name):
        return []
    
    with open(file_name) as openfileobject:
    
        obj = Pft_Object()
        for line in openfileobject:
            #skipping ";" and "empty" lines
            if line.find(";") == -1 and len(line) > 1:

                if '[' in line:
                    # parsing object properties
                    value_start = line.find("=")+1
                    value_end = line.find("]")
                    line_value = line[value_start:value_end]
                
                    if line.find("Label") != -1:
                        obj.label = line_value
                    if line.find("LineDisplay") != -1:
                        obj.lineDisplay = line_value
                    if line.find("LineMode") != -1:
                        obj.lineMode = line_value
                    if line.find("PointColor") != -1:
                        obj.pointColor = line_value
                    if line.find("PointDisplay") != -1:
                        obj.pointDisplay = line_value
                    if line.find("PointMode") != -1:
                        obj.pointMode = line_value
                    if line.find("PointSize") != -1:
                        obj.pointSize = line_value
                    if line.find("PointWidth") != -1:
                        obj.pointWidth = line_value
                
                # Part points parsing
                if line.find("{") != -1 and len(line) > 2:
                    #parsing object points
                    coord_line = line.replace(",", "", 1)
                    point_coordinate = re.findall(r"[-+]?\d*\.\d+|\d+", coord_line)
                    point_coordinate[0] = float(point_coordinate[0])
                    point_coordinate[1] = float(point_coordinate[1])
                    
                    if len(point_coordinate) > 0:
                        obj.add_point((point_coordinate[0], point_coordinate[1]))

                if line.find("}") == 0:
                    if (part_search is None) or (part_search in obj.label):
                        parsed_objects.append(obj)
                    
                    #resetting object
                    obj = Pft_Object()
                    
    return parsed_objects

def print_pft_objects(path_to_gt, paths, part_to_search = None):
    print("=== START ===")
    
    for file_name in paths:
        
        pfs_file_name = path_to_gt + file_name

        if not os.path.isfile(pfs_file_name):
            print("File doesn't exist: %s" % pfs_file_name)
        else:
            print("File: %s" % file_name)
            print(get_pft_parts(pfs_file_name, part_to_search))
            print( )

        print()

    print("=== END  ===")

###
# EXAMPLE
###

def parse():
    path_to_ground_truth = "[PATH TO GROUND TRUTH]\\scratch\\fold1\\points\\"
    
    part_to_search = None
    paths = get_paths(path_to_ground_truth)
    print_pft_objects(path_to_ground_truth, paths, part_to_search)

execution_time = timeit.timeit(parse, number=1)
print(execution_time)
