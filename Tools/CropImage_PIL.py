import os
import PIL
from PIL import Image, ImageOps, ImageFile
import cv2
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

"""因为opencv读图有时错误地将8位单通道的标签图片也切割并保存为24位三通道的了，因此改用PIL将数据集中的大图切割成小图。"""

#  图像宽不足裁剪宽度,填充至裁剪宽度
def fill_right(img, size_w):
    size = img.size
    #  填充值为全黑，像素值0
    img_fill_right = ImageOps.expand(img, border=(0, 0, 0, size_w - size[1]), fill=0)
    return img_fill_right

#  图像高不足裁剪高度,填充至裁剪高度
def fill_bottom(img, size_h):
    size = img.size
    img_fill_bottom = ImageOps.expand(img, border=(0, 0, 0, size_h - size[0]), fill=0)
    return img_fill_bottom

#  图像宽高不足裁剪宽高度,填充至裁剪宽高度
def fill_right_bottom(img, size_w, size_h):
    size = img.size
    img_fill_right_bottom = ImageOps.expand(img, border=(0, 0, size_w - size[1], size_h - size[0]), fill=0)
    return img_fill_right_bottom

#  图像切割[img_folder: 图像文件夹],[out_img_folder:图像切割输出文件夹],[size_w: 切割图像宽],[size_h: 切割图像高],[step: 切割步长]
def image_crop(img_folder, out_img_folder, size_w, size_h, step):
    img_list = os.listdir(img_folder)
    # print(img_list)
    count = 0
    for img_name in img_list:
        number = 0
        name = img_name[:-4]  # 去除.png后缀
        img_path = os.path.join(img_folder, img_name)
        img = Image.open(img_path)
        size = img.size
        #  若图像宽高大于切割宽高（正常情况）
        if size[0] >= size_h and size[1] >= size_w:
           count = count + 1
           for h in range(0, size[0] - 1, step):
               start_h = h
               for w in range(0, size[1] - 1, step):
                   start_w = w
                   end_h = start_h + size_h
                   if end_h > size[0]:
                      start_h = size[0] - size_h
                      end_h = start_h + size_h
                   end_w = start_w + size_w
                   if end_w > size[1]:
                      start_w = size[1] - size_w
                   end_w = start_w + size_w
                   name_img = name + '_' + f'{start_h:04d}' + '_' + f'{start_w:04d}'
                   new_img = img.crop((start_w, start_h, end_w, end_h))
                   new_img_filename = '{}/{}.png'.format(out_img_folder, name_img)
                   new_img.save(new_img_filename)
                   number = number + 1
        #  若图像高大于切割高,但宽小于切割宽
        elif size[0] >= size_h and size[1] < size_w:
            print('图片{}需要在右面补齐'.format(name))
            count = count + 1
            img0 = fill_right(img, size_w)
            for h in range(0, size[0] - 1, step):
               start_h = h
               start_w = 0
               end_h = start_h + size_h
               if end_h > size[0]:
                  start_h = size[0] - size_h
                  end_h = start_h + size_h
               end_w = start_w + size_w
               name_img = name + '_' + f'{start_h:04d}' + '_' + f'{start_w:04d}'
               new_img = img0.crop((start_w, start_h, end_w, end_h))
               new_img_filename = '{}/{}.png'.format(out_img_folder, name_img)
               new_img.save(new_img_filename)
               number = number + 1
        #  若图像宽大于切割宽,但高小于切割高
        elif size[0] < size_h and size[1] >= size_w:
            count = count + 1
            print('图片{}需要在下面补齐'.format(name))
            img0 = fill_bottom(img, size_h)
            for w in range(0, size[1] - 1, step):
               start_h = 0
               start_w = w
               end_w = start_w + size_w
               if end_w > size[1]:
                  start_w = size[1] - size_w
                  end_w = start_w + size_w
               end_h = start_h + size_h
               name_img = name + '_' + f'{start_h:04d}' + '_' + f'{start_w:04d}'
               new_img = img0.crop((start_w, start_h, end_w, end_h))
               new_img_filename = '{}/{}.png'.format(out_img_folder, name_img)
               new_img.save(new_img_filename)
               number = number + 1
        #  若图像宽高小于切割宽高
        elif size[0] < size_h and size[1] < size_w:
            count = count + 1
            print('图片{}需要在下面和右面补齐'.format(name))
            img0 = fill_right_bottom(img,  size_w, size_h)
            name_img = name + '_' + '0000' + '_' + '0000'
            new_img = img0.crop((0, 0, size_w, size_h))
            new_img_filename = '{}/{}.png'.format(out_img_folder, name_img)
            new_img.save(new_img_filename)
            number = number + 1
    print('裁切完成')

if __name__ == "__main__":
    #  图像数据集文件夹（输入文件夹）
    img_folder = '/home/rtx3080ti/ChangeDetection/Tools/1'
    #  切割得到的图像数据集存放文件夹（输出文件夹）
    out_img_folder = r'/home/rtx3080ti/ChangeDetection/Tools/2'
    #  切割后的图像宽（预设参数1）
    size_w = 256
    #  切割后的图像高（预设参数2）
    size_h = 256
    #  切割步长,重叠度为size_w - step（预设参数3）
    step = 256
    image_crop(img_folder, out_img_folder, size_w, size_h, step)

