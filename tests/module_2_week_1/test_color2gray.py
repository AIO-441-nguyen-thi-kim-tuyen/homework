import os
import sys
import numpy as np

from homework.module_2_week_1.color2gray import ColorToGrayscale

image_path = os.path.join(os.path.dirname(__file__), 'dog.jpeg')
converter = ColorToGrayscale(image_path)

epsilon = sys.float_info.epsilon


# Question 12
def test_to_grayscale_lightness():
    lightness = converter.to_grayscale_lightness()
    converter.save_image(lightness.astype(np.uint8), os.path.join(os.path.dirname(__file__), 'lightness_grayscale.jpg'))
    assert abs(round(lightness[0, 0], 1) - 102.5) < epsilon


# Question 13
def test_to_grayscale_average():
    average = converter.to_grayscale_average()
    converter.save_image(average, os.path.join(os.path.dirname(__file__), 'average_grayscale.jpg'))
    assert abs(round(average[0, 0], 1) - 107.7) < epsilon


# Question 14
def test_to_grayscale_luminosity():
    luminosity = converter.to_grayscale_luminosity()
    converter.save_image(luminosity, os.path.join(os.path.dirname(__file__), 'luminosity_grayscale.jpg'))
    assert abs(round(luminosity[0, 0], 1) - 126.2) < epsilon
