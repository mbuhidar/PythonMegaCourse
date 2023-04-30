import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

file = "profile.jpg"

img = cv2.imread(file)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sF = 110
mN = 3

faces = face_cascade.detectMultiScale(img, 
                                      scaleFactor=sF/100.0, 
                                      minNeighbors=mN)

faces = faces[0:1] # Use only the first detection (typically largest)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 25)

cv2.imwrite("prof_" + str(mN) + "_" + str(sF) + "_" + file, img)

resized = cv2.resize(img, (int(img.shape[1]/5), int(img.shape[0]/5)))

cv2.imshow("Detected", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
