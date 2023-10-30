import os
import cv2
from send2trash import send2trash

if __name__ == "__main__":
    root_folder = "D:\\MACVI\\v7\\train"
    imgs_folder = os.path.join(root_folder, "images")
    anns_folder = os.path.join(root_folder, "labels")

    for img_name in os.listdir(imgs_folder):
        full_img_path = os.path.join(imgs_folder, img_name)

        img = cv2.imread(full_img_path, 0)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
        total = th3.shape[0] * th3.shape[1]
        perc = cv2.countNonZero(th3) / total
        if perc < 0.85:
            try:
                os.remove(full_img_path)
                os.remove(os.path.join(anns_folder, img_name))
                print(full_img_path)
            except FileNotFoundError as e:
                print(e)
        # cv2.imshow("a", th3)
        # cv2.waitKey(0)
