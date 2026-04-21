import tkinter as tk
from tkinter import ttk
import subprocess, threading, os

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

## Batch render logic
def batch_render(frame_start):
    batch = []  ## list of files to be rendered in batch mode
    if not os.path.isdir(blend_file_entry.get()):   ## check if path is a directory
        output_box.insert(tk.END, "Error: Batch mode requires a folder path, not a file.\n")
        return
    else:
        for file in os.scandir(blend_file_entry.get()): ## scan through the provided directory for .blend files
            if file.is_file() and file.name.endswith(".blend"):
                batch.append(os.path.join(blend_file_entry.get(), file.name))
        
        for blend_file in batch:
            cmd = ["blender", "-b", blend_file] ## command prepping
            
            if animation_var.get():
                cmd += ["-s", frame_start, "-a"]    ## animation command
            else:
                cmd += ["-f", frame_start]   ## still frame command
            
            ## actual rendering, used to show output in the text box in the GUI
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                output_box.insert(tk.END, line)
                output_box.see(tk.END)


## Render logic
def run_render():
    blender_file = blend_file_entry.get()
    frame_start = frame_start_entry.get()
    
    if frame_start == "":
        frame_start = "1"   ## default to frame 1 if not specified
    
    if batch_var.get(): ## check if batch render should be applied
        batch_render(frame_start)
    else:   ## single file render
        cmd = ["blender", "-b", blender_file]   ## command prepping
        
        if animation_var.get():
            cmd += ["-s", frame_start, "-a"]    ## animation command
        else:
            cmd += ["-f", frame_start]   ## still frame command
        
        ## actual rendering, used to show output in the text box in the GUI
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            output_box.insert(tk.END, line)
            output_box.see(tk.END)
    
    ## removing double exports, only needed when working with file output nodes in the compositer
    if default_output_entry.get() != "" and file_output_var.get():
        excess_output = default_output_entry.get()
        try:
            if os.path.isdir(excess_output): ## check if the provided path is a directory
                for file in os.scandir(excess_output):
                    if file.is_file():  ## check for files to delete
                        os.remove(os.path.join(excess_output, file.name)) ## remove the files
            else:
                output_box.insert(tk.END, "Error: Default output path is not a valid directory.\n")
        except Exception as e:
            output_box.insert(tk.END, f"Error while trying to remove default output files: {e}\n")

## Labels
main_label = tk.Label(root, text="coralRender", font=(32))
blender_file_label = tk.Label(root, text="Path to .blend file (only add folder for batch rendering):")
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
file_output_only_checkbox = ttk.Checkbutton( root, text='Only use File Output Nodes', variable=file_output_var)
animation_checkbox = ttk.Checkbutton( root, text='Render Animation', variable=animation_var)
batch_render_checkbox = ttk.Checkbutton( root, text='Batch Render', variable=batch_var)

## Output box
output_box = tk.Text(root, height=30, width=90)

## Buttons
start_render_button = tk.Button(root, text="Start Render", command=lambda: threading.Thread(target=run_render).start())

## Gridding
main_label.grid(row=0, column=0, columnspan=3, pady=10)

blender_file_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
frame_start_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
default_output_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)

blend_file_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
frame_start_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)
default_output_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

batch_render_checkbox.grid(row=2, column=2, sticky="w", padx=5, pady=5)
animation_checkbox.grid(row=3, column=2, sticky="w", padx=5, pady=5)
file_output_only_checkbox.grid(row=4, column=2, sticky="w", padx=5, pady=5)

output_box.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

start_render_button.grid(row=7, column=0, columnspan=3, pady=10)

root.mainloop()
