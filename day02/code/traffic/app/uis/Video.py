class Video(QThread):
    def __init__(self):
        super(Video,self).__init__()
        # 获取摄像头 第0个摄像头
        self.dev = 