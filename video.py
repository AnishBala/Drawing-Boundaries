import pandas as pd
import cv2

df = pd.read_csv("cctvStatusD03.csv")
option = ["Hwy 50 at Zinfandel Dr EB 2"]
row_index = 191
url = df.loc[row_index, "streamingVideoURL"]
def draw_rectangle(frame, x, y, w, h, color=(255, 0, 0), thickness = 2):
    cv2.rectangle(frame, (x,y), (x+w, y+h), color, thickness)
video_path = "output.mp4"
cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    draw_rectangle(frame, 0, 13, 1280, 23)
    draw_rectangle(frame, 0, 38, 1280, 26)
    draw_rectangle(frame, 0, 65, 1280, 29)
    draw_rectangle(frame, 0, 95, 1280, 32)
    draw_rectangle(frame, 0, 128, 1280, 36)
    draw_rectangle(frame, 0, 165, 1280, 41)
    draw_rectangle(frame, 0, 297, 1280, 57)
    draw_rectangle(frame, 0, 360, 1280, 65)
    draw_rectangle(frame, 0, 431, 1280, 75)
    draw_rectangle(frame, 0, 512, 1280, 89)
    draw_rectangle(frame, 0, 609, 1280, 100)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()