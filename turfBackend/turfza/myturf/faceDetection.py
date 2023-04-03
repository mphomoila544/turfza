import cv2


cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('id.jpg')

scale_percent = 20  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray, 1.1, 4)
count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    count += 1

print(count)

cv2.imshow('img', img)
cv2.waitKey()
