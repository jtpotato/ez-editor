import os
import sys

# error check
def libraryError():
  print("One or more libraries were not installed properly. Installing...")
  os.system("pip install -r requirements.txt") # TODO: macOS and Linux support

def errorCheck():
  if os.system("auto-editor --version") == 1 or os.system("ffmpeg-normalize --version") == 1:
    libraryError()

  if len(sys.argv) < 2:
    raise Exception("No arguments specified")

def showVersions():
  os.system("auto-editor --version")
  os.system("ffmpeg-normalize --version")

errorCheck()
# showVersions()

# take input path
input_path = sys.argv[1]
original_path = os.getcwd()

# get parent folder
parent_folder = os.path.dirname(input_path)
print(parent_folder)

# filename
filename = os.path.basename(input_path)

os.chdir(parent_folder)

# os.system(f"ffmpeg-normalize \"{filename}\"")

os.chdir(original_path)