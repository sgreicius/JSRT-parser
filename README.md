# JSRT parser
This repository contains the code for parsing lung ground truth files from https://www.isi.uu.nl/Research/Databases/SCR/.

## Usage
* ```path_to_ground_truth``` - path to files in '...\\scratch\\fold1\\points\\' or '...\\scratch\\fold2\\points\\' 
* function ```get_pft_objects``` 
    - file_names - path to '...\\scratch\\fold1\\points\\JPCLNXXX.pfs' or '...\\scratch\\fold1\\points\\JPCNNXXX.pfs' file. 
        - XXX - numbers [001-999]
    - obj_name - object name

### Searchable object names ("part_to_search"):
* ```lung``` - entire lung
* ```right lung fixed```
* ```right lung```
* ```left lung fixed```
* ```left lung```
* ```heart fixed```
* ```heart```
* ```clavicle``` - entire clavicle
* ```right clavicle fixed```
* ```right clavicle```
* ```left clavicle fixed```
* ```left clavicle```

***Note***: JSRT dataset url: http://db.jsrt.or.jp/eng.php.
