import cv2

def light(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        avg_brightness = gray.mean()

        threshold = 50 # You can adjust this value
        if avg_brightness > threshold:
            status= 'ON'
        else:
            status='OFF'
        return status
