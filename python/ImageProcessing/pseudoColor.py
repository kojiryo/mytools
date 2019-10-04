# import numpy as np
import cv2
# import copy

colormap_table_count = 0
COLORMAP_TABLE = [
    ['COLORMAP_AUTUMN',  cv2.COLORMAP_AUTUMN],
    ['COLORMAP_JET',     cv2.COLORMAP_JET],
    ['COLORMAP_WINTER',  cv2.COLORMAP_WINTER],
    ['COLORMAP_RAINBOW', cv2.COLORMAP_RAINBOW],
    ['COLORMAP_OCEAN',   cv2.COLORMAP_OCEAN],
    ['COLORMAP_SUMMER',  cv2.COLORMAP_SUMMER],
    ['COLORMAP_SPRING',  cv2.COLORMAP_SPRING],
    ['COLORMAP_COOL',    cv2.COLORMAP_COOL],
    ['COLORMAP_HSV',     cv2.COLORMAP_HSV],
    ['COLORMAP_PINK',    cv2.COLORMAP_PINK],
    ['COLORMAP_HOT',     cv2.COLORMAP_HOT]
]

video_input = cv2.VideoCapture(0)

while True:
    ret, frame = video_input.read()

    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    apply_color_map_image = cv2.applyColorMap(
        grayscale_image, COLORMAP_TABLE[colormap_table_count % len(COLORMAP_TABLE)][1])

    cv2.putText(apply_color_map_image, COLORMAP_TABLE[colormap_table_count % len(
        COLORMAP_TABLE)][0], (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)
    cv2.imshow('apply_color_map_image', apply_color_map_image)

    k = cv2.waitKey(50) & 0xff
    if k == 110:  # N
        colormap_table_count = colormap_table_count + 1
    if k == 27:  # ESC
        break

video_input.release()
cv2.destroyAllWindows()
