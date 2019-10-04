import cv2
import sys
import os
import numpy as np


def main():
    """
    overwrite color image files with each pixel values
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        print('usage: overwritePixelValuesColor.py <path/to/*.png> ...')
        sys.exit(1)

    os.makedirs('result/overwritePixelValuesColor', exist_ok=True)

    mag = int(32)  # def:16

    for i in range(1, argc):
        im = cv2.imread(argvs[i])
        img = cv2.resize(im, None, fx=mag, fy=mag,
                         interpolation=cv2.INTER_NEAREST)
        font = cv2.FONT_HERSHEY_PLAIN
        font_size = mag / 40
        for i_x in range(im.shape[1]):
            for i_y in range(im.shape[0]):
                pt = np.array([0 + i_x * mag, int(12 * font_size + i_y * mag)])
                pixelvalues = img[pt[1], pt[0]]  # b,g,r
                ptcolor = [int(256 - i) for i in pixelvalues]
                cv2.putText(img, str(pixelvalues[0]),
                            tuple(pt), font, font_size, (ptcolor[0], 0, 0))
                cv2.putText(img, str(pixelvalues[1]),
                            tuple(pt + [0, int(12 * font_size)]), font, font_size, (0, ptcolor[1], 0))
                cv2.putText(img, str(pixelvalues[2]),
                            tuple(pt + [0, int(24 * font_size)]), font, font_size, (0, 0, ptcolor[2]))

        # root, ext = os.path.splitext(argvs[i])
        # cv2.imwrite(root + '_pixelvaluesColor.png', img)

        strImgName = argvs[i].split('/')[-1]
        root, ext = os.path.splitext(strImgName)
        cv2.imwrite('result/overwritePixelValuesColor/PixelValuesColor_' +
                    root + '.png', img)


if __name__ == '__main__':
    main()
