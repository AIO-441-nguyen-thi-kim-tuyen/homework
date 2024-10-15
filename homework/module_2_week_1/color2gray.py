from PIL import Image
import numpy as np
import matplotlib.image as mpimg


class ColorToGrayscale:
    def __init__(self, image_path):
        # self.image = Image.open(image_path)
        self.image = mpimg.imread(image_path)
        self.image_np = np.array(self.image)

    # Question 12
    def to_grayscale_lightness(self):
        # Lightness method: (max(R, G, B) + min(R, G, B)) / 2
        max_rgb = np.max(self.image_np[:, :, :3], axis=2)
        min_rgb = np.min(self.image_np[:, :, :3], axis=2)
        lightness = (max_rgb + min_rgb) / 2
        return lightness

    # Question 13
    def to_grayscale_average(self):
        # Average method: (R + G + B) / 3
        average = np.mean(self.image_np[:, :, :3], axis=2)
        return average

    # Question 14
    def to_grayscale_luminosity(self):
        # Luminosity method: 0.21 * R + 0.72 * G + 0.07 * B
        luminosity = (0.21 * self.image_np[:, :, 0] +
                      0.72 * self.image_np[:, :, 1] +
                      0.07 * self.image_np[:, :, 2])
        return luminosity

    def save_image(self, image_array, path):
        image = Image.fromarray(image_array.astype(np.uint8))
        image.save(path)

    # def show_image(self, image_array):
    #     image = Image.fromarray(image_array)
    #     image.show()
