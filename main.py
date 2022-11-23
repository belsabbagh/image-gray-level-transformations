from src.gray_level_transformations import correct_gamma
from src.image_ops import read_img_grayscale, show_img

if __name__ == '__main__':
    img_path = 'data\\img\\grayscale_spectrum.png'
    img = read_img_grayscale(img_path)
    new_img = correct_gamma(img, 3)
    show_img('correction', new_img)
