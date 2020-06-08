# JSRT parser
This repository contains the code for parsing lung ground truth files from https://www.isi.uu.nl/Research/Databases/SCR/.

## Usage
* '''path_to_ground_truth''' - set path to '...\\scratch\\fold1\\points\\'

* '''get_pft_coordinates'''
** file_names - paths from '...\\scratch\\fold1\\points\\' containing '.pfs' files 
** obj_name - object name

## Posible 'obj_name' names:
* '''lung''' - 'entire lung'
* '''right lung fixed'''
* '''right lung'''
* '''left lung fixed'''
* '''left lung'''
* '''heart fixed'''
* '''heart'''
* '''right clavicle fixed'''
* '''right clavicle'''
* '''left clavicle fixed'''
* '''left clavicle'''

***Note***: JSRT dataset url: http://db.jsrt.or.jp/eng.php.
