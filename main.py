from light_det_ocv import light
from human_detection import detect_humans
from send_alert import send_alert_telegram
import cv2
import time

# Open default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break
        
        cv2.imshow("Live Feed", frame)  # Add this just before cv2.waitKey

        light_status = light(frame)
        print("Light Status: ",light_status)
    
        # Step 3: Detect Humans
        human_present = detect_humans(frame)  
        print("Human Present: ",human_present)
    
        # Step 4: If lights are ON and no humans detected, send alert
        if light_status == "ON" and not human_present:
            print("ALERT: No human detected but lights are ON!")
            send_alert_telegram()
        else:
            print("Everything is fine. No alert needed.")
        # Wait for 10 seconds
        print('-------------------------')
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
        time.sleep(10)

except KeyboardInterrupt:
    print("Interrupted by user")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
