from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip


def get_video_duration(file_path):
    clip = VideoFileClip(file_path)
    duration = clip.duration
    clip.close()
    return duration


def add_text_to_image(image_path, text):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    # Use DejaVuSans-Bold.ttf font file
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font = ImageFont.truetype(font_path, 20)

    # Get text size
    textbbox = draw.textbbox((0, 0), text, font=font)
    textwidth = textbbox[2] - textbbox[0]
    textheight = textbbox[3] - textbbox[1]

    # Set position: bottom-right corner
    width, height = image.size
    x = width - textwidth - 10
    y = height - textheight - 10

    # Draw text
    draw.text((x, y), text, font=font, fill="white")

    # Save the edited image
    image.save(image_path)

# Test the function
# add_text_to_image("thumbnail.jpg", "00:55, 16.7 MB")
