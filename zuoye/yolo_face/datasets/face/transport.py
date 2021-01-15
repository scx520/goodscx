#  outputs 01.xml  ......  18.xml
#  labels  1.txt   ......  18.txt
# 生成labels文件夹   写入1.txt文件   {1}.xml-txt
# 1.txt内容：类别下标（0,1,2,3） c_x   c_y       w       h 归一化
# 1.xml      类别单词          x_min  y_min    x_max   y_max
import os
import xml.dom.minidom
names = {
    "yang":0,
    "cat":1,
    "qiang":2,
    "person":3,
    "woman":4,
    "scx":5,
    "scy":6,
    "dog":7
}

def format_label(xml_file,out_path):
    # xml文件的路径   输出文件的文件夹
    # .....outputs/01.xml              labels/01.txt
    file_name = os.path.basename(xml_file)# 01.xml
    only_name = file_name.split(".")  # 截成两部分，[‘01’，‘xml’]
    # 输出的完整路径
    out_file = os.path.join(out_path,F"{int(only_name[0])}.txt")

    # xml_file        out_file 两个完整路径
    with open(xml_file) as fd:#打开文件读内容
        dom = xml.dom.minidom.parse(xml_file)
        root = dom.documentElement
        # 图像宽 高
        img_w = root.getElementsByTagName('width')[0].firstChild.data
        img_h = root.getElementsByTagName('height')[0].firstChild.data
        # 标注目标
        objects = root.getElementsByTagName('object')
        # 打开out_file文件  "w" "r" "a"
        out_fd = open(out_file,"a")
        for obj in objects:
            name = root.getElementsByTagName('name')[0].firstChild.data #名
            xmin = root.getElementsByTagName('xmin')[0].firstChild.data
            ymin = root.getElementsByTagName('ymin')[0].firstChild.data
            xmax = root.getElementsByTagName('xmax')[0].firstChild.data
            ymax = root.getElementsByTagName('ymax')[0].firstChild.data
            name = names[name]  #0
            # 目标的宽高 中心点
            w = float(float(xmax) - float(xmin))
            h = float(float(ymax) - float(ymin))
            xcenter = float(xmin) + w/2
            ycenter = float(ymin) + h/2
            # 归一化
            w = w/float(img_w)
            h = h/float(img_h)
            xcenter = xcenter/float(img_w)
            ycenter = ycenter/float(img_h)
            # name xcenter ycenter w h
            # 写入
            out_fd.write(F"{name} {xcenter:.6f} {ycenter:.6f} {w:.6f} {h:.6f}")
        out_fd.close()
        print(F"完成{xml_file}转换")
#输入路径，输出路径
def to_yolo(in_path,out_path):
    # 判断输出路径是否存在  不存在新建文件夹
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    # 遍历输入路径 获取所有*.xml
    all_xml_files = os.listdir(in_path)
    for xml_file in all_xml_files:
        # 01.xml
        # 拼接操作稳健的完整路径
        path_file = os.path.join(in_path,xml_file)
        format_label(path_file,out_path)

to_yolo("C:\\Users\\Administrator\\Desktop\\yolo_face\\datasets\\face\\outputs","C:\\Users\\Administrator\\Desktop\\yolo_face\\datasets\\face\\labels")