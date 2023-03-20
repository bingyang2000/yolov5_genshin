# import os
#
#
# def convert_yolo_format(input_path, output_path, class_dict):
#     with open(input_path, 'r') as f:
#         lines = f.readlines()
#     with open(output_path, 'w') as f:
#         for line in lines:
#             data = line.strip().split()
#             class_name = data[0]
#             class_id = class_dict[class_name]
#             x, y, w, h = map(float, data[1:])
#             x_center = x + w / 2
#             y_center = y + h / 2
#             x_center /= 1.0  # 图像宽度
#             y_center /= 1.0  # 图像高度
#             w /= 1.0  # 图像宽度
#             h /= 1.0  # 图像高度
#             f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")
#
#
# class_dict = {'pt': 0, 'jz': 1, 'hl': 2, 'zg': 3}  # 将类别名映射为类别 ID
# input_path = r'D:\project\DeepStudy\dataset\bx'
# output_path = r'D:\project\DeepStudy\dataset\bx_yolov5'
# convert_yolo_format(input_path, output_path, class_dict)

# import os
#
#
# def batch_convert_yolo_format(input_dir, output_dir, class_dict):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#     for file_name in os.listdir(input_dir):
#         if file_name.endswith('.txt'):
#             input_path = os.path.join(input_dir, file_name)
#             output_path = os.path.join(output_dir, file_name)
#             with open(input_path, 'r') as f:
#                 lines = f.readlines()
#             with open(output_path, 'w') as f:
#                 for line in lines:
#                     data = line.strip().split()
#                     class_name = data[0]
#                     class_id = class_dict[class_name]
#                     x, y, w, h = map(float, data[1:])
#                     x_center = x + w / 2
#                     y_center = y + h / 2
#                     x_center /= 1.0  # 图像宽度
#                     y_center /= 1.0  # 图像高度
#                     w /= 1.0  # 图像宽度
#                     h /= 1.0  # 图像高度
#                     f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")
#
#
# class_dict = {'pt': 0, 'jz': 1, 'hl': 2, 'zg': 3}  # 将类别名映射为类别 ID
# input_dir = r'D:\project\DeepStudy\dataset\bx'
# output_dir = r'D:\project\DeepStudy\dataset\bx_yolov5'
# batch_convert_yolo_format(input_dir, output_dir, class_dict)

import torch
from utils import autoanchor

path = r'data/bx/images/train'
n = 9  # anchor boxes数量
iou_thresh = 0.5  # 用于聚类的IOU阈值
multiplier = 1.0  # k-means聚类时用于缩放的因子
output_file = "anchor.txt"  # 保存生成的anchor boxes的文件路径

anchors = autoanchor.kmean_anchors(path, n=n, iou_thresh=iou_thresh, multiplier=multiplier, output=output_file)
print(anchors)
