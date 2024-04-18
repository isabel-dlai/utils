import tkinter as tk
from tkinter import scrolledtext

def update_info(event=None):
    text_content = text_area.get("1.0", "end-1c")
    words = len(text_content.split())
    minutes = words // 130
    seconds = int((words / 130 - minutes) * 60)
    word_count_label.config(text=f"Word Count: {words}")
    
    # Temporarily make the entry widget editable to update the time
    time_entry.configure(state='normal')  # Allow editing to update the text
    time_entry.delete(0, tk.END)
    time_entry.insert(0, f"{minutes}:{seconds:02d}")
    time_entry.configure(state='readonly')  # Set back to read-only

# Create the main window
root = tk.Tk()
root.title("Speech Time Estimator")
root.geometry("400x300")  # Initial size of the window

# Grid configuration for resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Label for the text area
text_area_label = tk.Label(root, text="Enter text below:")
text_area_label.grid(row=0, column=0, sticky='nw', padx=10, pady=(10, 0))

# Create a text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
text_area.bind("<KeyRelease>", update_info)

# Label for displaying the word count
word_count_label = tk.Label(root, text="Word Count: 0")
word_count_label.grid(row=2, column=0, sticky='nw', padx=10)

# Label for estimated time
time_label = tk.Label(root, text="Estimated time to speak (130 wpm):")
time_label.grid(row=3, column=0, sticky='nw', padx=10)

# Entry for displaying the estimated time, initially read-only
time_entry = tk.Entry(root, justify='center', font=('Arial', 14), borderwidth=2, relief='groove', width=8)
time_entry.grid(row=3, column=0, sticky='ne', padx=10)
time_entry.insert(0, "0:00")
time_entry.configure(state='readonly')  # Set to read-only

# Run the application
root.mainloop()
