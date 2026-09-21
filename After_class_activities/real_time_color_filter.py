import cv2
import numpy as np

def apply_color_filter(image, filter_type, red, green, blue):
    """Apply the colour filter"""
    new_image = "beach.jpeg()"

    if filter_type == "red":
        new_image[:, :, 1] = 0
        new_image[:, :, 0] = 0

    elif filter_type == "blue":
        new_image[:, :, 1] = 0
        new_image[:, :, 2] = 0

    elif filter_type == "green":
        new_image[:, :, 2] = 0
        new_image[:, :, 0] = 0

    if red > 0:
        new_image[:, :, 2] = cv2.add(new_image[:, :, 2], red)
    elif red < 0:
        new_image[:, :, 2] = cv2.subtract(new_image[:, :, 2], abs(red))

    if green > 0:
        new_image[:, :, 1] = cv2.add(new_image[:, :, 1], green)
    elif green < 0:
        new_image[:, :, 1] = cv2.subtract(new_image[:, :, 1], abs(green))

    if blue > 0:
        new_image[:, :, 0] = cv2.add(new_image[:, :, 0], blue)
    elif blue < 0:
        new_image[:, :, 0] = cv2.subtract(new_image[:, :, 0], abs(blue))

    return new_image


image = cv2.imread("beach.jpeg")
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"

    red = 0
    green = 0
    blue = 0

    print("Press a key:")
    print("r - Red")
    print("g - Green")
    print("b - Blue")
    print("i - More Red")
    print("d - Less Blue")
    print("Up Arrow - More Green")
    print("Down Arrow - Less Red")
    print("s - Save")
    print("q - Quit")

    while True:
        new_image = apply_color_filter(
            image, filter_type, red, green, blue
        )

        cv2.imshow("Filtered Image", new_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red"

        elif key == ord('g'):
            filter_type = "green"

        elif key == ord('b'):
            filter_type = "blue"

        elif key == ord('i'):
            red = red + 50

        elif key == ord('d'):
            blue = blue - 50

        elif key == 82:
            green = green + 50

        elif key == 84:
            red = red - 50

        elif key == ord('s'):
            name = input("Enter a name for the image: ")

            name = name.replace(" ", "_")
            name = name.replace("/", "_")
            name = name.replace("\\", "_")
            name = name.replace(":", "_")

            save_path = "images/" + name + ".jpg"

            cv2.imwrite(save_path, new_image)

            print("Image saved!")

        elif key == ord('q'):
            break

        else:
            print("Try one of the keys above.")

cv2.destroyAllWindows()