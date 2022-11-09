import pyautogui
import time

startTime = time.time()
time.sleep(5)
file = open("nameList.txt", "r")
for i, name in enumerate(file.readlines()[0:1]):
    time.sleep(1)
    pyautogui.moveTo(x=1141, y=551)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=1141, y=551)
    pyautogui.tripleClick()
    pyautogui.typewrite(name.strip().upper())
    time.sleep(0.5)

    pyautogui.moveTo(x=1824, y=109)
    pyautogui.click()
    time.sleep(0.5)

    # Download Option
    pyautogui.moveTo(x=1583, y=759)
    pyautogui.click()
    time.sleep(0.5)

    # Option
    pyautogui.moveTo(x=1644, y=294)
    pyautogui.click()
    time.sleep(0.5)

    # PDF
    pyautogui.moveTo(x=1607, y=545)
    pyautogui.click()
    time.sleep(0.5)

    # Download Btn
    pyautogui.moveTo(x=1509, y=538)
    pyautogui.click()
    time.sleep(10)

    # File name
    pyautogui.moveTo(x=1053, y=109)
    pyautogui.tripleClick()
    pyautogui.typewrite(name+".pdf")
    pyautogui.moveTo(x=1472, y=890)
    pyautogui.click()

    print(f"{i+1}) {name} saved")

print("Total Time Taken: " + str(time.time() - startTime))