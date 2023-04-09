import os
import cv2
import numpy as np
import sys

# Define the brightness adjustment value
#multiple of original image- 0.5 meaning 2x as dark, 2 meaning 2x as bright
BRIGHTNESS_ADJUSTMENT = 0.5

# Define the noise factor value
NOISE_FACTOR = 20

# Define the output directory name
OUTPUT_DIR = "augmented_images"

def augment_images(input_dir, n):
    """
    Augments n images in the input directory by adjusting their brightness and adding noise.

    Args:
        input_dir (str): Path to the directory containing the input images.
        n (int): Number of images to augment.
    """

    # Create the output directory
    output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_DIR)
    if not os.path.exists(output_dir):
        print("making directory..")
        os.mkdir(output_dir)
    else:
        print("directory exists at " + output_dir)

    # Get a list of all the image file names in the input directory
    image_file_names = [f for f in os.listdir(input_dir) if f.endswith(".jpg") or f.endswith(".png")]

    # Augment n images
    for i in range(n):
        # Select a random image file name
        image_file_name = np.random.choice(image_file_names)

        # Load the image
        image_path = os.path.join(input_dir, image_file_name)
        image = cv2.imread(image_path)

        # Adjust the brightness
        image = cv2.convertScaleAbs(image, 1, BRIGHTNESS_ADJUSTMENT)
        

        # Add noise
        noise_factor = NOISE_FACTOR / 100.0
        if noise_factor > 0:
            noise = noise_factor * image.max() * (np.random.random(image.shape) - 0.5)
            image = image + noise
            image = np.clip(image, 0, 255)

        # Save the augmented image
        output_file_name = f"{os.path.splitext(image_file_name)[0]}_{i+1}.png"
        output_path = os.path.join(output_dir, output_file_name)
        cv2.imwrite(output_path, image)

if __name__ == "__main__":
    # Get the input directory path from the command line argument
    input_dir = sys.argv[1]
    
    n = int(sys.argv[2])
    
    # Augment 10 images in the input directory
    augment_images(input_dir, n)