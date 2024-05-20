import os
from tkinter import filedialog, messagebox
from .filetypes import filetypes

def new_file(text_area, current_file, root):
    if confirm_discard_changes(text_area, current_file):
        text_area.delete(1.0, "end")
        current_file = None
        root.title("Basic Code Editor - New File")

def open_file(text_area, current_file, root):
    if confirm_discard_changes(text_area, current_file):
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            text_area.delete(1.0, "end")
            text_area.insert("insert", content)
            current_file = file_path
            root.title(f"Basic Code Editor - {os.path.basename(file_path)}")

def save_file(text_area, current_file):
    if current_file:
        write_to_file(text_area, current_file)
    else:
        save_file_as(text_area)

def save_file_as(text_area, current_file):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=filetypes)
    if file_path:
        write_to_file(text_area, file_path)
        current_file = file_path

def write_to_file(text_area, file_path):
    try:
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, "end")
            file.write(content)
        messagebox.showinfo("Success", "File saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def confirm_discard_changes(text_area, current_file):
    if text_area.edit_modified():
        response = messagebox.askyesnocancel("Unsaved Changes", "You have unsaved changes. Do you want to save them before continuing?")
        if response:  # Yes
            save_file(text_area, current_file)
            return True
        elif response is None:  # Cancel
            return False
        else:  # No
            return True
    return True

def exit_editor(root, text_area, current_file):
    if confirm_discard_changes(text_area, current_file):
        root.quit()
