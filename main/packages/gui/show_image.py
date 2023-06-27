import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
window = tk.Tk()

# Load the image
image_path = "image.png"  # Replace with the path to your image file
image = Image.open(image_path)
image_width, image_height = image.size

# Create a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
image_label = tk.Label(window, image=photo)
image_label.pack()

# Start the Tkinter event loop
window.mainloop()