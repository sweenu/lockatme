import face_recognition as fr


def is_recognized(imageSet, imagePath):
    model_image = fr.load_image_file(imageSet)
    unknown_image = fr.load_image_file(imagePath)

    model_face_encoding = fr.face_encodings(model_image)[0]
    unknown_face_encoding = fr.face_encodings(unknown_image)[0]

    know_faces = [
        model_face_encoding
    ]

    results = fr.compare_faces(know_faces, unknown_face_encoding)

    return any(results)
