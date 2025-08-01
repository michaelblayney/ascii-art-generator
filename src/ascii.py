from PIL import Image, ImageOps

ASCII_CHARS = "@@%%NNN91ac*+=-:.  "[::-1]
OUTPUT_WIDTH = 100
OUTPUT_HEIGHT = 100

image = Image.open("images/fudge1.png")
image = ImageOps.grayscale(image) 
image = image.resize((OUTPUT_WIDTH, OUTPUT_HEIGHT))

# Map grayscale values to ASCII characters
ascii_art = ""
for y in range(OUTPUT_HEIGHT):
    for x in range(OUTPUT_WIDTH):
        pixelValue = image.getpixel((x,y))
        ascii_index = int(pixelValue / 255 * (len(ASCII_CHARS) - 1))
        ascii_art += ASCII_CHARS[ascii_index]
        ascii_art += ""
    ascii_art += "\n"  # New line after each row

print(ascii_art)

with open("output/ascii_art.txt", "w") as f:
    f.write(ascii_art)

# image.show()