path = r"C:\Users\dieko\Downloads\Colorful Abstract Online Shop Free Logo.png"


key = int(input("Enter kry for encryption of image: "))

print("The path file is : ", path)
print("Key for encryption is : ", key)

fin = open(path, "rb")

image = fin.read()
fin.close()

image = bytearray(image)

for index, values in enumerate(image):
    image[index] = values ^ key

fin = open(path, "wb")

fin.write(image)
fin.close()
print("Encrypted")
