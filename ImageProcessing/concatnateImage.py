import cv2
import sys
# import os
# import numpy as np


def main():
    """
    concatnate image files
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        print('usage: concatnateImage.py <path/to/*.png> ...')
        sys.exit(1)

    im_list = []
    for i in range(1, argc):
        im_list.append(cv2.imread(argvs[i]))

    w_min = min(im.shape[1] for im in im_list)

    im_list_resize = [cv2.resize(
        im, (w_min, int(im.shape[0] * w_min / im.shape[1]))) for im in im_list]

    outputimg = cv2.vconcat(im_list_resize)
    cv2.imwrite('output.png', outputimg)


if __name__ == '__main__':
    main()
