"""
VeilSight — Persistence-Gated Glyph Extraction (Public Skeleton)

This script demonstrates the persistence logic used to extract
stable visual structures ("glyphs") from entropy-rich video.

NOTE:
- This version does NOT include trained models
- Dataset access is not provided
"""

import cv2
import numpy as np
import os

# ---------------- CONFIG ----------------

VIDEO_PATH = "input_video.mp4"
OUTPUT_DIR = "glyphs_out"

FRAME_STEP = 4
ENTROPY_THRESHOLD = 4.5
STABILITY_FRAMES = 8
EDGE_DIFF_THRESHOLD = 10

# ----------------------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)


def frame_entropy(gray):
    """Shannon entropy of grayscale frame"""
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist = hist / (hist.sum() + 1e-9)
    return -np.sum(hist * np.log2(hist + 1e-9))


def predict_glyph_placeholder(gray_frame):
    """
    Placeholder for trained glyph model.
    Always returns True for demonstration.
    """
    return True


cap = cv2.VideoCapture(VIDEO_PATH)

prev_edges = None
stable_count = 0
glyph_id = 0
frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % FRAME_STEP != 0:
        frame_id += 1
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 60, 120)
    entropy = frame_entropy(gray)

    if entropy < ENTROPY_THRESHOLD:
        if prev_edges is not None:
            diff = np.mean(np.abs(edges - prev_edges))
            if diff < EDGE_DIFF_THRESHOLD:
                stable_count += 1
            else:
                stable_count = 0

        prev_edges = edges

        if stable_count >= STABILITY_FRAMES:
            if predict_glyph_placeholder(gray):
                out_path = os.path.join(
                    OUTPUT_DIR, f"glyph_{glyph_id}.png"
                )
                cv2.imwrite(out_path, gray)
                print(f"[GLYPH] saved {out_path}")
                glyph_id += 1
                stable_count = 0

    frame_id += 1

cap.release()
print("Extraction complete.")
