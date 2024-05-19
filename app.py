import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
from filetypes import filetypes

class CodeEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Basic Code Editor")
        self.geometry("800x600")

        # Setting up the menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New File", command=self.new_file)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="Save File", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        # Text area
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Current file path
        self.current_file = None

    def new_file(self):
        if self.confirm_discard_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.title("Basic Code Editor - New File")

    def open_file(self):
        if self.confirm_discard_changes():
            file_path = filedialog.askopenfilename(
                filetypes=filetypes
            )
            if file_path:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
                self.current_file = file_path
                self.title(f"Basic Code Editor - {os.path.basename(file_path)}")

    def save_file(self):
        if self.current_file:
            self.write_to_file(self.current_file)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
             filetypes=filetypes
        )
        if file_path:
            self.write_to_file(file_path)
            self.current_file = file_path
            self.title(f"Basic Code Editor - {os.path.basename(file_path)}")

    def write_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            messagebox.showinfo("Success", "File saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

    def exit_editor(self):
        if self.confirm_discard_changes():
            self.quit()

    def confirm_discard_changes(self):
        if self.text_area.edit_modified():
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save them before continuing?"
            )
            if response:  # Yes
                self.save_file()
                return True
            elif response is None:  # Cancel
                return False
            else:  # No
                return True
        return True

if __name__ == "__main__":
    editor = CodeEditor()
    editor.mainloop()
