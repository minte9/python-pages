import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
window = tk.Tk()
window.title("Image Fill")

# Create a new blank image
image = Image.new("RGB", (400, 400), "white")

# Create a Tkinter compatible photo image
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
image_label = tk.Label(window, image=photo)
image_label.pack()

# Start the Tkinter event loop
window.mainloop()
