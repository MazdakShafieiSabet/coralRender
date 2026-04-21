import tkinter as tk
from tkinter import ttk
import subprocess, threading

## GUI initialisation
root = tk.Tk()
root.title("coralRender")

## Making Window appear in the middle of the screen
window_width = 738
window_height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

## Render logic
def run_render():
    blender_file = blend_file_entry.get()
    frame_start = frame_start_entry.get()

    if frame_start == "":
        frame_start = "1"  ## default to frame 1 if not specified
    
    cmd = ["blender", "-b", blender_file]
    
    if animation_var.get():
        cmd += ["-s", frame_start, "-a"]
    else:
        cmd += ["-f", frame_start]
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        output_box.insert(tk.END, line)
        output_box.see(tk.END)


## Labels
main_label = tk.Label(root, text="coralRender", font=(32))
blender_file_label = tk.Label(root, text="Path to .blend file:")
frame_start_label = tk.Label(root, text="Start Frame (default is 1):")
default_output_label = tk.Label(root, text="Output Path to remove (can be left empty):")

## Entries
blend_file_entry = tk.Entry(root, width=25)
frame_start_entry = tk.Entry(root, width=25)
default_output_entry = tk.Entry(root, width=25)

## Checkbox
file_output_var = tk.BooleanVar()
animation_var = tk.BooleanVar()
batch_var = tk.BooleanVar()
file_output_only = ttk.Checkbutton( root, text='Only use File Output Nodes', variable=file_output_var)
animation_checkbox = ttk.Checkbutton( root, text='Render Animation', variable=animation_var)
batch_render_checkbox = ttk.Checkbutton( root, text='Batch Render', variable=batch_var)

## Output box
output_box = tk.Text(root, height=30, width=90)

## Buttons
start_render_button = tk.Button(root, text="Start Render", command=lambda: threading.Thread(target=run_render).start())

## Gridding
main_label.grid(row=0, column=0, columnspan=3, pady=10)
blender_file_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
blend_file_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
frame_start_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
frame_start_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)
default_output_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
default_output_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

batch_render_checkbox.grid(row=2, column=2, sticky="w", padx=5, pady=5)
animation_checkbox.grid(row=3, column=2, sticky="w", padx=5, pady=5)
file_output_only.grid(row=4, column=2, sticky="w", padx=5, pady=5)

output_box.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

start_render_button.grid(row=7, column=0, columnspan=3, pady=10)


root.mainloop()

## print("This is an automated render script meant to be used to render out images and image sequences from Blender.")
## print("This script assumes you already have Blender installed and it is added to your system's PATH variable.")
## print("If this is not the case, follow the instructions in the README file to set up Blender and add it to your PATH variable.")
## 
## blend_file = input("Enter the path to your .blend file (including the filename and extension): ")
## output_path = input("Enter where the default Blender output is to remove it after rendering (if you don't have a File Output node in your compositor, you can just enter and the directory won't be deleted): ")

