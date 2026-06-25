from ultralytics import YOLO
import cv2

# Load the trained YOLO model
model = YOLO("runs/detect/train6/weights/best.pt")  # Load a pretrained model (use your model path)

def predict_on_image(image_path, conf=0.4):
    # Read the image
    image = cv2.imread(image_path)

    # Run inference on the image with the specified confidence threshold
    results = model(image, conf=conf)  # Predict on the image with confidence threshold

    # Get the first result (since results is a list of results)
    result = results[0]

    # Render the predictions on the image
    image_with_detections = result.plot()  # This will add the bounding boxes, labels to the image

    # Display the image with the detected objects in an OpenCV window
    cv2.imshow("Image with Detections", image_with_detections)

    # Wait for any key press to close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def predict_on_video(video_path, conf=0.4):
    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or error reading the video.")
            break

        # Run inference on the current frame with the specified confidence threshold
        results = model(frame, conf=conf)  # Predict on the frame with confidence threshold

        # Get the first result (since results is a list of results)
        result = results[0]

        # Render the predictions on the frame
        frame_with_detections = result.plot()  # This will add the bounding boxes, labels to the frame

        # Display the frame with the detected objects in an OpenCV window
        cv2.imshow("Video with Detections", frame_with_detections)

        # Press 'Esc' to exit
        if cv2.waitKey(1) & 0xFF == 27:  # 1ms delay
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Choose either image or video
    choice = input("Enter '1' for image or '2' for video: ")

    if choice == '1':
        # Path to your image file
        image_path = "IMG_6092(1).JPG"
        predict_on_image(image_path, conf=0.5)
    elif choice == '2':
        # Path to your video file
        video_path = "New BOSS Eyewear- #SharpenYourFocus with Henry Cavill - Part Two - BOSS.mp4"
        predict_on_video(video_path, conf=0.5)
    else:
        print("Invalid choice. Please enter '1' for image or '2' for video.")