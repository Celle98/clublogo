from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Set logo dimensions and colors
logo_width = 400
logo_height = 400
background_color = '#000000'  # Black
text_color = '#FFFFFF'  # White

# Create a blank image with a black background
logo_image = Image.new('RGB', (logo_width, logo_height), background_color)
draw = ImageDraw.Draw(logo_image)

# Define font
font_path = 'Arial.ttf'  # Change to the path of your desired font file
font_size = 120
font = ImageFont.truetype(font_path, font_size)

# Define the name
name = "LitData"

# Calculate text size and position
text_width, text_height = draw.textsize(name, font=font)
text_position = ((logo_width - text_width) // 2, (logo_height - text_height) // 2)

# Draw the name
draw.text(text_position, name, font=font, fill=text_color)

# Save the logo as an image file
logo_image.save('litdata_logo.png')

# Display the logo using Matplotlib
plt.imshow(logo_image)
plt.axis('off')
plt.show()
