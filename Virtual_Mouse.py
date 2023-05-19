import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
mpHand = mp.solutions.hands
hands = mpHand.Hands()
screen_width , screen_height = pyautogui.size()
mpDraw = mp.solutions.drawing_utils
pointer_y = 0

while True:
    _success, img = cam.read()
    img = cv2.flip(img, 1)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_RGB)

    if result.multi_hand_landmarks:
        for handLandmarks in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLandmarks, mpHand.HAND_CONNECTIONS)

            for id, lm in enumerate(handLandmarks.landmark):
                frame_height, frame_width, _chennal = img.shape
                x_corrdinate = int(lm.x * frame_width)
                y_corrdinate = int(lm.y * frame_height)

                if id == 8:
                    pointer_x = (screen_width/frame_width) * x_corrdinate
                    pointer_y = (screen_height/frame_height) * y_corrdinate
                    cv2.circle(img, (x_corrdinate, y_corrdinate), 10, (255,0,0), cv2.FILLED)
                    pyautogui.moveTo(pointer_x, pointer_y)

                if id == 12:
                    middle_x = (screen_width/frame_width) * x_corrdinate
                    middle_y = (screen_height/frame_height) * y_corrdinate
                    cv2.circle(img, (x_corrdinate, y_corrdinate), 10, (225,0,0),cv2.FILLED)

                    print("distance ", abs(pointer_y - middle_y))
                    if abs(pointer_y - middle_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    




    cv2.imshow("Image", img)
    cv2.waitKey(1)
