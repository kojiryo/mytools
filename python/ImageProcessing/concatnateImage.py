import cv2
import sys
import os


def main():
    """
    concatnate image files
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        print('usage: concatnateImage.py <path/to/*.png> ...')
        sys.exit(1)

    os.makedirs('result/concatnateImage', exist_ok=True)

    im_list = []
    for i in range(1, argc):
        im_list.append(cv2.imread(argvs[i]))

    w_min = min(im.shape[1] for im in im_list)

    im_list_resize = [cv2.resize(
        im, (w_min, int(im.shape[0] * w_min / im.shape[1]))) for im in im_list]
    img = cv2.vconcat(im_list_resize)

    # cv2.imwrite('concatImage.png', img)

    strImgName = argvs[1].split('/')[-1]
    root, ext = os.path.splitext(strImgName)
    cv2.imwrite('result/concatnateImage/Concat_' + root + '.png', img)


if __name__ == '__main__':
    main()
