import HandCounting

startDetection = HandCounting

totalFingers = startDetection.FingerCount(timeout=3)

toBinary = bin(totalFingers)[2:]
if len(toBinary) < 4:
    while len(toBinary) < 4:
        toBinary = "0" + toBinary
        print(toBinary)

