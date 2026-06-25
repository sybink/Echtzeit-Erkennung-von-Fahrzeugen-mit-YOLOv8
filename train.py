from ultralytics import YOLO  # Import YOLO class

# Load a model
model = YOLO("runs/detect/train4/weights/last.pt")  # Load your trained model
if __name__ == '__main__':
    # Train the model
    model.train(data="coco1289.yaml", epochs=5, device="0", batch=10, workers=8)

