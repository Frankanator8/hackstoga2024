
# Attemping Hand detection and tracking 

# pip install mediapipe, cv2, imutils

# drawing from mediapipe, used there intro to acess their dataset

# Jake Frischmann




import cv2

import mediapipe as mp

import imutils






hands_mp = mp.solutions.hands

draw = mp.solutions.drawing_utils




cam = cv2.VideoCapture(0)

img_w = 1000




hand_positions = []

frame_distance = 30

movement_threshold_x = img_w /4

movement_threshold_y = img_w/4

move_cooldown =10

move_cooldown_timer =0




while cam.isOpened():

    is_on, image = cam.read()

    image_height, image_width, dp = image.shape

    move_cooldown_timer +=1


    #brg to rgb. cv2 is weird and does brg, WHO DOES BRG?!?!

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)




    #Appying media pipe

    image_with_mp = hands_mp.Hands().process(image)

    

    #BACK TO CV2! Gotta convert back

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if image_with_mp.multi_hand_landmarks:
# as long as there is a hand: draw on

        for hand_lm in image_with_mp.multi_hand_landmarks:

            draw.draw_landmarks(image, hand_lm,connections=hands_mp.HAND_CONNECTIONS)

            

        for ids, lm in enumerate(hand_lm.landmark):

            x = lm.x * image_width

            y = lm.y * image_height

            hand_positions.append([x,y])

            if len(hand_positions) >= frame_distance:

                past = hand_positions.pop(0)

                if move_cooldown_timer > move_cooldown:

                    if past[0]- x > movement_threshold_x:

                        print('move right')

                        move_cooldown_timer =0

                    elif past[0] - x < -1 * movement_threshold_x:

                        print('move left')

                        move_cooldown_timer=0

                    # if past[1] - y > movement_threshold_y:

                    #     print('move up')

                    #     move_cooldown_timer = 0

                    # elif past[1] - y < -1 * movement_threshold_y:

                    #     print('move down')

                    #     move_cooldown_timer = 0

            

            # print(x, y, ids, 'lm', "x | y | ids | landmark")




    

    

    

    

    image = imutils.resize(image, width=img_w)

    cv2.imshow('', image)

    

    

    if cv2.waitKey(5) & 0xFF == ord("q"):

        break




cam.release()

cv2.destroyAllWindows()
