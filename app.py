import tkinter as tk
import os
from tkinter import scrolledtext, filedialog
from tkinter.ttk import Treeview
from lib.file_ops.file_operations import new_file, open_file, save_file, save_file_as, exit_editor, open_folder


def create_menu(root, text_area, current_file):
    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New File", command=lambda: new_file(
        text_area, current_file, root))
    file_menu.add_command(label="Open File", command=lambda: open_file(
        text_area, current_file, root))
    file_menu.add_command(
        label="Save File", command=lambda: save_file(text_area, current_file))
    file_menu.add_command(label="Open Folder",
                          command=lambda: open_folder(tree, folder_name_label))
    file_menu.add_command(label="Save File As",
                          command=lambda: save_file_as(text_area, current_file))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=lambda: exit_editor(
        root, text_area, current_file))

    # Additional platform-specific configuration for macOS
    if root.tk.call('tk', 'windowingsystem') == 'aqua':
        root.createcommand('::tk::mac::Quit', lambda: exit_editor(
            root, text_area, current_file))
        # Ensure the app name appears correctly in the menu bar
        root.createcommand('tk::mac::ShowPreferences', lambda: None)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Basic Code Editor")
    root.geometry("1440x1080")

    # Main PanedWindow
    main_pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    main_pane.pack(fill=tk.BOTH, expand=1)

    # Left Frame for file and folder viewer
    left_frame = tk.Frame(main_pane, width=300)
    left_frame.pack(fill=tk.Y, expand=0)
    main_pane.add(left_frame)

    # Add label for File Explorer
    file_explorer_label = tk.Label(left_frame, text="File Explorer")
    file_explorer_label.pack(anchor='w')

    # Add label for opened folder name
    folder_name_label = tk.Label(left_frame, text="Opened Folder: None")
    folder_name_label.pack(anchor='w')

    # Add Treeview for file and folder viewer
    tree = Treeview(left_frame)
    tree.pack(fill=tk.BOTH, expand=1)

    # Middle PanedWindow for open files and text editor
    middle_pane = tk.PanedWindow(main_pane, orient=tk.VERTICAL)
    middle_pane.pack(fill=tk.BOTH, expand=1)
    main_pane.add(middle_pane)

    # Top Frame for open files
    top_frame = tk.Frame(middle_pane, height=30)
    top_frame.pack(fill=tk.X, expand=0)
    middle_pane.add(top_frame)

    # Add a label to simulate open files (you can replace this with your logic)
    open_files_label = tk.Label(top_frame, text="Open Files: file1.txt, file2.py")
    open_files_label.pack(side=tk.LEFT, padx=10)

    # Text area for code editing
    text_area = scrolledtext.ScrolledText(middle_pane, wrap=tk.WORD, undo=True)
    text_area.pack(fill=tk.BOTH, expand=1)
    middle_pane.add(text_area)

    # Bottom Frame for terminal/output area
    bottom_frame = tk.Frame(middle_pane, height=150)
    bottom_frame.pack(fill=tk.X, expand=0)
    middle_pane.add(bottom_frame)

    # Add label for Terminal/Output
    terminal_label = tk.Label(bottom_frame, text="Terminal/Output")
    terminal_label.pack(anchor='w')

    # Add a text area for terminal/output (you can replace this with your logic)
    terminal_area = scrolledtext.ScrolledText(bottom_frame, wrap=tk.WORD, undo=True, height=8)
    terminal_area.pack(fill=tk.BOTH, expand=1)

    # Current file path as a list to allow modifications within functions
    current_file = [None]

    create_menu(root, text_area, current_file)

    root.mainloop()