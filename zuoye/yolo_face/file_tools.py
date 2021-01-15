import os# 一个自动写路径到txt文件的脚本
import numpy as np

def create_image_list(src_path, dst_path, filename):
    """
            函数功能主要把一个目录下的图像文件名归档为一个文本文件。
            src_path：需要归档的图像所在目录
            dst_path：产生的归档文本文件的目录
            filename：产生的归档文件名
    """
    # 返回文件列表
    files = os.listdir(src_path)
    # 遍历处理文件名，产生清单
    with open(os.path.join(dst_path, filename),"w") as fd:
            for file in files:
                fd.write(os.path.join(src_path, file))
                fd.write("\n")

if __name__ == "__main__":
    # 图像所在目录：datasets/coco128/images/train2017
    # 归档文本文件存放目录：datasets
    # 归档文件名：train.txt
    create_image_list("datasets/face/images", "datasets", "train.txt")