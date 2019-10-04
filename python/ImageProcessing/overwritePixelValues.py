import cv2
import sys
import os


def main():
    """
    overwrite grayscale image files with each pixel values
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        print('usage: overwritePixelValues.py <path/to/*.png> ...')
        sys.exit(1)

    os.makedirs('result/overwritePixelValues', exist_ok=True)

    mag = int(32)  # def:16

    for i in range(1, argc):
        im = cv2.imread(argvs[i], cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(im, None, fx=mag, fy=mag,
                         interpolation=cv2.INTER_NEAREST)
        font = cv2.FONT_HERSHEY_PLAIN
        font_size = mag / 32
        for i_x in range(im.shape[1]):
            for i_y in range(im.shape[0]):
                pt = (0 + i_x * mag, int(12 * font_size + i_y * mag))
                pixelvalue = img[pt[1], pt[0]]  # grayscale
                ptcolor = int(256 - pixelvalue)
                cv2.putText(img, str(pixelvalue),
                            pt, font, font_size, ptcolor)

        # root, ext = os.path.splitext(argvs[i])
        # cv2.imwrite(root + '_pixelvalues.png', img)

        strImgName = argvs[i].split('/')[-1]
        root, ext = os.path.splitext(strImgName)
        cv2.imwrite('result/overwritePixelValues/PixelValues_' +
                    root + '.png', img)


if __name__ == '__main__':
    main()
