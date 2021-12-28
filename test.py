from utils.plots import Annotator, colors
# from utils.general import (scale_coords)
import cv2
import numpy as np

path = 'data/images/zidane.jpg'
im0 = cv2.imread(path)
print(type(im0), im0.shape)

annotator = Annotator(im0, line_width=2, pil=not ascii)

# if det is not None and len(det):
#     # Rescale boxes from img_size to im0 size
#     det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

#     xyxy = det[:, 0:4]
#     confs = det[:, 4]
#     clss = det[:, 5]

#     inplace_counter = 0
#     # draw boxes for visualization
#     if len(det) > 0:
#         for j, (bbox, cls, conf) in enumerate(zip(xyxy.cpu(), clss.cpu(), confs.cpu())):

#             c = int(cls)  # integer class
#             label = f'{names[c]} {conf:.2f}'
#             annotator.box_label(bbox, label, color=colors(c, True))

#             # # check for boxes in given range
#             # if mask:
#             #     # if bbox in region:
#             #     #     inplace_counter+=1
#             #     pass
#         # if mask:
    
annotator.text([0,0], f'{0} people in a target region')

# Stream results
im0 = annotator.result()

cv2.namedWindow('imageWindow')
cv2.imshow('imageWindow', im0)
wait = True
while wait:
    wait = cv2.waitKey()=='q113' # hit q to exit