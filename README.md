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