# 层
# 线性层（全连接层） 堆叠多个线性层 不能帮助神经网络学习新的东西 
# 非线性激活函数
# 卷积层

#基于解决的问题确定最后一层
# 1 回归问题 输出线性层
# 2 二分类 使用sigmoid函数
# 3 多分类 输出线性层 然后使用类（softmax）函数输出给定数量的样例的概率  和为1
# 损失函数
# 回归问题 均方误差函数
# 分类问题 交叉熵损失函数

# 数据集
# 目录结构必须遵守固定规则
# 第三方框架的处理[]

import loader
import torch
import torch.utils.data
from lenet import LeNet5

# 读取训练数据集
# 图片
train_x = loader.load_image_fromfile('data/train-images.idx3-ubyte') 
train_y = loader.load_label_fromfile('data/train-labels.idx1-ubyte') 
print(train_x.shape)# N H W
print(train_y.shape) 

# 读取测试数据集
# 图片
test_x = loader.load_image_fromfile('data/t10k-images.idx3-ubyte') 
test_y = loader.load_label_fromfile('data/t10k-labels.idx1-ubyte') 
print(test_x.shape)
print(test_y.shape)

x = torch.Tensor(train_x).view(train_x.shape[0],1,train_x.shape[1],train_x.shape[2])
y = torch.LongTensor(train_y)

t_x = torch.Tensor(test_x).view(test_x.shape[0],1,test_x.shape[1],test_x.shape[2])
t_y = torch.LongTensor(test_y)

# 使用torch封装数据
train_dataset = torch.utils.data.TensorDataset(x,y)
test_dataset = torch.utils.data.TensorDataset(t_x,t_y)

# 数据随机加载 按批切分   （数据加载器）
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,shuffle=True,batch_size=2000)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,shuffle=True,batch_size=10000)


# 训练模型
# 模型          
model = LeNet5()  # model.foward() ==>正确的模型使用 model(input)
params = model.parameters()

# 损失函数
cri = torch.nn.CrossEntropyLoss()

# 优化器 学习率
opt = torch.optim.Adam(model.parameters(),lr=0.001)

# 训练轮数
epoch = 2

for e in range(epoch):
    # 1轮 整个训练数据集 学习一次
    print(F"第{e+1:02d}轮")
    for data,target in train_loader:
        #1 批
        # print(data.shape)
        # print(target.shape)
        # 批处理
        # 批梯度下降 权重更新

        #导数清零 
        opt.zero_grad()
        # 使用模型预测
        out = model(data)
        # out target  计算损失
        loss = cri(out,target)
        # 求导
        loss.backward()
        # 更新权重
        opt.step()


    #计算准确率 e % 100==0
    with torch.no_grad():
         for data,target in test_loader:
             y_ = model(data)
             predict = torch.argmax(y_,dim=1)
             c_rate = (predict == target).float().mean()
             print(F"准确率：{c_rate*100:5.2f}%")
    #保存模型 整个网络结构和参数  torc.load()
    # torch.save(model,"lenet.pth") 

    torch.save(model.state_dict(),"lenet1111.pth")  #整个参数 二进制保存有自己特殊的规则

    # 可视化在线工具 查看模型 结构  https://netron.app/
        


