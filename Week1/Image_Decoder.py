from PIL import Image

#Andreas Vikke
img = Image.open('7fe3c3f6-Stego.png')
width, height = img.size

extracted_bin = [str(img.getpixel((y, x))[2]&1) for x in range(0, height) for y in range(0, width)]
extracted_bytes = ["".join(extracted_bin[i:i+8][::-1]) for i in range(0, len(extracted_bin), 8)]

result = ''
for byte in extracted_bytes:
    if byte != '00000000':
        result += chr(int(byte, 2))
    else:
        break

print ("Secret Message: ", result)

# #Martin Frederiksen
# im = Image.open('7fe3c3f6-Stego.png')
# width, height = im.size

# bytes_array = []
# bit_string = ""
# for x in range(height):
#     for y in range(width):
#         bit_string += bin(im.getpixel((y, x))[2])[-1]

# bytes_array = [bit_string[i:i+8][::-1] for i in range(0, len(bit_string), 8)]

# result = ""
# for byte in bytes_array:
#     if byte == '00000000':
#         break 
#     result += chr(int(byte, 2))

# print(result)
