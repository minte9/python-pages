from PIL import Image, ImageDraw

# Create a new blank image
image = Image.new("RGB", (400, 400), "white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw the outer circle
draw.ellipse((20, 20, 380, 380), fill=None, outline="black")

# Draw the inner circles
draw.ellipse((150, 60, 250, 160), fill=None, outline="black")
draw.ellipse((150, 240, 250, 340), fill=None, outline="black")

# Draw the curved median lines
draw.arc((100, 20, 290, 200), -90, 90, fill="black")
draw.arc((100, 200, 290, 380), 90, 270, fill="black")

# Display the image
image.show()
