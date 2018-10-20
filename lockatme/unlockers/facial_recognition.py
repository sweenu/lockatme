import face_recognition as face
import cv2


def is_recognized(model_image_path, test_image):
    model_image = face.load_image_file(model_image_path)

    model_face_encoding = face.face_encodings(model_image)[0]
    test_face_locations = face.face_locations(test_image)
    test_face_encodings = face.face_encodings(test_image, test_face_locations)

    known_faces = [
        model_face_encoding
    ]

    for face_encoding in test_face_encodings:
        matches = face.compare_faces(known_faces, face_encoding)

        if True in matches:
            return True

    return False


def authenticate(path):
    camera = cv2.VideoCapture(0)

    process_shot = True
    while True:
        _, shot = camera.read()
        shot = cv2.resize(shot, (0, 0), fx=0.25, fy=0.25) # 1/4 the size of original
        shot = shot[:, :, ::-1]  # Conversion from BGR to RGB

        if process_shot:
            if is_recognized(path, shot):
                camera.release()
                cv2.destroyAllWindows()
                return

        process_shot = not process_shot
