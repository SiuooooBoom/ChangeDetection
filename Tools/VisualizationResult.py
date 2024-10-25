from PIL import Image, ImageOps
import os
import cv2



def compare_images(image_label_folder, image_predict_folder, output_vis_result_folder):
    img_list = os.listdir(image_label_folder)
    for img_name in img_list:
        img_label_path = os.path.join(image_label_folder, img_name)
        image_predict_path = os.path.join(image_predict_folder, img_name)
        output_vis_result_path = os.path.join(output_vis_result_folder, img_name)

        # 打开图片A和B
        image_label = Image.open(img_label_path).convert('RGB')
        image_predict = Image.open(image_predict_path).convert('RGB')

        # 确保两张图片的分辨率相同
        if image_label.size != image_predict.size:
            raise ValueError("The two images do not have the same resolution.")

        # 创建一个新的与A和B相同分辨率的图片C
        width, height = image_label.size
        image_vis_result = Image.new('RGB', (width, height))
        pixels_vis_result = image_vis_result.load()

        # 遍历每个像素进行比较
        for x in range(width):
            for y in range(height):
                pixel_label = image_label.getpixel((x, y))
                pixel_predict = image_predict.getpixel((x, y))

                if pixel_label == pixel_predict:
                    pixels_vis_result[x, y] = pixel_label
                elif pixel_label == (255, 255, 255) and pixel_predict == (0, 0, 0):  # false negative
                    pixels_vis_result[x, y] = (0, 255, 0)  # 假阳性，标记为绿色
                elif pixel_label == (0, 0, 0) and pixel_predict == (255, 255, 255):  # false positive
                    pixels_vis_result[x, y] = (255, 0, 0)  # 假阴性，标记为红色
                else:
                    # 如果不满足以上条件，可以设置为任意颜色，这里设置为灰色作为示例
                    # 你也可以根据需要设置为其他颜色或保留其中一个图片的像素值
                    pixels_vis_result[x, y] = (0, 0, 255)  # 蓝色

        # 保存新的图片C
        image_vis_result.save(output_vis_result_path)
    print(f"The output image has been saved to {output_vis_result_folder}")

if __name__ == "__main__":
    # 使用示例
    image_label_folder = '/home/rtx3080ti/ChangeDetection/Tools/label'
    image_predict_folder = '/home/rtx3080ti/ChangeDetection/Tools/predict'
    output_vis_result_folder = '/home/rtx3080ti/ChangeDetection/Tools/vis_result'
    compare_images(image_label_folder, image_predict_folder, output_vis_result_folder)