import time
import os
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Path to the folder containing images
image_folder = "C:\\Users\\DELL\\Desktop\\Sem 6\\MINI PRO\\classroom_images"

# Get list of image files in the folder (sorted for consistency)
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png", ".jpeg"))])

def detect_humans(image_path):
    """
    Uses YOLOv8 to detect humans in the provided image.
    Returns True if a person is detected, else False.
    """
    results = model(image_path)
    for r in results:
        for box in r.boxes:
            if r.names[int(box.cls[0])] == "person":
                return True  # Human detected
    return False  # No human detected

if __name__ == "__main__":
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        print(f"Processing: {image_path}")

        # Detect humans in the image
        human_found = detect_humans(image_path)
        print(f"Human Detected: {human_found} | Image: {image_path}")

        # Wait for 2 minutes before processing the next image
        time.sleep(10)

    print("All images processed!")