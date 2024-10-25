import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
import torch

"""
    用Pillow处理文件夹中的所有图像，添加两个红色虚线矩形框。

    :param folder_path: 输入文件夹路径
    :param rect1: 第一个矩形框的坐标 (x1, y1, x2, y2)
    :param rect2: 第二个矩形框的坐标 (x1, y1, x2, y2)
    :param output_folder: 输出文件夹路径
    :param dash_length: 虚线的间隔长度
    :param line_width: 线条的宽度
"""



def process_images_in_folder(folder_path,  rect1_params, rect2_params, output_folder, line_width, edge_color):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            img = Image.open(input_path)
            draw = ImageDraw.Draw(img)

            # 绘制第一个矩形框
            draw.rectangle(rect1_params, outline='red', width=2)  # width参数控制矩形框边框的厚度

            # 绘制第二个矩形框
            draw.rectangle(rect2_params, outline='red', width=2)

            # 保存图片
            output_path = os.path.join(output_folder, 'DrawBox_' + filename)
            img.save(output_path)



if __name__ == "__main__":
    input_folder = "/home/rtx3080ti/ChangeDetection/Tools/orgin"  # 替换为你的输入文件夹路径
    output_folder = "/home/rtx3080ti/ChangeDetection/Tools/draw"  # 替换为你的输出文件夹路径
    
    line_width = 2
    edge_color = str('red')

    # 设置第一个矩形框的位置和尺寸
    rect1_params = ((50, 50), (70, 80))  # ((左上角x，左上角y),(右下角x，右下角y))
    # 设置第二个矩形框的位置和尺寸
    rect2_params = ((100, 100), (150, 120))

    process_images_in_folder(input_folder, box_1, box_2, output_folder, line_width, edge_color)
    print(f"已完成，图片已保存至 {output_folder}")
