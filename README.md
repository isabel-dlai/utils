# Utilities

A collection of automation tools that may be of use.

## extract_notes_from_slides_cwd.py

Identifies all `.pptx` files in the current working directory, extracts all speaker notes separated by slide into a `.txt` file that begins with `[Notes]` and ends with the original file name, saved in the current working directory.

### Installation instructions

After pulling the code, you'll need to make sure you have `python-pptx` package installed.

```os
pip install python-pptx
python3 extract_notes_from_slides_cwd.py
```

## speech_length_gui.py

This script creates a simple GUI application that allows users to paste or type text into a text box. As the text is entered, the application calculates and displays the number of words and estimates the time it would take to speak the text aloud at a rate of 130 words per minute. The calculation updates live, providing instant feedback as the user modifies the text. This can be particularly useful for preparing speeches, presentations, or determining the length of spoken segments.

### Installation instructions

Before running the script, ensure that you have Python installed along with the Tkinter library, which is used for the GUI components. Tkinter is included with most Python installations, but if it's not present, you can install it with your package manager.

```sh
pip install tk
python3 speech_length_gui.py
```

To run the script, simply navigate to the directory containing `speech_length_gui.py` and execute the command above. A window will open where you can start typing or pasting text into the provided text area. The word count and estimated speaking time will update automatically as you edit the text.