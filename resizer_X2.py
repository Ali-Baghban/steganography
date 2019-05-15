import numpy as np
from PIL import Image
#############################################
input_file = input('Target file = ')
#############################################
img = Image.open(input_file)
img_rgb = img.convert('RGB')
width,height = img.size
new_width = int(width*2)
new_height = int(height*2)
#img_rgb.thumbnail((new_width, new_height), Image.ANTIALIAS)
#img_rgb.save(input('Name->'))
#############################################
img_matrix = np.asarray(img_rgb, dtype=np.uint8)
#############################################
img_matrix_tmp = np.zeros((new_height,new_width,3), dtype=np.uint8)
##### 2i , 2j
for i in range(0,height):
    for j in range(0,width):
        img_matrix_tmp[[i*2],[j*2]] = img_matrix[[i],[j]]
#####################################################
##### 2i , 2j+1
for i in range(0,new_height):
    for j in range(0,new_width):
        try:
            tmp1_matrix = np.array(img_matrix_tmp[[2*i],[2*j]], dtype=np.uint16)
            tmp2_matrix = np.array(img_matrix_tmp[[2*i],[2*j+2]], dtype=np.uint16)
            tmp = (tmp1_matrix + tmp2_matrix) /2
            img_matrix_tmp[[2*i],[2*j+1]] = tmp
        except:
            pass
#####################################################
##### 2i+1 , 2j
for i in range(0,new_height):
    for j in range(0,new_width):
        try:
            tmp1_matrix = np.array(img_matrix_tmp[[2*i],[2*j]], dtype=np.uint16)
            tmp2_matrix = np.array(img_matrix_tmp[[2*i+2],[2*j]], dtype=np.uint16)
            tmp = (tmp1_matrix + tmp2_matrix) /2
            img_matrix_tmp[[2*i+1],[2*j]] = tmp
        except:
            pass
#####################################################
##### 2i+1,2j+1
for i in range(0,new_height):
    for j in range(0,new_width):
        try:
            tmp1_matrix = np.array(img_matrix_tmp[[2*i+1],[2*j]], dtype=np.uint16)
            tmp2_matrix = np.array(img_matrix_tmp[[2*i+1],[2*j+2]], dtype=np.uint16)
            tmp = (tmp1_matrix + tmp2_matrix) /2
            img_matrix_tmp[[2*i+1],[2*j+1]] = tmp
        except:
            pass
Image.fromarray(img_matrix_tmp).save(input('name->'))

