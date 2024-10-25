import cv2
import os

#  图像宽不足裁剪宽度,填充至裁剪宽度
def fill_right(img, size_w):
    size = img.shape
    #  填充值为数据集均值
    img_fill_right = cv2.copyMakeBorder(img, 0, 0, 0, size_w - size[1],
                                        cv2.BORDER_CONSTANT, value = (107, 113, 115))
    return img_fill_right

#  图像高不足裁剪高度,填充至裁剪高度
def fill_bottom(img, size_h):
    size = img.shape
    img_fill_bottom = cv2.copyMakeBorder(img, 0, size_h - size[0], 0, 0,
                                         cv2.BORDER_CONSTANT, value = (107, 113, 115))
    return img_fill_bottom

#  图像宽高不足裁剪宽高度,填充至裁剪宽高度
def fill_right_bottom(img, size_w, size_h):
    size = img.shape
    img_fill_right_bottom = cv2.copyMakeBorder(img, 0, size_h - size[0], 0, size_w - size[1],
                                               cv2.BORDER_CONSTANT, value = (107, 113, 115))
    return img_fill_right_bottom

#  图像切割
#  img_floder 图像文件夹
#  out_img_floder 图像切割输出文件夹
#  size_w 切割图像宽
#  size_h 切割图像高
#  step 切割步长
def image_crop(img_floder, out_img_floder, size_w, size_h, step):
    img_list = os.listdir(img_floder)
    # print(img_list)
    count = 0
    for img_name in img_list:
        number = 0
        # print(img_name)
        #  去除.png后缀
        name = img_name[:-4]
        img = cv2.imread(img_floder + "/" + img_name)
        # print(img_floder )
        cv2.imshow('1',img)
        size = img.shape
        #  若图像宽高大于切割宽高
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
                   cropped = img[start_h : end_h, start_w : end_w]
                   #  用起始坐标来命名切割得到的图像，为的是方便后续标签数据抓取
                   # name_img = name + '_'+ str(start_h) +'_' + str(start_w)
                   name_img = name + '_' + f'{start_h:04d}' + '_' + f'{start_w:04d}'
                   cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
                   number = number + 1
        #  若图像高大于切割高,但宽小于切割宽
        elif size[0] >= size_h and size[1] < size_w:
            # print('图片{}需要在右面补齐'.format(name))
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
               cropped = img0[start_h : end_h, start_w : end_w]
               # name_img = name + '_' + str(start_h) + '_' + str(start_w)
               name_img = name + '_' + f'{start_h:04d}' + '_' + f'{start_w:04d}'
               cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
               number = number + 1
        #  若图像宽大于切割宽,但高小于切割高
        elif size[0] < size_h and size[1] >= size_w:
            count = count + 1
            # print('图片{}需要在下面补齐'.format(name))
            img0 = fill_bottom(img, size_h)
            for w in range(0, size[1] - 1, step):
               start_h = 0
               start_w = w
               end_w = start_w + size_w
               if end_w > size[1]:
                  start_w = size[1] - size_w
                  end_w = start_w + size_w
               end_h = start_h + size_h
               cropped = img0[start_h : end_h, start_w : end_w]
               # name_img = name + '_'+ str(start_h) +'_' + str(start_w)
               name_img = name + '_' + f'{start_h:04d}' + '_' + f'{start_w:04d}'
               cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
               number = number + 1
        #  若图像宽高小于切割宽高
        elif size[0] < size_h and size[1] < size_w:
            count = count + 1
            # print('图片{}需要在下面和右面补齐'.format(name))
            img0 = fill_right_bottom(img,  size_w, size_h)
            cropped = img0[0 : size_h, 0 : size_w]
            name_img = name + '_'+ '0000' +'_' + '0000'
            cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
            number = number + 1
        # print('{}.png切割成{}张.'.format(name,number))
    # print('共完成{}张图片'.format(count))

if __name__ == "__main__":
    #  图像数据集文件夹
    img_floder = r'/home/rtx3080ti/ChangeDetection/Tools/image'
    #  切割得到的图像数据集存放文件夹
    out_img_floder = r'/home/rtx3080ti/ChangeDetection/Tools/new'
    #  切割图像宽
    size_w = 256
    #  切割图像高
    size_h = 256
    #  切割步长,重叠度为size_w - step
    step = 256
    image_crop(img_floder, out_img_floder, size_w, size_h, step)
    print('裁切完成')