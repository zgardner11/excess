import cv2

# import destination image
img = cv2.imread("C:\Prints\Prints\Final\Lightning.tif")

color = [255, 255, 255] #white

# border widths in pixels
top, bottom = [1500]*2
left, right = [0]*2

#add border
img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

#write to destination path
check = cv2.imwrite('C:\Prints\Prints\Final\Calendar20.tif', img_with_border)

#check for successful write
print("Image written to file-system : ", check)