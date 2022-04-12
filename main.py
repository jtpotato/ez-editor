import error_check



error_check.run()

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