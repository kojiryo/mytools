import cv2
import sys
import os


def main():
    """
    resize image files by height
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc <= 3:
        print(
            'usage: resizeImageByHeight.py <height[pixel]> <path/to/*.png> ...')
        sys.exit(1)

    height = int(argvs[1])

    for i in range(2, argc):
        im = cv2.imread(argvs[i])
        img = cv2.resize(im, (int(im.shape[1] * height / im.shape[0]), height))
        root, ext = os.path.splitext(argvs[i])
        cv2.imwrite(root + '.png', img)


if __name__ == '__main__':
    main()
