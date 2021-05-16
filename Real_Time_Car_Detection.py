import cv2
#Importing the image
img_file = "images\More-cars-and-vans.png"
video = cv2.VideoCapture("images\Dramatic Dashcam Footage Shows Plane Crash in Mukilteo Washington.mp4")

#Importing classifier file
car_classifier_file = "images\cars1.xml"

#classify
car_tracker = cv2.CascadeClassifier(car_classifier_file)

#Looping thought the video
while True:
    #Reading the current frame
    (read_successfully, frame) = video.read()

    #Safe Codding
    if read_successfully:
        # convert to black and white
        black_n_white = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    else:
        break

    # detect the cars in the image
    car = car_tracker.detectMultiScale(black_n_white)

    # drawing rectangles
    for (x, y, w, h) in car:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display image
    cv2.imshow("Car App", frame)
    cv2.waitKey(1)

print("Done")