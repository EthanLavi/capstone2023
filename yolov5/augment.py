import os
import cv2
import numpy as np
import sys
import random

# Define the brightness adjustment value
#multiple of original image- 0.5 meaning 2x as dark, 2 meaning 2x as bright
# First value is for light, second value is for dark
BRIGHTNESS_ADJUSTMENT = (0.5, 2)

# Define the noise factor value
NOISE_FACTOR = 20

# Define the output directory name
OUTPUT_DIR = "augmented_images"
LABEL_OUTPUT_DIR = "augmented_labels"

def is_in_category(image_name, use_day):
    if use_day:
        return "img_" not in image_name and "ethan" not in image_name
    else:
        return "img_" in image_name or "ethan" in image_name
        

def augment_images(image_dir, label_dir, n, use_day):
    # Create the output directory
    output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_DIR)
    label_output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), LABEL_OUTPUT_DIR)
    if not os.path.exists(output_dir):
        print("making directory..")
        os.mkdir(output_dir)
    else:
        print("directory exists at " + output_dir)
    if not os.path.exists(label_output_dir):
        print("making directory..")
        os.mkdir(label_output_dir)
    else:
        print("directory exists at " + label_output_dir)

    # Get a list of all the image file names in the input directory
    image_file_names = [f for f in os.listdir(image_dir) if (f.endswith(".jpg") or f.endswith(".png")) and is_in_category(f, use_day)]
    label_file_names = [f for f in os.listdir(label_dir) if f.endswith(".txt")]
        
    # Augment all images
    c = 0
    for image_file_name in image_file_names:
        c += 1
        if c > n and n >= 0:
            break
 
        # Load the image
        image_path = os.path.join(image_dir, image_file_name)
        image = cv2.imread(image_path)

        # Adjust the brightness
        index = 0 if use_day else 1
        image = cv2.convertScaleAbs(image, 1, BRIGHTNESS_ADJUSTMENT[index])

        # Add noise
        noise_factor = NOISE_FACTOR / 100.0
        if noise_factor > 0:
            noise = noise_factor * image.max() * (np.random.random(image.shape) - 0.5)
            image = image + noise
            image = np.clip(image, 0, 255)
        
        # Get the label
        label_file_name = None
        for label in label_file_names:
            if label.split(".")[0] == image_file_name.split(".")[0]:
                label_file_name = label

        
        # Make sure we have the label_file_name
        if label_file_name is None:
            c -= 1
            continue

        # Save the augmented image
        output_file_name = f"aug{image_file_name}"
        output_path = os.path.join(output_dir, output_file_name)
        os.system(f"cp {os.path.join(label_dir, label_file_name)} {os.path.join(label_output_dir, 'aug' + label_file_name)}")
        cv2.imwrite(output_path, image)
    print("-- FINISHED AUGMENTATION --")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("""Augments n images in the input directory by adjusting their brightness and adding noise.
Args:
    image_dir (str): Path to the directory containing the input images.
    label_dir (str): Path to the directory containing the labels.
    n (int): How many images to do. If <0 will do all
    use_day (bool): If to augment the night time images or the day time ones (judged via img_ prefix)""")
        exit(0)
    # Get the input directory path from the command line argument
    image_dir = sys.argv[1]
    label_dir = sys.argv[2]
    n = int(sys.argv[3])
    use_day = sys.argv[4]
    if use_day not in ["y", "n"]:
        print("use_day argument must be y or n")
        exit(1)
    
    # Augment 10 images in the input directory
    augment_images(image_dir, label_dir, n, use_day == "y")