
import cv2
import sys
import os


def main():
    """
    convert image files to 8 bit image
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc <= 2:
        print(
            'usage: convertto8BitImage.py <height[pixel]> <path/to/*.png> ...')
        sys.exit(1)

    height = int(argvs[1])

    os.makedirs('result/convertto8BitImage', exist_ok=True)

    for i in range(2, argc):
        im = cv2.imread(argvs[i])
        # im = cv2.imread(argvs[i], 0) #grayscale
        img = cv2.resize(im, (int(
            im.shape[1] * height / im.shape[0]), height), interpolation=cv2.INTER_NEAREST)

        # root, ext = os.path.splitext(argvs[i])
        # cv2.imwrite(root + '_resize.png', img)

        strImgName = argvs[i].split('/')[-1]
        root, ext = os.path.splitext(strImgName)
        cv2.imwrite('result/convertto8BitImage/8BitH' +
                    str(height) + '_' + root + '.png', img)


if __name__ == '__main__':
    main()
