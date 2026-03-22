from PIL import Image
import sys

def png_to_himg(input_file, output_file):
    img = Image.open(input_file).convert("RGB")
    width, height = img.size
    pixels = img.load()

    with open(output_file, "w") as f:
        f.write("HIMG\n")
        f.write(f"{width} {height}\n")

        for y in range(height):
            row = []
            for x in range(width):
                r, g, b = pixels[x, y]
                row.append(f"{r:02X}{g:02X}{b:02X}")
            f.write(" ".join(row) + "\n")

    print("[OK] HIMG created:", output_file)


def himg_to_png(input_file, output_file):
    with open(input_file, "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    if lines[0] != "HIMG":
        print("[ERROR] Invalid HIMG file")
        return

    width, height = map(int, lines[1].split())
    data = lines[2:]

    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for y, row in enumerate(data):
        cols = row.split()
        for x, hex_color in enumerate(cols):
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            pixels[x, y] = (r, g, b)

    img.save(output_file)
    print("[OK] PNG generated:", output_file)


if len(sys.argv) < 4:
    print("Usage:")
    print("  python himg.py encode input.png output.himg")
    print("  python himg.py decode input.himg output.png")
    sys.exit()

mode = sys.argv[1]

if mode == "encode":
    png_to_himg(sys.argv[2], sys.argv[3])
elif mode == "decode":
    himg_to_png(sys.argv[2], sys.argv[3])
else:
    print("[ERROR] Invalid mode")
