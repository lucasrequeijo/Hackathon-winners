import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Global variable to store the image object so it doesn't get garbage collected
img_tk = None

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
    global img_tk
    img = Image.open(file_path)
    
    # Convert the image to something Tkinter can display
    img_tk = ImageTk.PhotoImage(img)
    
    # Get the dimensions of the canvas and image
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    img_width = img_tk.width()
    img_height = img_tk.height()

    # Calculate the position to center the image
    x_pos = (canvas_width - img_width) // 2
    y_pos = (canvas_height - img_height) // 2
    
    # Clear the canvas and display the image
    canvas.delete("all")
    canvas.create_image(x_pos, y_pos, anchor=tk.NW, image=img_tk)
    canvas.config(scrollregion=canvas.bbox(tk.ALL))
    print(f"Image loaded with size: {img_width}x{img_height} at position: ({x_pos}, {y_pos})")

# Create the main window
root = tk.Tk()
root.title("Click to Get Coordinates")

# Create a canvas widget with larger size (e.g., 1200x800)
canvas = tk.Canvas(root, bg="white", width=1200, height=800)
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
