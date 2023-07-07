import cv2
import time
import HandTrackingModule as htm

def FingerCount(timeout):
    wCam, hCam = 940, 780
    
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    
    counted = 0

    pTime = 0
    
    detector = htm.handDetector(detectionCon=0.75)
    
    tipIds = [4, 8, 12, 16, 20]

    zeroDetected = False
    oneDetected = False
    twoDetected = False
    threeDetected = False
    fourDetected = False
    fiveDetected = False

    startTime = 0

    finalInput = 0

    
    while counted < 3:
        success, img = cap.read()
        img = detector.findHands(img)
        img = cv2.flip(img, 1)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)
    
        if len(lmList) != 0:
            fingers = []
    
            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
    
            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
    
            totalFingers = fingers.count(1)
            # print(totalFingers)

            if not zeroDetected and totalFingers == 0:
                zeroDetected = True
                oneDetected = False
                twoDetected = False
                threeDetected = False
                fourDetected = False
                fiveDetected = False
                startTime = 0
                startTime = time.time()
            elif not oneDetected and totalFingers == 1:
                zeroDetected = False
                oneDetected = True
                twoDetected = False
                threeDetected = False
                fourDetected = False
                fiveDetected = False
                startTime = 0
                startTime = time.time()
            elif not twoDetected and totalFingers == 2:
                zeroDetected = False
                oneDetected = False
                twoDetected = True
                threeDetected = False
                fourDetected = False
                fiveDetected = False
                startTime = 0
                startTime = time.time()
            elif not threeDetected and totalFingers == 3:
                zeroDetected = False
                oneDetected = False
                twoDetected = False
                threeDetected = True
                fourDetected = False
                fiveDetected = False
                startTime = 0
                startTime = time.time()
            elif not fourDetected and totalFingers == 4:
                zeroDetected = False
                oneDetected = False
                twoDetected = False
                threeDetected = False
                fourDetected = True
                fiveDetected = False
                startTime = 0
                startTime = time.time()
            elif not fiveDetected and totalFingers == 5:
                zeroDetected = False
                oneDetected = False
                twoDetected = False
                threeDetected = False
                fourDetected = False
                fiveDetected = True
                startTime = 0
                startTime = time.time()
    
            if time.time() - startTime > timeout:
                finalInput += totalFingers
                counted += 1
                zeroDetected = False
                oneDetected = False
                twoDetected = False
                threeDetected = False
                fourDetected = False
                fiveDetected = False
                startTime = 0


            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
    
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
    
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
        cv2.putText(img, f'{int(time.time() - startTime)}', (300, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 255, 0), 3)
        
        cv2.putText(img, f'{finalInput}', (300, 120), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 255, 0), 3)
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)

    print(finalInput)
    return finalInput

# if __name__ == '__main__':
#     detected = FingerCount(timeout=3)
#     if detected == True:
#         print("The face is detected. OK")
#     else:
#         print("I'm sorry but I can't detect your face")