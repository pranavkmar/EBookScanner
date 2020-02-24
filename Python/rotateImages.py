from scipy import ndimage, misc
import numpy as np
import os
import cv2


def main():
    outPath = "C:\Miniconda\envs\.."
    path = "C:\Miniconda\envs\out\.."

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):
        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_rotate = ndimage.imread(input_path)

        # rotate the image
        rotated = ndimage.rotate(image_to_rotate, 45)

        # create full output path, 'example.jpg'
        # becomes 'rotate_example.jpg', save the file to disk
        fullPath = os.path.join(outPath, 'rotated_' + image_path)
        misc.imsave(fullPath, rotated)


if __name__ == '__main__':
    main()
