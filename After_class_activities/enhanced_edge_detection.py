import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image(name, picture):
    """Function used to display an image."""
    plt.figure(figsize=(8, 8))

    if len(picture.shape) == 2:
        plt.imshow(picture, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))

    plt.title(name)
    plt.axis('off')
    plt.show()


def edge_detection(picture, method="sobel", kernel_size=3, low_threshold=100, high_threshold=200):
    """Uses the selected method to detect edges."""
    gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

    if method == "sobel":
        edge_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
        edge_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)

        return cv2.bitwise_or(edge_x.astype(np.uint8), edge_y.astype(np.uint8))

    elif method == "canny":
        return cv2.Canny(gray, low_threshold, high_threshold)

    elif method == "laplacian":
        return cv2.Laplacian(gray, cv2.CV_64F).astype(np.uint8)


def image_filter(picture, filter_method="gaussian", kernel_size=5):
    """Uses the selected filter on the image."""

    if filter_method == "gaussian":
        return cv2.GaussianBlur(picture, (kernel_size, kernel_size), 0)

    elif filter_method == "median":
        return cv2.medianBlur(picture, kernel_size)


def edge_detection_activity(file_path):
    """Activity for trying different edge detection methods and filters."""
    picture = cv2.imread(file_path)

    if picture is None:
        print("Error: Image not found!")
        return

    print("Choose an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        selection = input("Enter your choice (1-6): ")

        if selection == "1":
            kernel_size = int(input("Enter kernel size for Sobel (odd number): "))

            output = edge_detection(
                picture,
                method="sobel",
                kernel_size=kernel_size
            )

            show_image("Sobel Edge Detection", output)

        elif selection == "2":
            low_threshold = int(input("Enter lower threshold for Canny: "))
            high_threshold = int(input("Enter upper threshold for Canny: "))

            output = edge_detection(
                picture,
                method="canny",
                low_threshold=low_threshold,
                high_threshold=high_threshold
            )

            show_image("Canny Edge Detection", output)

        elif selection == "3":
            output = edge_detection(picture, method="laplacian")

            show_image("Laplacian Edge Detection", output)

        elif selection == "4":
            kernel_size = int(input("Enter kernel size for Gaussian smoothing (odd number): "))

            output = image_filter(
                picture,
                filter_method="gaussian",
                kernel_size=kernel_size
            )

            show_image("Gaussian Smoothed Image", output)

        elif selection == "5":
            kernel_size = int(input("Enter kernel size for Median filtering (odd number): "))

            output = image_filter(
                picture,
                filter_method="median",
                kernel_size=kernel_size
            )

            show_image("Median Filtered Image", output)

        elif selection == "6":
            print("Exiting...")
            print("Thank you for using the edge detection activity!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")


edge_detection_activity('beach.jpeg')
