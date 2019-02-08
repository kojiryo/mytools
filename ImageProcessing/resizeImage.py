import cv2
import sys
import os


def main():
    """
    resize image files
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc <= 2:
        print('usage: resizeImage.py <scale> <path/to/*.png> ...')
        sys.exit(1)

    scale = float(argvs[1])

    for i in range(2, argc):
        im = cv2.imread(argvs[i])
        img = cv2.resize(im, None, fx=scale, fy=scale)
        root, ext = os.path.splitext(argvs[i])
        cv2.imwrite(root + '.png', img)


if __name__ == '__main__':
    main()
