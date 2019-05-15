import numpy as np
from PIL import Image
#############################################
input_file = input('Target file = ')
#############################################
img = Image.open(input_file)
img_rgb = img.convert('RGB')
width,height = img.size
new_width = int(width/2)
new_height = int(height/2)
#img_rgb.thumbnail((new_width, new_height), Image.ANTIALIAS)
#img_rgb.save(input('Name->'))
#############################################
img_matrix = np.asarray(img_rgb, dtype=np.uint8)
#############################################
img_matrix_tmp = np.zeros((new_height,new_width,3), dtype=np.uint8)
for i in range(0,new_height):
    for j in range(0,new_width):
        img_matrix_tmp[[i],[j]] = img_matrix[[2*i],[2*j]]
        
Image.fromarray(img_matrix_tmp).save(input('name->'))
