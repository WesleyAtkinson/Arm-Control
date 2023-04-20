import cv2
import mediapipe as mp
import serial
#Importing Mediapipe AI, Python serial port commands and CV2 for camera capture
ser = serial.Serial(port = 'COM8', baudrate = 9600)
#Opening serial port(you may need to change this depending on your system)
handsAI = mp.solutions.hands
hands = handsAI.Hands()
#identifies if there are hands on the screen
HandsOutline = mp.solutions.drawing_utils
#Creates the hands outline using mediapipe drawing tool
cap = cv2.VideoCapture(0)
#Captures Video using cv2 built in function
fingertips = [8, 12, 16, 20]
#Identifying and assigning all the figer tips into one varible
message = 0
#Message Varible for serial port
while True:
    ret, img = cap.read()   
    #Starting the capture and reading it while storing it to a varible
    img = cv2.flip(img, 1)
    #Flip the image so it is easier to use
    h, w, c = img.shape
    #Stores varibles of the window that this open 
    
    results = hands.process(img)
    #Storing and processing the hands that the AI has picked up
    if results.multi_hand_landmarks:
        #If there are hands on screen
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            #Storing all points on the hand it can identify
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)          
            for tip in fingertips:
                cx, cy = int(lm.x*w), int(lm.y*h)
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
            #Where is the hand on screen using x and y that was stored

              

            

            
            print(f"Hand {id+1}: X={cx}, Y={cy}")
            x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
            print(x, y)
            #printing the hand x and y into terminal

            
            if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and y < 270 and y > 100 and x > 200 and x < 400:
                #Comparing each finger to the location to determine what shape the hand is in
                message = "O"
                #Writing the letter O to the serial port for the ardunio
                ser.write(message.encode('utf-8'))
                 #Writes the letter to the serial port
                cv2.putText(img, "Open", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                #Writes the action on screen that you are doing
                print("Open")
                #Writes the action into the terminal
            if lm_list[3].x < lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and y < 270 and y > 100 and x > 200 and x < 400:
                #Comparing each finger to the location to determine what shape the hand is in
                message = "C"
                #Writing the letter C to the serial port for the ardunio
                ser.write(message.encode('utf-8'))
                  #Writes the letter to the serial port stored as message
                cv2.putText(img, "Close", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Close")
            if  y < 150 and lm_list[8].y > lm_list[4].y:
                #Comparing each finger to the location to determine what shape the hand is in and where the hand is depending on where the screen is
                message = "U"
                ser.write(message.encode('utf-8'))
                cv2.putText(img, "Up", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Up")
            if  y < 150 and lm_list[8].y < lm_list[4].y:
                #Comparing each finger to the location to determine what shape the hand is in and where the hand is depending on where the screen is
                message = "B"
                ser.write(message.encode('utf-8'))
                #Stores the letter to message and writes the letter to the serial port
                cv2.putText(img, "Left Motor Up", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Left Motor Up")
            if  y > 270 and lm_list[8].y > lm_list[4].y:
                #Comparing each finger to the location to determine what shape the hand is in and where the hand is depending on where the screen is
                message = "D"
                ser.write(message.encode('utf-8'))
                #Stores the letter to message and writes the letter to the serial port
                cv2.putText(img, "Down", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Down")
            if  y > 270 and lm_list[8].y < lm_list[4].y:
                #Comparing each finger to the location to determine what shape the hand is in and where the hand is depending on where the screen is
                message = "F"
                ser.write(message.encode('utf-8'))
                cv2.putText(img, "Left Motor Down", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Left Motor Down")
            if  x > 400:
                message = "R"
                ser.write(message.encode('utf-8'))
                #Stores the letter to message and writes the letter to the serial port
                cv2.putText(img, "Right", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Right")
            if x < 200:
                message = "L"
                ser.write(message.encode('utf-8'))
                cv2.putText(img, "Left", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                 #Writes the action on screen that you are doing
                print("Left")
            else:
                message = "0"
                ser.write(message.encode('utf-8'))
            #Serial port message = 0
            HandsOutline.draw_landmarks(img, hand_landmark,
                                    handsAI.HAND_CONNECTIONS,
                                    HandsOutline.DrawingSpec((0, 255, 0), 6, 3),
                                    HandsOutline.DrawingSpec((0, 255, 0), 4, 2)
                                   )
            #Drawing the hand mark on screen so the user can see
    cv2.imshow("Hand Sign Detection", img)
    cv2.waitKey(1)
