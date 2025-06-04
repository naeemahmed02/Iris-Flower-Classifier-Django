from django.shortcuts import render
from .forms import IrisForm
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, 'static', 'iris_model.pkl')
model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'static', 'scaler.pkl')
scaler = joblib.load(scaler_path)


def home(request):
    
    prediction = ""
    flowers = ['Versicolor', 'Virginica']
    
    if request.method == "POST":
        form = IrisForm(request.POST)
        if form.is_valid():
            data = np.array(
                [
                    [
                        form.cleaned_data["sepal_length"],
                        form.cleaned_data["sepal_width"],
                        form.cleaned_data["petal_length"],
                        form.cleaned_data["petal_width"],
                    ]
                ]
            )
            data = scaler.transform(data)
            pred = model.predict(data)
            prediction = flowers[pred[0]]
            
    else:
        form = IrisForm()
    return render(request, "base/index.html", {"form": form, "prediction": prediction})
