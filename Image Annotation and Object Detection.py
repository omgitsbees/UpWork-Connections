import tensorflow as tf
import numpy as np
import cv2
import os
from PIL import Image
import matplotlib.pyplot as plt

# Load pre-trained YOLO model from TensorFlow Hub
MODEL_URL = "https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2"
detector = tf.saved_model.load(MODEL_URL)

# Load image for object detection
def load_image(image_path):
    img = Image.open(image_path)
    img = img.resize((640, 640))
    img_np = np.array(img)
    return img_np

# Perform object detection on an image
def detect_objects(image_path):
    img_np = load_image(image_path)
    input_tensor = tf.convert_to_tensor(img_np)
    input_tensor = input_tensor[tf.newaxis, ...]  # Corrected syntax
    
    # Perform detection
    detections = detector(input_tensor)
    
    # Visualize the detection
    visualize_detection(img_np, detections)

# Visualizing detection results
def visualize_detection(img_np, detections):
    boxes = detections['detection_boxes'].numpy()[0]
    scores = detections['detection_scores'].numpy()[0]
    classes = detections['detection_classes'].numpy()[0]
    
    for i, box in enumerate(boxes):
        if scores[i] < 0.5:  # Filter low confidence detections
            continue
        
        y1, x1, y2, x2 = box
        h, w, _ = img_np.shape
        p1 = int(x1 * w), int(y1 * h)
        p2 = int(x2 * w), int(y2 * h)
        
        # Draw rectangle for the detected object
        img_np = cv2.rectangle(img_np, p1, p2, (0, 255, 0), 2)
        label = f"Object {int(classes[i])}: {scores[i]:.2f}"
        img_np = cv2.putText(img_np, label, p1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Display the image with detection results
    plt.imshow(img_np)
    plt.axis("off")
    plt.show()

# Sample usage
image_path = "path_to_your_image.jpg"
detect_objects(image_path)

# Once images are annotated, you can use this script to detect objects using YOLO
