import os

import cv2


def decode_image(image_path: str) -> str:
    assert os.path.isfile(image_path), f"Image file not found: {image_path}"
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use OpenCV to decode the QR code
    detector = cv2.QRCodeDetector()
    val, _, _ = detector.detectAndDecode(gray)

    val if val else "QR code could not be decoded."

    return val


def main():
    value = decode_image("./data/image.png")
    print(value)


if __name__ == "__main__":
    main()
