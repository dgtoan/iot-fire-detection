from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")

# Perform object detection on an image
results = model("fire_images/0000.jpg")
results[0].show()