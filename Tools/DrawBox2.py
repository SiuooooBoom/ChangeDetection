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

def draw_box_to_image(input_path, output_path, box_1, box_2, line_width, edge_color):
    image = mpimg.imread(input_path)
    plt.title('Draw Box')
    plt.axis('off')  # 不显示坐标轴
    plt.imshow(image, figsize=(6, 6))
    plt.show()
    # 画第一个矩形框
    x1min, y1min, x1max, y1max = box_1[0], box_1[1], box_1[2], box_1[3]
    width1 = x1max - x1min
    height1 = y1max - y1min
    rect1 = plt.Rectangle((x1min, y1min), width1, height1, linewidth=line_width, edgecolor=edge_color, facecolor='none')
    plt.gca().add_patch(rect1)
    # 画第二个矩形框
    x2min, y2min, x2max, y2max = box_2[0], box_2[1], box_2[2], box_2[3]
    width2 = x2max - x2min
    height2 = y2max - y2min
    rect2 = plt.Rectangle((x2min, y2min), width2, height2, linewidth=line_width, edgecolor=edge_color, facecolor='none')
    plt.gca().add_patch(rect2)
    # 如果需要展示图像可以使用 plt.show()
    plt.show()
    # 保存图像
    # plt.savefig(output_path)


def draw_dashed_rectangle(draw, xy, width, height, dash_length=10, gap_length=10):
    """
    Draw a dashed rectangle.

    :param draw: PIL.ImageDraw.Draw object
    :param xy: Top-left corner of the rectangle as a (x, y) tuple
    :param width: Width of the rectangle
    :param height: Height of the rectangle
    :param dash_length: Length of each dash
    :param gap_length: Length of each gap between dashes
    """
    top_left = xy
    bottom_right = (xy[0] + width, xy[1] + height)

    for side in range(2):  # Iterate over top and bottom sides
        if side == 0:
            start_point = top_left
            end_point = (bottom_right[0], top_left[1])
        else:
            start_point = (top_left[0], bottom_right[1])
            end_point = bottom_right

        current_x = start_point[0]
        while current_x <= end_point[0]:
            draw.rectangle([
                (current_x, start_point[1]),
                (current_x + dash_length, end_point[1])
            ], outline='red', fill=None)
            current_x += dash_length + gap_length


def process_images_in_folder(folder_path, box_1, box_2, output_folder, line_width, edge_color):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            img = Image.open(input_path)
            draw = ImageDraw.Draw(img)

            # 画第一个（虚线）矩形框
            # draw_box_to_image(input_path, output_path, box_1, box_2, line_width, edge_color)
            # draw_dashed_rectangle(draw, rect1_xy, rect1_size[0], rect1_size[1])
            #
            # # 画第二个（虚线）矩形框
            # draw_dashed_rectangle(draw, rect2_xy, rect2_size[0], rect2_size[1])
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

    box_1 = [50, 50, 80, 80]  # 第一个矩形框的坐标 (x1, y1, x2, y2)
    box_2 = [150, 150, 200, 200]  # 第二个矩形框的坐标 (x1, y1, x2, y2)
    line_width = 2
    edge_color = str('red')

    # 设置第一个矩形框的位置和尺寸
    rect1_params = (50, 50, 20, 30)  # (x, y, width, height)
    # 设置第二个矩形框的位置和尺寸
    rect2_params = (100, 100, 50, 80)  # (x, y, width, height)

    process_images_in_folder(input_folder, box_1, box_2, output_folder, line_width, edge_color)
    print(f"已完成，图片已保存至 {output_folder}")
