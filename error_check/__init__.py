# TODO: Work out how to turn this into it's own module, upload to pypi, market
import os
import sys
import json

# import json file as dict
with open("internal.json", "r") as f:
  settings = json.load(f)

# error check
def libraryError():
  print("One or more libraries were not installed properly. Installing...")
  os.system("pip install -r requirements.txt") # TODO: macOS and Linux support

def errorCheck():
  # Check arguments
  if len(sys.argv) < 2:
    raise Exception("No arguments specified")

  # Check libraries
  errors = 0
  for i in settings["cli-dependencies"]:
    if os.system(f"{i} --version") == 1:
      errors += 1

  if errors != 0:
    libraryError()

def run():
  errorCheck()