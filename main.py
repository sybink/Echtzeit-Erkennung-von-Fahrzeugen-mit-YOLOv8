from ultralytics import YOLO

# # Load a model
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
model = YOLO("runs/detect/train6/weights/best.pt")  # Load a pretrained model (use your model path)
if __name__ == '__main__':
# # Use the model
#   model.train(data="coco1289.yaml", epochs=15, device= "0",batch=8, workers=6)  # train the model
 results = model("bai-tren(1) (1).jpg", save=True)  # predict on an image
# # print('ok',results)
# python predict.py model=yolov8l.pt source="test3.mp4" show=True
