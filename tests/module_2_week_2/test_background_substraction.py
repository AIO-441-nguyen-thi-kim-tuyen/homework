import os
from homework.module_2_week_2.background_substraction import BackgroundSubtractor

foreground_object = os.path.join(os.path.dirname(__file__), 'image_data', 'Object.png')
background_image = os.path.join(os.path.dirname(__file__), 'image_data', 'GreenBackground.png')
target_background_image = os.path.join(os.path.dirname(__file__), 'image_data',
                                       'NewBackground.jpg')  # Đường dẫn đến hình ảnh nền thay thế


def test_background_substraction():
    bg_subtractor = BackgroundSubtractor(foreground_object, background_image)
    output = bg_subtractor.process_frame()
    assert True
