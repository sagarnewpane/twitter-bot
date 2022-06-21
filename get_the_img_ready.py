from PIL import Image,ImageDraw,ImageFont
import textwrap
from string import ascii_letters

def write_on_image(quote):
    # Open image
    img = Image.open(fp='thumbnail.jpg', mode='r')

    # Load custom font
    font = ImageFont.truetype(font='NotoSans-Regular.ttf', size=42)
    # Create DrawText object
    draw = ImageDraw.Draw(img)

    # Define our text
    text = quote

    # Calculate the average length of a single character of our font.
    # Note: this takes into account the specific font and font size.
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

    # Translate this average length into a character count
    max_char_count = int(img.size[0] * .93 / avg_char_width)

    # Create a wrapped text object using scaled character count
    text = textwrap.fill(text=text, width=max_char_count)

    # Add text to the image
    draw.text(xy=(100,100), text=text, font=font,anchor='ms', fill='#000000')

    # view the result
    img.save('img_with_quotes.jpg')