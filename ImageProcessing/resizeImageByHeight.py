import cv2
import sys
import os


def main():
    """
    resize image files by height
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc <= 2:
        print(
            'usage: resizeImageByHeight.py <height[pixel]> <path/to/*.png> ...')
        sys.exit(1)

    height = int(argvs[1])

    os.makedirs('result/resizeImageByHeight', exist_ok=True)

    for i in range(2, argc):
        im = cv2.imread(argvs[i])
        img = cv2.resize(im, (int(im.shape[1] * height / im.shape[0]), height))

        # root, ext = os.path.splitext(argvs[i])
        # cv2.imwrite(root + '_resize.png', img)

        strImgName = argvs[i].split('/')[-1]
        cv2.imwrite('result/resizeImageByHeight/H'
                    + str(height) + '_' + strImgName, img)


if __name__ == '__main__':
    main()
