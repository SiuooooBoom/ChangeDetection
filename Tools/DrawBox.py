import os
import torch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

# 假设 ca_map 是一个 32x32 的张量，值在 0 到 1 之间
ca_map = torch.rand((32, 32))


# 假设 bbox 是一个包含 (xmin, ymin, xmax, ymax) 的张量
bbox = torch.tensor([5, 5, 20, 20])

# 将张量转换为 numpy 数组以便于使用 matplotlib 处理
ca_map_np = ca_map.numpy()

# 创建一个图像
plt.figure(figsize=(6, 6))
plt.imshow(ca_map_np, cmap='viridis', interpolation='nearest')
plt.colorbar()  # 添加颜色条用于指示颜色值范围
plt.title("Visualized CA Map with Bounding Box")

# 绘制边界框
xmin, ymin, xmax, ymax = bbox.numpy()
width = xmax - xmin
height = ymax - ymin
rect = plt.Rectangle((xmin, ymin), width, height, linewidth=2, edgecolor='red', facecolor='none')
plt.gca().add_patch(rect)

# 保存图像
plt.savefig("ca_map_with_bbox.png")

# 如果需要展示图像可以使用 plt.show()
# plt.show()

if __name__ == "__main__":
    #  图像数据集文件夹（输入文件夹）
    img_folder = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/label'
    #  切画框后生成的图像存放文件夹（输出文件夹）
    out_img_folder = r'/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/label'
    #  切割后的图像宽（预设参数）
    size_w = 256
    #  切割后的图像高（预设参数2）
    size_h = 256
    #  切割步长,重叠度为size_w - step（预设参数3）
    step = 256
    image_crop(img_folder, out_img_folder, size_w, size_h, step)

