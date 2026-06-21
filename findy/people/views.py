import face_recognition
from django.shortcuts import render
from .models import MissingPerson

def face_search(request):
    results = []
    message = ''
    if request.method == 'POST' and request.FILES.get('photo'):
        upload = request.FILES['photo']
        image = face_recognition.load_image_file(upload)
        encodings = face_recognition.face_encodings(image)
        if not encodings:
            message = 'No face found in uploaded image.'
        else:
            query_encoding = encodings[0]
            people = MissingPerson.objects.exclude(photo='')
            for person in people:
                try:
                    known_image = face_recognition.load_image_file(person.photo.path)
                    known_encodings = face_recognition.face_encodings(known_image)
                    if known_encodings:
                        match = face_recognition.compare_faces([known_encodings[0]], query_encoding, tolerance=0.5)
                        if match[0]:
                            results.append(person)
                except Exception:
                    pass
    return render(request, 'people/face_search.html', {
        'results': results,
        'message': message,
    })