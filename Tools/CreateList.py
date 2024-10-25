import os

def get_image_files(directory, extensions):
    """
    获取指定目录下的所有图片文件名
    :param directory: 文件夹路径
    :param extensions: 图片文件扩展名的列表
    :return: 图片文件名的列表
    """
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(file)
    return image_files


def write_filenames_to_txt(filenames, output_file):
    """
    将文件名列表写入文本文件
    :param filenames: 文件名列表
    :param output_file: 输出文本文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for filename in filenames:
            f.write(filename + '\n')


def main():
    # 指定文件夹路径
    directory = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/A'  # 替换为你的文件夹路径

    # 图片文件扩展名
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # 输出文本文件路径
    output_file = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/list/train.txt'

    # 获取图片文件名
    image_files = get_image_files(directory, extensions)

    # 写入文本文件
    write_filenames_to_txt(image_files, output_file)

    print(f"已将 {len(image_files)} 个图片文件名写入 {output_file}")


if __name__ == "__main__":
    main()