""" Helper functions. """

import pyautogui
# get the game corner coordinates
CORNER = pyautogui.locateOnScreen('ingame-corner.png')

# our coordinates are shifted 25 px up because of steam border

# lower pyautogui.PAUSE constant for more efficiency
pyautogui.PAUSE = 0.01


def getCoords(x, y):
    return (CORNER[0] + x, CORNER[1] + y - 25)


def moveTo(x, y):
    x = CORNER[0] + x
    y = CORNER[1] + y - 25
    pyautogui.moveTo(x, y)


def click(x, y, button="left"):
    moveTo(x, y)
    pyautogui.click(button=button)
    sleep(0.1)


def sleep(time):
    pyautogui.sleep(time)
