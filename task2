# Taking the path of the image to encrypt
path = r"C:\Users\Bhoomika T\OneDrive\Pictures\tcs.png"

# Taking the encryption key as input
key = int(input('Enter the key for encryption of the image: '))

# Print the path of image file and the key used for encryption
print('The path of the file:', path)
print('Key for encryption:', key)

# Open the file for reading in binary mode
with open(path, 'rb') as fin:
    image = fin.read()

# Convert the image into a bytearray to perform encryption easily on numeric data
image = bytearray(image)

# Performing the XOR operation on each value of the bytearray
for index, values in enumerate(image):
    image[index] = values ^ key

# Open the file for writing in binary mode and write the encrypted data back to the image
with open(path, 'wb') as fout:
    fout.write(image)

print('Encryption done...')

