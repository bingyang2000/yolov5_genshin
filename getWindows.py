import win32gui


def get_visible_windows():
    # 定义一个回调函数来枚举所有可见窗口
    def enum_windows_callback(hwnd, visible_windows):
        if win32gui.IsWindowVisible(hwnd):
            visible_windows.append(hwnd)
        return True

    # 枚举所有可见窗口
    visible_windows = []
    win32gui.EnumWindows(enum_windows_callback, visible_windows)

    return visible_windows


def get_genshin_location():
    for hwnd in get_visible_windows():
        window_title = win32gui.GetWindowText(hwnd)
        if window_title == '原神':
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            return left, top, right, bottom

    return 0, 0, 0, 0
