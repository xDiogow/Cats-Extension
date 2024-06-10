from PIL import Image
import cv2
import os

def get_pixel_colors(image_path):
    """Returns the colors of each pixel in the image

    Args:
        image_path (str): Path where the file is located.

    Returns:
        List: 
    """
    
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        pixel_data = list(img.getdata())
        return pixel_data
    
def get_image_size(image_path):
    """Returns the size of the image

    Args:
        image_path (str): Path where the file is located.

    Returns:
        Tuple: (Height, Width, Dimension)
    """

    im = cv2.imread(image_path)
    return im.shape
    
def rgb_to_hex(colors):
    hex_list = []
    
    for color in colors:
        hex_list.append('{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2]))
    return hex_list


def main():
    image_path = input("Enter image path: ")

    image_size = get_image_size(image_path)
    colors_list = rgb_to_hex(get_pixel_colors(image_path))
    if os.path.exists(image_path[:-4] + ".cats"):
        os.remove(image_path[:-4] + ".cats")
        print('Deleted .cat file!')

    width = 0
    f = open(image_path[:-4] + ".cats", 'a')

    # Saves the dimension of the image in the first line of the file.
    f.write(f'{image_size[1]} {image_size[0]}\n')

    # Saves the hex to a file 6 by 6
    for hex in colors_list:
        if width == image_size[1]:
            f.write('\n')
            width = 0

        f.write(hex)
        width += 1
    f.close()
    print(f'Successfully converted to .cats! Width: {image_size[1]} - Height: {image_size[0]}')

main()