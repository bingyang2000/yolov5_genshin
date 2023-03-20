"python train.py --data models/config/data.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --device 0 --epoch 125 --batch-size 16 --img-size 256"
import train

if __name__ == '__main__':
    train.run(data="models/config/data.yaml", cfg="models/yolov5s.yaml", weights="yolov5s.pt", device="0",
              epochs=125, batch_size=16, img_size=640)  # 调用train.py中的run()函数进行训练
