import cv2
import matplotlib.pyplot as plt

def display_image(img, title="Img"):
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()

def get_image_path():
    return input("Rasm manzilini kiriting (masalan, C:\\Users\\user\\Desktop\\rasm.png), : ")

image_path = get_image_path()
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Kiritilgan rasm manzili to'g'ri emas yoki rasm topilmadi.")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_image(image, "Asl Rasm")

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    display_image(binary, "Binar Rasm")

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = image.copy()
    cv2.drawContours(output, contours, -1, (255, 37, 34), 2)
    display_image(output, "Kontur Chizilgan Rasm")
