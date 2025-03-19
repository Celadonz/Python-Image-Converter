
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import sys


def png_to_ico(input_file, output_file, sizes=None):
    if sizes is None:
        sizes = [16, 32, 48, 64, 128, 256]
    try:
        img = Image.open(input_file)
        img.save(output_file, format='ICO', sizes=[(size, size) for size in sizes])
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt user for input PNG file
    input_png = filedialog.askopenfilename(title="Select a PNG file", filetypes=[("PNG Files", "*.png")])
    # Check if the user provided a filename
    if not input_png:
        print("No input file selected.")
        sys.exit()

    # Prompt user for output ICO file
    output_ico = filedialog.asksaveasfilename(title="Save ICO file as", defaultextension=".ico",
                                              filetypes=[("ICO Files", "*.ico")])
    if not output_ico:
        print("No output file selected.")
        sys.exit()  # Replace return with sys.exit()

    png_to_ico(input_png, output_ico)