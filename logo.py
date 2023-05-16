from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Set logo dimensions and colors
logo_width = 400
logo_height = 400
background_color = '#FFFFFF'  # White
text_color = '#000000'  # Black
chart_color = '#1f77b4'  # Default color from Matplotlib

# Create a blank image with a white background
logo_image = Image.new('RGB', (logo_width, logo_height), background_color)
draw = ImageDraw.Draw(logo_image)

# Define fonts
title_font = ImageFont.truetype('Arial.ttf', 48)
subtitle_font = ImageFont.truetype('Arial.ttf', 24)

# Draw book symbol
book_width = 200
book_height = 200
book_position = (logo_width // 2 - book_width // 2, logo_height // 2 - book_height // 2)
draw.rectangle([book_position, (book_position[0] + book_width, book_position[1] + book_height)], fill=chart_color)

# Draw line chart symbol
chart_width = 150
chart_height = 150
chart_position = (logo_width // 2 - chart_width // 2, logo_height // 2 - chart_height // 2)
draw.rectangle([chart_position, (chart_position[0] + chart_width, chart_position[1] + chart_height)], fill=chart_color)

# Add club name and subtitle
club_name = "LitData"
subtitle = "Literature Club with Data Science"
title_width, title_height = draw.textsize(club_name, font=title_font)
subtitle_width, subtitle_height = draw.textsize(subtitle, font=subtitle_font)
title_position = (logo_width // 2 - title_width // 2, logo_height // 2 + book_height // 2 + 20)
subtitle_position = (logo_width // 2 - subtitle_width // 2, title_position[1] + title_height + 10)
draw.text(title_position, club_name, font=title_font, fill=text_color)
draw.text(subtitle_position, subtitle, font=subtitle_font, fill=text_color)

# Save the logo as an image file
logo_image.save('litdata_logo.png')

# Display the logo using Matplotlib
plt.imshow(logo_image)
plt.axis('off')
plt.show()
