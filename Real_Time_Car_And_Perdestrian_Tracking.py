import cv2
#Importing the image
img_file = "images\More-cars-and-vans.png"
video = cv2.VideoCapture("images\London Cycling, Near Misses No Filter, Apr to Jun 19.mp4")

#Importing classifier file
car_classifier_file = "images\cars1.xml"

#classify
car_tracker = cv2.CascadeClassifier(car_classifier_file)

#pedestraion
pedestiran_classifer_file = "images\haarcascade_fullbody.xml"

#classify file
pedestiran_tracker = cv2.CascadeClassifier(pedestiran_classifer_file)

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

    # detect the cars and pedestrians
    car = car_tracker.detectMultiScale(black_n_white)
    pedestrians = pedestiran_tracker.detectMultiScale(black_n_white)

    # drawing rectangles
    for (x, y, w, h) in car:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 255), 2)

    # Display image
    cv2.imshow("Car and Perdestians tracking apps", frame)
    key = cv2.waitKey(1)

    #Q for qiut
    if key == 81 or key == 113:
        break

video.release()