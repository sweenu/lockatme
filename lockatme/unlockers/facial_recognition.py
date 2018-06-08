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

    matches = []
    for _, face_encoding in zip(test_face_locations, test_face_encodings):
        matches.append(face.compare_faces(known_faces, face_encoding, tolerance=0.6))

    return any(matches)


def authenticate():
    camera = cv2.VideoCapture(0)

    while True:
        _, shot = camera.read()
        shot = shot[:, :, ::-1]  # Conversion from BGR to RGB
        if is_recognized('/home/sweenu/Pictures/prof_pic.jpg', shot):
            camera.release()
            cv2.destroyAllWindows()
            return
