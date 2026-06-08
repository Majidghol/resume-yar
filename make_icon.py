from PIL import Image, ImageDraw

img = Image.new("RGB", (512, 512), (20, 20, 20))

draw = ImageDraw.Draw(img)

draw.rounded_rectangle(
    [(40, 40), (472, 472)],
    radius=50,
    fill=(30, 30, 30),
    outline=(255, 255, 255),
    width=8
)

draw.rectangle(
    [(140, 100), (372, 412)],
    fill=(255, 255, 255)
)

draw.line((170, 170, 340, 170), fill=(0, 0, 0), width=6)
draw.line((170, 220, 340, 220), fill=(0, 0, 0), width=6)
draw.line((170, 270, 340, 270), fill=(0, 0, 0), width=6)
draw.line((170, 320, 300, 320), fill=(0, 0, 0), width=6)

img.save("assets/icon.png")

print("✓ icon created: assets/icon.png")
