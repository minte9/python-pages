from PIL import Image, ImageDraw

# Create a new blank image
image = Image.new("RGB", (400, 400), "white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw the outer circle
draw.ellipse((20, 20, 350, 350), fill=None, outline="black")

# Draw the inner circles
draw.ellipse((150, 50, 250, 150), fill=None, outline="black")
draw.ellipse((150, 250, 250, 350), fill=None, outline="black")

# Draw the curved median lines
draw.arc((100, 20, 280, 190), -90, 90, fill="black")
draw.arc((100, 190, 280, 380), 90, 270, fill="black")

# Display the image
image.show()
