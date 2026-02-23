import cv2
import os

def extract_frames(video_path, output_dir, every_n=5):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % every_n == 0:
            cv2.imwrite(
                os.path.join(output_dir, f"frame_{saved}.jpg"),
                frame
            )
            saved += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved} frames from {video_path}")


REAL_DIR = "dataset/real"
FAKE_DIR = "dataset/fake"

for video in os.listdir(REAL_DIR):
    extract_frames(
        os.path.join(REAL_DIR, video),
        os.path.join("frames/real", video.split(".")[0])
    )

for video in os.listdir(FAKE_DIR):
    extract_frames(
        os.path.join(FAKE_DIR, video),
        os.path.join("frames/fake", video.split(".")[0])
    )
