import tkinter as tk
from tkinter import scrolledtext

def update_info(event=None):
    text_content = text_area.get("1.0", "end-1c")
    words = len(text_content.split())
    minutes = words // 130
    seconds = int((words / 130 - minutes) * 60)
    word_count_label.config(text=f"Word Count: {words}")
    time_label.config(text=f"Estimated Time: {minutes}:{seconds:02d}")

# Create the main window
root = tk.Tk()
root.title("Speech Time Estimator")

# Create a text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)
text_area.bind("<KeyRelease>", update_info)

# Labels for displaying the word count and time
word_count_label = tk.Label(root, text="Word Count: 0")
word_count_label.pack()
time_label = tk.Label(root, text="Estimated Time: 0:00")
time_label.pack()

# Run the application
root.mainloop()
