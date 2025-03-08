import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to handle mouse click events
def on_click(event):
    x = event.x
    y = event.y
    # Display the coordinates
    coord_label.config(text=f"Clicked at: ({x}, {y})")

# Function to upload an image
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        load_image(file_path)

# Function to load and display the image on the canvas
def load_image(file_path):
    global img, img_tk
    img = Image.open(file_path)
    
    # Get the dimensions of the image
    img_width, img_height = img.size
    
    # Resize the canvas to match the image size
    canvas.config(width=img_width, height=img_height)
    
    # Resize the image to fit the canvas while maintaining aspect ratio
    img_tk = ImageTk.PhotoImage(img)
    
    # Clear the canvas and display the image
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.config(scrollregion=canvas.bbox(tk.ALL))
    print(f"Image loaded with size: {img_width}x{img_height}")

# Create the main window
root = tk.Tk()
root.title("Click to Get Coordinates")

# Create a canvas widget
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the click event to the on_click function
canvas.bind("<Button-1>", on_click)

# Create a label to display the coordinates
coord_label = tk.Label(root, text="Click on the canvas to get coordinates")
coord_label.pack()

# Create a button to upload an image
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Start the Tkinter event loop
root.mainloop()