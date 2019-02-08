import cv2
import sys
import os


def main():
    """
    convert image files to png files
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        print('usage: convert2png.py <path/to/*.ppm> ...')
        sys.exit(1)

    for i in range(1, argc):
        img = cv2.imread(argvs[i])
        root, ext = os.path.splitext(argvs[i])
        cv2.imwrite(root + '.png', img)


if __name__ == '__main__':
    main()
