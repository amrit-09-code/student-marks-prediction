from django.shortcuts import render

# Create your views here.
import pickle, os
from django.shortcuts import render
from .models import Student

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def home(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'home.html', {'students': students})

def predict(request):
    if request.method == 'POST':
        name = request.POST['name']
        study = float(request.POST['study_hours'])
        attend = float(request.POST['attendance'])
        prev = float(request.POST['previous_marks'])
        sleep = float(request.POST['sleep_hours'])

        pred = model.predict([[study, attend, prev, sleep]])[0]
        result = "Pass" if pred >= 40 else "Fail - Need Improvement"

        Student.objects.create(
            name=name, study_hours=study, attendance=attend,
            previous_marks=prev, sleep_hours=sleep,
            predicted_marks=round(float(pred), 2), result=result
        )
        return render(request, 'result.html', {'name': name, 'marks': round(float(pred), 2), 'result': result})
    return render(request, 'predict.html')