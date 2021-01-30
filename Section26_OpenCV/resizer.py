import cv2
import glob


def disp_img(image):
    cv2.imshow("Resized to 100 X 100", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(image):
    img = cv2.imread(image, 0)
    resized_image = cv2.resize(img, (100, 100))
    disp_img(resized_image)
    return resized_image


images = glob.glob("*.jpg")

for image in images:
    cv2.imwrite("resized_" + image, resize(image))
