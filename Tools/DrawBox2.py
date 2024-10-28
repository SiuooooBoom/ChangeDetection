import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

"""
    用Pillow处理文件夹中的所有图像，添加两个红色虚线矩形框。
    :param input_folder: 输入文件夹路径
    :param box1_params1: 第一个矩形框的坐标 ((左上角x,左上角y),(右下角x,右下角y))
    :param box1_params2: 第二个矩形框的坐标 ((左上角x,左上角y),(右下角x,右下角y))
    :param output_folder: 输出文件夹路径
"""

def process_images_in_folder(input_folder, box1_params, box2_params, output_folder,):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)

            # 按照彩色图的方式读取每一张图片
            img = Image.open(input_path).convert('RGB')
            draw = ImageDraw.Draw(img)

            # 绘制第一个矩形框
            draw.rectangle(box1_params, outline='red', width=2)
            # 绘制第二个矩形框
            draw.rectangle(box2_params, outline='red', width=2)

            # 保存图片
            output_path = os.path.join(output_folder, 'DrawBox_' + filename)
            img.save(output_path)
    return

if __name__ == "__main__":
    # 输入文件夹路径
    input_folder = "/home/rtx3080ti/ChangeDetection/Tools/orgin"
    # 输出文件夹路径
    output_folder = "/home/rtx3080ti/ChangeDetection/Tools/draw"

    # 设置第一个矩形框的位置和尺寸
    box1_params = ((50, 50), (70, 80))      # ((左上角x,左上角y),(右下角x,右下角y))
    # 设置第二个矩形框的位置和尺寸
    box2_params = ((100, 100), (150, 120))  # ((左上角x,左上角y),(右下角x,右下角y))

    process_images_in_folder(input_folder, box1_params, box2_params, output_folder)
    print(f"已完成，图片已保存至 {output_folder}")
