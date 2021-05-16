import cv2
#Importing the image
img_file = "images\More-cars-and-vans.png"

#Importing classifier file
classifier_file = "images\cars1.xml"

#Creating opencv image
img = cv2.imread(img_file)

#classify
car_tracker = cv2.CascadeClassifier(classifier_file)

#convert to black and white
black_n_white = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#detect the cars in the image
car = car_tracker.detectMultiScale(black_n_white)

#drawing rectangles
for (x, y, w, h) in car:
    cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0), 2)

#Display image
cv2.imshow("Car App", img)
cv2.waitKey()
print("Done")
