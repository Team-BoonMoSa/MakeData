import cv2
import os

def sample_images(video_file, output_folder, interval=1000):
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print("Error: failed to open video file.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval == 0:
            image_file = os.path.join(output_folder, f"{count}.jpg")
            cv2.imwrite(image_file, frame)
        count += 1
    cap.release()

if __name__ == "__main__":
    sample_images("tar.MOV", "output_folder", 100)