def center_resize_window(top_window, width=600, height=400):
    left, top = calculate_position(top_window, width, height)
    top_window.geometry(f"{width}x{height}+{left}+{top}")

def calculate_position(parent, width=600, height=400):
    parent_width = parent.winfo_screenwidth()
    parent_height = parent.winfo_screenheight()
    left = (parent_width - width) // 2
    top = (parent_height - height) // 2
    return (left, top)

def print_hierarchy(w, depth=0):
    w.update_idletasks()
    print(
        '  ' * depth + w.winfo_class()
        + ' w=' + str(w.winfo_width()) + " h=" + str(w.winfo_height())
        + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y())
    )
    for chw in w.winfo_children():
        print_hierarchy(chw, depth + 1)