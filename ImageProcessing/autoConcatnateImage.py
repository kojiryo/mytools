import cv2
import sys
import os
# import numpy as np


def main():
    """
    concatnate each sequence image files from Dataset
    """
    argvs = sys.argv
    argc = len(argvs)
    if argc == 1:
        print('usage: autoConcatnateImage.py <path/to/Dataset/> ...')
        sys.exit(1)
    else:
        if argvs[1].endswith('/') is False:
            argvs[1] += '/'
        print('Dataset path=\n', argvs[1])

    strRootName = argvs[1].split('/')[-2]
    os.makedirs('concatimagesfrom"' + strRootName + '"', exist_ok=True)

    files = sorted(os.listdir(argvs[1]))
    # print(files)
    strDirName_list = [f for f in files if os.path.isdir(
        os.path.join(argvs[1], f))]
    print('sequence image directory=\n', strDirName_list)

    for strDirName in strDirName_list:

        im_list = []

        objects = sorted(os.listdir(argvs[1] + strDirName))
        # print(objects)
        strImgName_list = [o for o in objects if os.path.isfile(
            os.path.join(argvs[1], strDirName, o))]
        # print(strImgName_list)
        for strImgName in strImgName_list:
            if cv2.imread(os.path.join(argvs[1], strDirName, strImgName)) is not None:
                im_list.append(cv2.imread(os.path.join(
                    argvs[1], strDirName, strImgName)))
                # print(strImgName)

        # print(im_list)

        width_min = min(im.shape[1] for im in im_list)

        im_list_resize = [cv2.resize(
            im, (width_min, int(im.shape[0] * width_min / im.shape[1]))) for im in im_list]

        outputimg = cv2.vconcat(im_list_resize)
        cv2.imwrite('concatimagesfrom"' + strRootName +
                    '"/' + strDirName + '.png', outputimg)


if __name__ == '__main__':
    main()
