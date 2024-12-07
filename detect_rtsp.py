from ultralytics import YOLO
import cv2
import torch
from collections import Counter

# 检查是否有可用的GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'使用设备: {device}')

# 加载YOLOv5模型并设置置信度阈值
model = YOLO('srickyolov5nu.pt')
model.to(device)
model.conf = 0.2  # 设置置信度阈值为0.2

# RTSP流地址
rtsp_url = "rtsp://172.32.0.93/live/0"

# 打开RTSP流
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("无法连接到摄像头流")
    exit()

# 获取视频流的宽度和高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置显示窗口的大小（宽度和高度减半）
display_width = frame_width // 2
display_height = frame_height // 2

# 创建命名窗口并设置大小
cv2.namedWindow("YOLOv5 Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLOv5 Detection", display_width, display_height)

# 设置视频写入器
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

# 设置跳帧
SKIP_FRAMES = 2
frame_count = 0
paused = False  # 添加暂停标志

print("按 'Q' 键退出程序")
print("按 'P' 键暂停/继续")

def draw_stats(frame, stats):
    # 设置文本参数
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2  # 增大字体大小
    font_thickness = 3  # 增加字体粗细
    padding = 15  # 增加内边距
    line_height = 40  # 增加行高
    
    # 绘制半透明背景
    overlay = frame.copy()
    bg_height = (len(stats) + 1) * line_height + 2 * padding
    bg_width = 300  # 增加背景宽度
    cv2.rectangle(overlay, (0, 0), (bg_width, bg_height), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
    
    # 绘制标题
    cv2.putText(frame, "检测统计:", (padding, line_height), 
                font, font_scale, (255, 255, 255), font_thickness)
    
    # 绘制每个类别的统计
    y = line_height * 2
    for cls, count in stats.items():
        # 确保类名是英文或数字
        text = f"{cls}: {count}"
        cv2.putText(frame, text, (padding, y), 
                   font, font_scale, (255, 255, 255), font_thickness)
        y += line_height
    
    return frame

while True:
    if not paused:
        # 读取一帧
        ret, frame = cap.read()
        if not ret:
            print("无法获取画面")
            break
            
        # 每隔SKIP_FRAMES帧进行一次检测
        if frame_count % SKIP_FRAMES == 0:
            results = model(frame)
            annotated_frame = results[0].plot()
            
            # 统计每个类别的数量
            class_stats = Counter()
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    cls = model.names[int(box.cls)]
                    class_stats[cls] += 1
            
            # 在画面上绘制统计信息
            annotated_frame = draw_stats(annotated_frame, class_stats)
        
        frame_count += 1
        # 显示结果
        cv2.imshow("YOLOv5 Detection", annotated_frame)
        
        # 保存视频帧
        out.write(annotated_frame)
    
    # 键盘控制
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):  # 按Q退出
        print("程序已退出")
        break
    elif key == ord('p') or key == ord('P'):  # 按P暂停/继续
        paused = not paused
        if paused:
            print("视频已暂停，按 'P' 继续")
        else:
            print("视频继续播放")

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows() 