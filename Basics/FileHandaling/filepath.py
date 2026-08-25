
from pathlib import Path

file_path = Path(r"C:\Users\AdminAdmin\Desktop\shahid\python\Simplequestions\FileHandaling\f2.txt")
print(file_path.name)      # f2.txt
print(file_path.stem)      # f2
print(file_path.suffix)    # .txt
print(file_path.parent)   # C:\Users\AdminAdmin\Desktop\shahid
print(file_path.exists()) #True
file = Path(r"FileHandaling/f1.txt")
print(file.parent)
print(file.resolve())
print(file.resolve().parent)