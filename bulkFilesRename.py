#import os
from pathlib import Path

folder = Path("path of the folder")
files = list(folder.iterdir())

for index, file in enumerate(files, start=1):
    if file.is_file() and file.suffix.lower() in ['.txt', '.png', '.jpg']:
    
        new_name = f"file{index}{file.suffix}"
        new_path = folder / new_name

    
        temp_index = index
        while new_path.exists():
            temp_index += 1
            new_name = f"file{temp_index}{file.suffix}"
            new_path = folder / new_name

        
        file.rename(new_path)

        
        print(f"Renamed: {file.name} → {new_path.name}")
