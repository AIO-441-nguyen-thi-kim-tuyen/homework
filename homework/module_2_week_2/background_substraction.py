import cv2
import numpy as np


class BackgroundSubtractor:
    DEFAULT_RESIZE_WIDTH = 678
    DEFAULT_RESIZE_HEIGHT = 381

    def __init__(self, foreground_object=None, background_image=None, target_background_image=None):
        """
        Khởi tạo đối tượng BackgroundSubtractor.

        Args:
        - foreground_object: đường dẫn đến hình ảnh đối tượng cần trích xuất để dán vào hình nền mới.
        - background_image: đường dẫn đến hình ảnh nền gốc.
        - target_background_image: đường dẫn đến hình ảnh nền thay thế.
        """
        if foreground_object:
            self.foreground_object = cv2.imread(foreground_object)

        if background_image:
            self.background_image = cv2.imread(background_image)

        if target_background_image:
            self.target_background_image = cv2.imread(target_background_image)

    def resize(self, frame, width=DEFAULT_RESIZE_WIDTH, height=DEFAULT_RESIZE_HEIGHT):
        """
        Thay đổi kích thước khung hình.

        Args:
        - frame: khung hình đầu vào.
        - width: chiều rộng mới.
        - height: chiều cao mới.

        Returns:
        - Khung hình đã thay đổi kích thước.
        """
        return cv2.resize(frame, (width, height))

    def compute_difference(self, frame1, frame2):
        """
        Tính toán sự khác biệt giữa hai khung hình .

        Args:
        - frame1: khung hình thứ nhất.
        - frame2: khung hình thứ hai.

        Returns:
        - Kênh đơn của khung hình khác biệt
        """
        difference_three_channel = cv2.absdiff(frame1, frame2)
        difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
        difference_single_channel = difference_single_channel.astype('uint8')
        return difference_single_channel

    def compute_binary_mask(self, difference_single_channel):
        """
        Tạo mặt nạ nhị phân từ kênh đơn.

        Args:
        - difference_single_channel: kênh đơn của khung hình khác biệt.

        Returns:
        - Mặt nạ nhị phân.
        """
        difference_binary = np.where(difference_single_channel >= 15, 255, 0)
        difference_binary = np.stack((difference_binary,) * 3, axis=-1)
        return difference_binary

    def replace_background(self, frame, binary_mask, target_background):
        """
        Thay thế nền trong khung hình.

        Args:
        - frame: khung hình chứa đối tượng đầu vào.
        - binary_mask: mặt nạ nền nhị phân.
        - target_background: nền thay thế

        Returns:
        - Khung hình với nền đã thay thế.
        """

        combined = np.where(binary_mask == 255, frame, target_background)

        return combined

    def process_frame(self):
        """
        Resize các ảnh đầu vào về cùng kích thước
        """
        if self.foreground_object:
            self.foreground_object = self.resize(self.foreground_object)
        else:
            return
        if self.background_image:
            self.background_image = self.resize(self.background_image)
        else:
            return
        if self.target_background_image:
            self.target_background_image = self.resize(self.target_background_image)
        else:
            return

        difference_single_channel = self.compute_difference(self.background_image, self.foreground_object)
        binary_mask = self.compute_binary_mask(difference_single_channel)
        combined = self.replace_background(self.foreground_object, binary_mask, self.target_background_image)
        return combined


# Sử dụng lớp BackgroundSubtractor
if __name__ == "__main__":
    foreground_object = 'path_to_your_foreground_object_image.jpg'
    background_image = 'path_to_your_background_image.jpg'
    target_background_image = 'path_to_your_target_background_image.jpg' # Đường dẫn đến hình ảnh nền thay thế
    bg_subtractor = BackgroundSubtractor(foreground_object, background_image, target_background_image)
    output = bg_subtractor.process_frame()
    cv2.imshow(output)
