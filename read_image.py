import tkinter as tk

root = tk.Tk("Cats Image Viewer")
canvas = tk.Canvas(root)
canvas.pack()

def get_pixel_colors_and_size(image_path):
    hex_list = [""]
    width = 0
    height = 0
    number_chars = 0
    current_hex = 0
    
    with open(image_path, 'r') as f:
        # Read the first line to get the image dimensions
        dimensions = f.readline().strip().split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        
        for color in f.read():
            if color in '\n\t ':
                continue  # Skip any whitespace or newline characters
            if number_chars == 6:
                number_chars = 0
                current_hex += 1
                hex_list.append("")

            hex_list[current_hex] += color
            number_chars += 1

    return hex_list, width, height

def draw_pixels(canvas, colors, width, height):
    pixel_image = tk.PhotoImage(width=width, height=height)
    for y in range(height):
        for x in range(width):
            color_index = y * width + x
            if color_index < len(colors):
                color = "#" + colors[color_index]
                pixel_image.put(color, (x, y))
    canvas.create_image((0, 0), image=pixel_image, anchor='nw')
    canvas.image = pixel_image
    
def main():
    image_path = input("Enter image path: ")

    print('Loading image!')
    colors, width, height = get_pixel_colors_and_size(image_path)
    colors = [color for color in colors if len(color) == 6]
    canvas.config(width=width, height=height)
    draw_pixels(canvas, colors, width, height)
    root.mainloop()

main()
