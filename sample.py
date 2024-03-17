import cv2

def main():
    img = cv2.imread("img/tare2.png")
    img2 = cv2.resize(img, (300, 200))
    cv2.imshow("Tare", img2)
    k = cv2.waitKey(0)

if __name__ == "__main__":
    main()