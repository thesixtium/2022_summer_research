import win32gui

window_array = []
search_name = ""

def callback(hwnd, extra):
    global search_name
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    if search_name in win32gui.GetWindowText(hwnd):
        append_dictionary = {
            "name": win32gui.GetWindowText(hwnd),
            "x": x,
            "y": y,
            "w": w,
            "h": h
        }
        window_array.append(append_dictionary)

def run(name):
    global search_name
    search_name = name
    win32gui.EnumWindows(callback, None)
    return window_array
