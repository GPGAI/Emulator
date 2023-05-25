from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()


def key_emulator(shot):
    keys = {
        "W": Key.up,
        "S": Key.down,
        "A": Key.left,
        "D": Key.right,
        "Shift": Key.shift,
        "Space": Key.space,
        "Ctrl": Key.ctrl,
        "F1": Key.f1,
        "F2": Key.f2,
        "Tab": Key.tab,
        "M": "m",
        "R": "r",
        "G": "g",
        "E": "e",
        "F10": Key.f10
    }

    # emulate key press
    for key, value in shot.items():
        if key in keys and value:
            keyboard.press(keys[key])
            keyboard.release(keys[key])

    # emulate mouse movement and click
    if "xCoord" in shot and "yCoord" in shot:
        mouse.position = (shot["xCoord"], shot["yCoord"])

    if "clickType" in shot:
        if shot["clickType"] == 1:
            mouse.click(Button.left, 1)
        elif shot["clickType"] == 2:
            mouse.click(Button.right, 1)

shot = {
    "W": True,
    "S": True,
    "A": False,
    "D": False,
    "Shift": False,
    "Space": False,
    "Ctrl": False,
    "F1": False,
    "F2": False,
    "Tab": False,
    "M": False,
    "R": False,
    "G": False,
    "E": False,
    "F10": False,
    "xCoord": 100,
    "yCoord": 100,
    "clickType": 2
}


key_emulator(shot)
