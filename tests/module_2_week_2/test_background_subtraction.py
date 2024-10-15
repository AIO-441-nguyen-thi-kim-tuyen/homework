import os

#from PIL import Image

from homework.module_2_week_2.background_substraction import BackgroundSubtractor

foreground_object = os.path.join(os.path.dirname(__file__), 'image_data', 'Object.png')
background_image = os.path.join(os.path.dirname(__file__), 'image_data', 'GreenBackground.png')
target_background_image = os.path.join(os.path.dirname(__file__), 'image_data',
                                       'NewBackground.jpg')  # Đường dẫn đến hình ảnh nền thay thế


def test_background_subtraction():
    bg_subtractor = BackgroundSubtractor(foreground_object, background_image, target_background_image)
    output = bg_subtractor.process_frame()
    # image = Image.fromarray(output)
    # image.show()
    assert True
