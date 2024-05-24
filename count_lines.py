import os
import json

# Set the path to the "Downloads/nbanalysis" folder
folder_path = os.path.expanduser("~/Downloads/nbanalysis/lf courses")

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file has a .ipynb extension
    if file_name.endswith(".ipynb"):
        file_path = os.path.join(folder_path, file_name)
        
        try:
            # Open the .ipynb file and load its contents as JSON
            with open(file_path, "r") as file:
                notebook = json.load(file)
            
            # Initialize a variable to store the total lines of code
            total_lines = 0
            
            # Iterate over each cell in the notebook
            for cell in notebook["cells"]:
                # Check if the cell type is "code"
                if cell["cell_type"] == "code":
                    # Split the source code into lines and count them
                    lines = cell["source"]
                    total_lines += len(lines)
            
            # Print the file name and the total lines of code
            print(f"{file_name}: [{total_lines}]")
        
        except Exception as e:
            # Handle any exceptions that occur while processing the file
            print(f"Error processing {file_name}: {str(e)}")