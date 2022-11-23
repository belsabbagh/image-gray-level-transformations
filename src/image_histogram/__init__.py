import matplotlib.pyplot as plt
import numpy as np


def generate_image_histogram(img):
    return np.histogram(img, bins=range(0, 256))


def plot_image_histogram(title, img):
    hist, bins = generate_image_histogram(img)
    plt.plot(hist)
    plt.title(title)
    plt.show()
