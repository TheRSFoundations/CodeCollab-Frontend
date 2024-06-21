def copy_line(text_area):
    try:
        text_area.event_generate("<<Copy>>")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy line: {e}")

def cut_line(text_area):
    try:
        text_area.event_generate("<<Cut>>")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to cut line: {e}")

def paste_line(text_area):
    try:
        text_area.event_generate("<<Paste>>")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to paste line: {e}")

def undo_function(text_area):
    try:
        text_area.event_generate("<<Undo>>")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to undo: {e}")

def redo_function(text_area):
    try:
        text_area.event_generate("<<Redo>>")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to redo: {e}")
