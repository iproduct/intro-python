def print_hierarchy(w, depth=0):
    print(
        '  ' * depth + w.winfo_class()
        + ' w=' + str(w.winfo_width()) + " h=" + str(w.winfo_height())
        + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y())
    )
    for chw in w.winfo_children():
        print_hierarchy(chw, depth + 1)


def get_ceter_window_left_top(parent, width, height):
    """Returns the left and top coordinates of a top level window to centwred on the screen"""
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()
    return ((screen_width - width) // 2, (screen_height - height) // 2)
