import time
import keyboard
import mouse

shot = {
    "W": False,
    "S": False,
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
    "xCoord": 0,
    "yCoord": 0,
    "clickType": 0
}

shots = []


# Function to update the mouse data
def update_mouse_data():
    shot["xCoord"], shot["yCoord"] = mouse.get_position()

    if mouse.is_pressed("left"):
        shot["clickType"] = 1  # Left Button (Fire)
    elif mouse.is_pressed("middle"):
        shot["clickType"] = 2  # Wheel button click / Middle button (Alternative fire)
    elif mouse.is_pressed("right"):
        shot["clickType"] = 3  # Right button
    elif mouse.is_pressed("wheel_up"):
        shot["clickType"] = 4  # Wheel up (Previous Weapon)
    elif mouse.is_pressed("wheel_down"):
        shot["clickType"] = 5  # Wheel down (Next Weapon)
    else:
        shot["clickType"] = 0  # No click


# Function to handle key press events
def on_key_press(event):
    if event.name in shot:
        shot[event.name] = True


# Function to handle key release events
def on_key_release(event):
    if event.name in shot:
        shot[event.name] = False


# Register key press and release event handlers
keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)


# Function to write shots to file
def write_shots_to_file():
    current_time = time.strftime("%Y%m%d-%H%M%S")
    filename = f"data/{current_time}_shot.txt"
    with open(filename, "a", encoding="utf-8") as file:
        for o in shots:
            file.write(str(o) + "\n")


# Main loop
while True:
    for _ in range(50000):
        update_mouse_data()
        shots.append(shot.copy())  # Добавляем копию текущего состояния `shot` в `shots`
        time.sleep(1 / 30)

    write_shots_to_file()
    shots.clear()  # Очищаем `shots` после записи в файл
