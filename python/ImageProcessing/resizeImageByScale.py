import cv2
import sys
import os


def main():
    """
    resize image files by scale
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc <= 2:
        print('usage: resizeImageByScale.py <scale> <path/to/*.png> ...')
        sys.exit(1)

    scale = float(argvs[1])

    os.makedirs('result/resizeImageByScale', exist_ok=True)

    for i in range(2, argc):
        im = cv2.imread(argvs[i])
        img = cv2.resize(im, None, fx=scale, fy=scale)

        # root, ext = os.path.splitext(argvs[i])
        # cv2.imwrite(root + '_resize.png', img)

        strImgName = argvs[i].split('/')[-1]
        cv2.imwrite('result/resizeImageByScale/S' +
                    str(scale) + '_' + strImgName, img)


if __name__ == '__main__':
    main()
