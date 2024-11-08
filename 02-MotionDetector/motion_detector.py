import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
video = cv2.VideoCapture(0)
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

while True:
    check, frame = video.read()
    status = 0

    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    current_frame = cv2.GaussianBlur(current_frame, (21, 21), 0) 

    # Detect first frame
    if first_frame is None:
        first_frame = current_frame
        continue
    
    # delta between first frame a nd current frame
    delta_frame = cv2.absdiff(first_frame, current_frame)
    delta_thresh= cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    delta_thresh = cv2.dilate(delta_thresh, None, iterations = 2)

    contours = cv2.findContours(delta_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        
        status = 1

        # Draw rectangle
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save motion in list
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    elif status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Create windows
    cv2.imshow("Gray", current_frame)
    cv2.imshow("Delta  frame", delta_frame)
    cv2.imshow("Thresh frame", delta_thresh)
    cv2.imshow("Color frame", frame)

    # Quit control
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(status_list)
print(times)

for i in range(0, len(times)-2, 2):
    row = pandas.DataFrame({"Start": [times[i]], "End": [times[i+1]]})
    df = pandas.concat([df, row], ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows