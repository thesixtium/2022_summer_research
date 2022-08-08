import find_windows
import get_gui_positions

import pyautogui

'''
    pyautogui.size() : get screen size
    pyautogui.position() : get mouse current position
    pyautogui.moveTo(x, y, duration=z) : move mouse to position
        x : x position on screen
        y : y position on screen
        z : how long to spend moving mouse
    pyautogui.moveRel(x, y, duration=z) : move mouse relative to current position
        x : x amount from current position
        y : y amount from current position
        z : how long to spend moving mouse
    pyautogui.click() : left click on screen with mouse
    pyautogui.click(button="right") : right click on screen with mouse
    pyautogui.dragto(x, y, duration=z)
        x : x position on screen
        y : y position on screen
        z : how long to spend dragging mouse
    pyautogui.dragRel(x, y, duration=z)
        x : x amount from current position
        y : y amount from current position
        z : how long to spend dragging mouse
    pyautogui.typewrite(x)
        x : string to be typed
    pyautogui.press(x)
        x : key to be pressed
    pyautogui.hotkey(x, y, ...)
        x : key to be pressed in hotkey sequence
        y : key to be pressed in hotkey sequence
        ...: any additional / optional keys to press
    pyautogui.screenshot(x)
        x : screenshot name (including extension such as ".png")
'''


def main():
    window_string = "general"
    window_location = find_windows.run(window_string)
    if len(window_location) != 1:
        exception_string = "More than 1 window with title containing '" + \
                        window_string + \
                        "' string. Total amount of windows that match: " + \
                        str(len(window_location))
        exception_string += "\nMatching windows found:"
        for window in window_location:
            exception_string += "\n\t - " + window["name"]
        raise Exception(exception_string)
    window_location = window_location[0]
    movement_gui_positions = get_gui_positions.movement_gui_positions(
        window_location["x"],
        window_location["y"],
        window_location["w"],
        window_location["h"]
    )
    print(movement_gui_positions)

    base_image = "controlSS.png"
    find_image = [
        "laser_data_labels.png",
        "laser_header.png",
        "laser_lateral_force.png",
        "laser_normal_force.png",
        "laser_total_signal.png"
    ]

    for find in find_image:
        get_gui_positions.laser_window_positions(base_image, find)


if __name__ == '__main__':
    main()
