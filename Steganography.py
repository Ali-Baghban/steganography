import numpy as np
from PIL import Image
#############################################
print("########################################################################")
print("# Steganography Process Engine {v 1.3} Scripted By Ali Baghban S.U.T.| #\n# Follow the project on : https://github.com/Ali-Baghban               #")
print("########################################################################")
print("Import an image for processing (2X Resize)\n---------------------------------")
input_file = input('Target file = ')
print("---------------------------------")
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
#####################################################
#####################################################
# Message Convert to Binary
#########################################################
#def text2binary(msg = ''):
#    return bin(int.from_bytes(msg.encode(), 'big')).strip('0b')
#
#def binary2text(binary = ''):
#   n = np.array(int('0b'+binary, 2))
#   return n.bytes((n.bit_length() + 7) // 8, 'big').decode()
#def string2bin(msg):
#   msg_length = str(len(msg))
#   msg = msg+msg_length
#   secret = list()
#   for char in msg:
#       x = bin(int.from_bytes(char.encode(), 'big')).strip('0b')
#       if char == ' ':
#          x = '0'+x+'00000'
#        else:
#           ln = len(bin(int.from_bytes(char.encode(), 'big')).strip('0b'))
#           if (ln) < 7:
#               for i in range(0,7-ln):
#                   x = x+'0'
#       secret.append(x)
#   string = ''.join(secret)
#   secret = string [::-1]
#   return secret
# ************************
def bigbang(msg):
    msg_length = str(bin(len(msg))).replace('0b','0')
    tmp_size = len(msg_length)
    while  tmp_size <16:
        msg_length = '0'+msg_length
        tmp_size += 1
    secret = ''
    for char in msg:
        x = bin(ord(char)).replace('0b','0')    
        ln = len(x)
        if (ln) < 8:
            for i in range(0,8-ln):
                x = '0'+x
        secret += x
    secret = msg_length+secret
    return secret
# ************************
#########################################################
print("Injection Section :) \n---------------------------------")
msg = input('Your message => ')
print("---------------------------------\n")
secret = bigbang(msg)
secret_list = list()
for m in secret:
    secret_list.append(m)
secret_list.reverse()
print ('Your message bin code = > '+secret+'\n')

print(secret_list)
#########################################################
# Injection
#########################################################
print("---------------------------------\nWaiting for injection \n---------------------------------")
for i in range(0,new_height):
    for j in range(0,new_width):
        try:
            bit = secret_list.pop()
            if i%2 == 0 :
                if img_matrix_tmp[i,2*j+1,0] != 255:
                    if bit == '1' :
                        img_matrix_tmp[i,2*j+1,0] = img_matrix_tmp[i,2*j+1,0]+1
                    else:
                        pass
                else:
                    if bit == '1' :
                        img_matrix_tmp[i,2*j+1,0] = img_matrix_tmp[i,2*j+1,0] - 1
                    else:
                        pass
            else:
                if img_matrix_tmp[i,j,0] != 255:
                    if bit == '1' :
                        img_matrix_tmp[i,j,0] = img_matrix_tmp[i,j,0]+1
                    else:
                        pass
                else:
                    if bit == '1' :
                        img_matrix_tmp[i,j,0] = img_matrix_tmp[i,j,0] - 1
        except:
            pass
print("---------------------------------\n")
#########################################################
#   Steganalysis
def steganalysis(new_height,new_width,img_matrix_tmp):
    bits = ''
    for i in range(0,new_height):
        for j in range(0,new_width):
            if i%2 == 0 :
                try:
                    tmp1_matrix = np.array(img_matrix_tmp[[2*i],[2*j]], dtype=np.uint16)
                    tmp2_matrix = np.array(img_matrix_tmp[[2*i],[2*j+2]], dtype=np.uint16)
                    tmp = (tmp1_matrix + tmp2_matrix) /2
                    red = int(tmp[0,0])
                    if img_matrix_tmp[[2*i],[2*j+1],0] == red:
                        bits += '0'
                    else:
                        bits += '1'
                except:
                    pass
            else:
                try:
                    tmp1_matrix = np.array(img_matrix_tmp[[i],[j]], dtype=np.uint16)
                    tmp2_matrix = np.array(img_matrix_tmp[[i],[j+2]], dtype=np.uint16)
                    tmp = (tmp1_matrix + tmp2_matrix) /2
                    red = int(tmp[0,0])
                    if img_matrix_tmp[[i],[2*j+1],0] == red:
                        bits += '0'
                    else:
                        bits += '1'
                except:
                    pass
    return bits
print("Steganalysis section\n---------------------------------")
secret_long = steganalysis(1,16,img_matrix_tmp)
print(secret_long)
secret_long = int(secret_long.encode(),2)
print(secret_long)
msg_secret = steganalysis(1,secret_long*8+16,img_matrix_tmp)
print(msg_secret)
msg_secret_list = list()
for x in msg_secret:
    msg_secret_list.append(x)
msg_secret_array = np.asarray(msg_secret_list)
print(msg_secret_array)
#--------------------------
msg_secret_list.clear()

msg_bin = ''
x = 16
try:
    for i in range(1,secret_long+1):
        msg_bin = ''
        for j in range(x,x+8):
            msg_bin = msg_bin+msg_secret_array[j]
        x += 8
        msg_secret_list.append(msg_bin)
except:
    pass
print(msg_secret_list)
msg_decoded = ''
for byte in msg_secret_list:
    msg_decoded += chr(int(byte.encode(),2))

print("The hidden message is => "+msg_decoded)
#########################################################
# Export
print("Export Section \n---------------------------------")
Image.fromarray(img_matrix_tmp).save(input('Export the Steg. image as file (Enter file name)-> '))



        
