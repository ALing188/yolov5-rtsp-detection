# YOLOv5 RTSP Detection

基于YOLOv5的RTSP视频流实时目标检测项目，支持实时显示检测结果和对象统计。

## 功能特点

- 支持RTSP视频流实时检测
- 实时显示检测结果和对象统计
- 支持暂停/继续功能（P键）
- 支持视频录制（自动保存为output.avi）
- 可调整显示窗口大小
- 实时统计检测对象数量并显示在左上角
- 支持GPU加速（如果可用）
- 低置信度阈值(0.2)以提高检测灵敏度

## 环境要求

- Python 3.9+
- CUDA支持（推荐，但不是必需）
- 操作系统：Windows/Linux

### 硬件要求
- CPU: 建议Intel i5或更高
- GPU: 建议NVIDIA GPU with CUDA支持
- RAM: 最小8GB，建议16GB
- 摄像头：支持RTSP协议的IP摄像头

## 安装步骤

1. 克隆仓库：
- GPU: 建议NVIDIA GPU with CUDA支持
- RAM: 最小8GB，建议16GB
- 摄像头：支持RTSP协议的IP摄像头

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/ALing188/yolov5-rtsp-detection.git
```
```bash
cd yolov5-rtsp-detection
```
2. 安装依赖：
```bash
pip install -r requirements.txt
```
3. 确保模型文件存在：
- 将训练好的YOLOv5模型文件 `srickyolov5nu.pt` 放在项目根目录

## 使用说明

1. 修改RTSP地址：
在detect_rtsp.py中修改RTSP地址
```python
rtsp_url = "rtsp://your_camera_ip/live/0"
```

2. 运行程序：
```bash
python detect_rtsp.py
```

3. 控制键：
- 'Q' 或 'q': 退出程序
- 'P' 或 'p': 暂停/继续视频流
- 关闭窗口：点击窗口的关闭按钮也可以退出程序

## 输出说明

1. 实时显示：
- 左上角显示检测到的对象类别和数量
- 视频画面中显示检测框和类别标签

2. 保存内容：
- 程序运行时自动保存处理后的视频为 `output.avi`
- 视频包含检测框和统计信息

## 自定义配置

1. 调整显示窗口大小：

修改显示比例（当前为原始大小的一半）
```python
display_width = frame_width // 2
```
```python
display_height = frame_height // 2
```

2. 修改检测灵敏度：

调整置信度阈值（当前为0.2）
```python
model.conf = 0.2 # 值越小，检测越敏感
```

3. 调整跳帧设置：

修改跳帧数（当前为2）
```python
SKIP_FRAMES = 2 # 值越大，处理速度越快但可能错过部分帧
```
## 演示效果

下面是项目的实际运行效果：

![演示视频]([test.gif])

*注：视频显示了实时目标检测和对象统计功能*


## 常见问题

1. 如果出现 "无法连接到摄像头流"：
   - 检查RTSP地址是否正确
   - 确保摄像头在同一网络中
   - 验证摄像头是否支持RTSP协议

2. 如果检测速度较慢：
   - 增加 SKIP_FRAMES 的值
   - 确保GPU可用并正确配置
   - 考虑降低输入分辨率

3. 如果显示窗口太大/太小：
   - 调整 display_width 和 display_height 的值

## 反馈与贡献

- 问题反馈：请在GitHub Issues中提出
- 代码贡献：欢迎提交Pull Request
- 联系方式：[您的联系方式]

## 许可证

MIT License

## 致谢

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- [OpenCV](https://opencv.org/)
