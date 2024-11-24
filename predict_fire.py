from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")

# Perform object detection on an image
results = model.predict("fire_images/0000.jpg", save=True)
results[0].show()