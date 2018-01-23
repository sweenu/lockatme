import subprocess
import face_recognition
import cv2


pl_image = face_recognition.load_image_file("pl.jpg")
pl_face_encoding = face_recognition.face_encodings(pl_image)[0]

if __name__ == '__main__':
    video_capture = cv2.VideoCapture(0)
    proc = subprocess.Popen(['feh', '-F', 'pad_lock.jpg'])
    reco = True

    while reco:
        ret, frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        for (top,right,bottom,left), face_encoding in zip(face_locations,face_encodings):
            
            match = face_recognition.compare_faces([pl_face_encoding], face_encoding)

            if match[0]:            
                proc.kill()
                reco = False

    video_capture.release()
