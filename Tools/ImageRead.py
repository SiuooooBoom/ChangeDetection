from PIL import Image
import cv2

file1 = (r'/home/rtx3080ti/ChangeDetection/Tools/3.png')
img1 =Image.open(file1)
print(img1.size)
print(len(img1.split()))

file2 = (r'/home/rtx3080ti/ChangeDetection/Tools/new/3_0624_0000.png')
img2 =Image.open(file2)
print(img2.size)
print(len(img2.split()))

img3 = cv2.imread('/home/rtx3080ti/ChangeDetection/Tools/1.png',cv2.IMREAD_GRAYSCALE)
size = img3.shape
print(size)