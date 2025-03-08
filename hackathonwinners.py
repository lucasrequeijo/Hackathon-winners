import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# Global variable to store the image object so it doesn't get garbage collected
img_tk = None

# Function to handle mouse click events
def on_click(event):
    x = event.x
    y = event.y
    # Display the coordinates
    coord_label.config(text=f"Clicked at: ({x}, {y})")
    
    # Find the nearest blue square
    if blue_squares:
        nearest_bin = find_nearest_bin(x, y, blue_squares)
        nearest_bin_label.config(text=f"The nearest recycling bin is at: ({nearest_bin[0]}, {nearest_bin[1]})")
        highlight_nearest_bin(nearest_bin)

# Function to upload an image
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        load_image(file_path)

# Function to load and display the image on the canvas
def load_image(file_path):
<<<<<<< HEAD
    global img, img_tk, blue_squares
=======
    global img_tk
>>>>>>> 3397ffb (Refactor image loading to center display on canvas and adjust canvas size)
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
<<<<<<< HEAD
    print(f"Image loaded with size: {img_width}x{img_height}")
    
    # Detect blue squares in the image
    blue_squares = detect_blue_squares(file_path)
    print(f"Blue squares detected at: {blue_squares}")

# Function to detect blue squares in the image
def detect_blue_squares(file_path):
    # Load the image using OpenCV
    img_cv = cv2.imread(file_path)
    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
    
    # Define the range for blue color in HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    
    # Create a mask for blue color
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    blue_squares = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:  # Check if the contour has 4 vertices (square/rectangle)
            x, y, w, h = cv2.boundingRect(approx)
            blue_squares.append((x, y, w, h))
    
    return blue_squares

# Function to find the nearest blue square
def find_nearest_bin(x, y, blue_squares):
    min_distance = float('inf')
    nearest_bin = None
    for (bx, by, bw, bh) in blue_squares:
        bin_center_x = bx + bw // 2
        bin_center_y = by + bh // 2
        distance = np.sqrt((x - bin_center_x) ** 2 + (y - bin_center_y) ** 2)
        if distance < min_distance:
            min_distance = distance
            nearest_bin = (bin_center_x, bin_center_y, bw, bh)
    return nearest_bin

# Function to highlight the nearest blue square
def highlight_nearest_bin(nearest_bin):
    bin_center_x, bin_center_y, bw, bh = nearest_bin
    radius = max(bw, bh) // 2
    canvas.create_oval(bin_center_x - radius, bin_center_y - radius, bin_center_x + radius, bin_center_y + radius, outline="red", width=2)
=======
    print(f"Image loaded with size: {img_width}x{img_height} at position: ({x_pos}, {y_pos})")
>>>>>>> 3397ffb (Refactor image loading to center display on canvas and adjust canvas size)

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

# Create a label to display the nearest recycling bin
nearest_bin_label = tk.Label(root, text="")
nearest_bin_label.pack()

# Create a button to upload an image
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Start the Tkinter event loop
root.mainloop()