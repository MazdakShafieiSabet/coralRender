import os

print("This is an automated render script meant to be used to render out images and image sequences from Blender.")
print("This script assumes you already have Blender installed and it is added to your system's PATH variable.")
print("If this is not the case, follow the instructions in the README file to set up Blender and add it to your PATH variable.")

blend_file = input("Enter the path to your .blend file (including the filename and extension): ")
output_path = input("Enter where the default Blender output is to remove it after rendering (if you don't have a File Output node in your compositor, you can just enter and the directory won't be deleted): ")

