import os

import cv2

from src.image_ops.get_shape import ImageShape


def get_shape(img):
    """
    Gets a dictionary of the image's shape
    """
    return ImageShape(img)


def read_images_from_directory(dir_path, color_mode):
    return {f: read_img(os.path.join(dir_path, f), color_mode) for f in os.listdir(dir_path)}


def read_img(file_path, color_mode=None):
    if color_mode is None:
        color_mode = cv2.IMREAD_UNCHANGED
    return cv2.imread(file_path, color_mode)


def read_img_color(file_path):
    return read_img(file_path, cv2.IMREAD_COLOR)


def read_img_grayscale(file_path):
    return read_img(file_path, cv2.IMREAD_GRAYSCALE)


def show_img(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None


def save_image(file_path, img):
    return cv2.imwrite(file_path, img)


def blur_image(_img, size):
    return cv2.blur(_img, (size, size))


def filter_image(_img, _kernel):
    return cv2.filter2D(_img, -1, _kernel)
