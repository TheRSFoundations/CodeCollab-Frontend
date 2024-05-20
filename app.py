import tkinter as tk
from tkinter import scrolledtext
from lib.file_ops.file_operations import new_file, open_file, save_file, save_file_as, exit_editor

def create_menu(root, text_area, current_file):
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

    # Additional platform-specific configuration for macOS
    if root.tk.call('tk', 'windowingsystem') == 'aqua':
        root.createcommand('::tk::mac::Quit', lambda: exit_editor(root, text_area, current_file))
        # Ensure the app name appears correctly in the menu bar
        root.createcommand('tk::mac::ShowPreferences', lambda: None)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Basic Code Editor")
    root.geometry("1440x1080")

    # Text area
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
    text_area.pack(fill=tk.BOTH, expand=1)

    # Current file path as a list to allow modifications within functions
    current_file = [None]

    create_menu(root, text_area, current_file)

    root.mainloop()
