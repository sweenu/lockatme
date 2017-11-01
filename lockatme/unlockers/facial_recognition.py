def facial_recognition(imageSet,imagePath):

    import face_recognition
    import sys
    #imageSet = sys.argv[1]
    #imagePath = sys.argv[2]
    juju_image = face_recognition.load_image_file(imageSet)
    unknown_image = face_recognition.load_image_file(imagePath)
    #not working all the time with sunglasses

    juju_face_encoding = face_recognition.face_encodings(juju_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    know_faces = [
        juju_face_encoding
    ]

    results = face_recognition.compare_faces(know_faces,unknown_face_encoding)

    return results[0]
