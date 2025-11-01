import cv2
import pytesseract
from gtts import gTTS
import os

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\subad\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Start webcam
cam = cv2.VideoCapture(0)
print("Press 's' to capture image...")

while True:
    ret, frame = cam.read()
    cv2.imshow("Smart Vision Glass - Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("captured_text.jpg", frame)
        print("✅ Image captured successfully!")
        break

cam.release()
cv2.destroyAllWindows()

# OCR - extract text from image
img = cv2.imread("captured_text.jpg")
text = pytesseract.image_to_string(img)
print("\n🧠 Detected Text:\n", text)

# Text to Speech
if text.strip() == "":
    text = "No readable text detected."

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
os.system("start output.mp3")
