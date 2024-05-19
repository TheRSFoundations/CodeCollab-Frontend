import tkinter as tk
from tkinter import scrolledtext
from file_ops.file_operations import new_file, open_file, save_file, save_file_as, exit_editor

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Basic Code Editor")
    root.geometry("1440x1080")

    # Setting up the menu
    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New File", command=lambda: new_file(text_area, current_file, root))
    file_menu.add_command(label="Open File", command=lambda: open_file(text_area, current_file, root))
    file_menu.add_command(label="Save File", command=lambda: save_file(text_area, current_file))
    file_menu.add_command(label="Save File As", command=lambda: save_file_as(text_area, current_file))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=lambda: exit_editor(root, text_area, current_file))

    # Text area
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
    text_area.pack(fill=tk.BOTH, expand=1)

    # Current file path
    current_file = None

    root.mainloop()
