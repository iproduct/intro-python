def center_window(top_window, width=600, height=400):
    left, top = calculate_position(top_window, width, height)
    top_window.geometry(f"{width}x{height}+{left}+{top}")

def calculate_position(parent, width=600, height=400):
    parent_width = parent.winfo_screenwidth()
    parent_height = parent.winfo_screenheight()
    left = (parent_width - width) // 2
    top = (parent_height - height) // 2
    return (left, top)