import os

def process_file(input_file):
    test_lines = []
    train_lines = []
    val_lines = []

    # 打开并读取输入文件
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # 去除每行末尾的换行符
            if line.startswith('test'):
                test_lines.append(line)
            elif line.startswith('train'):
                train_lines.append(line)
            elif line.startswith('val'):
                val_lines.append(line)

   # 将test行的内容写入test.txt文件
    with open(output_file_test, 'w', encoding='utf-8') as test_file:
        for line in test_lines:
            test_file.write(line + '\n')

    # 将train行的内容写入train.txt文件
    with open(output_file_train, 'w', encoding='utf-8') as train_file:
        for line in train_lines:
            train_file.write(line + '\n')

    # 将val行的内容写入val.txt文件
    with open(output_file_val, 'w', encoding='utf-8') as val_file:
        for line in val_lines:
            val_file.write(line + '\n')

if __name__ == "__main__":
    # 输入文件名
    input_file = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/list/all.txt'
    # 输出文件名
    output_file_train = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/list/train.txt'
    output_file_test = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/list/test.txt'
    output_file_val = '/home/rtx3080ti/ChangeDetection/Dataset/LEVIR-CD/1_Crop/list/val.txt'

    process_file(input_file)
    print('已完成！')
