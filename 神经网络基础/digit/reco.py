from lenet import LeNet5
import torch

net = LeNet5()

# 保证保存时对应
state = torch.load('./lenet1111.pth')
net.load_state_dict(state)

print(net)




import cv2
img = cv2.imread('./1.jpg') # 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 
img = cv2.resize(img,(28,28)) # 28*28
img = torch.Tensor(img).view(1,1,img.shape[0],img.shape[1]) #1 1 w h



print(img)
y_ = net(img)
print(y_)
predict = torch.argmax(y_,dim=0)
print(predict.numpy())