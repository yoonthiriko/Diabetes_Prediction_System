from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def home(request):
    """Render the home page."""
    return render(request, 'Home.html')

def predict(request):
    """Render the prediction page."""
    return render(request, 'predict.html')

def result(request):
    """Handle the prediction request and return the result as JSON."""
    if request.method == "GET":
        # Load and prepare data
        data = pd.read_csv(r'C:\Users\User\Desktop\DiabetesPrediction\DiabetesPrediction\diabetes.csv')
        X = data.drop(columns='Outcome')
        Y = data['Outcome']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        model = LogisticRegression()
        model.fit(X_train, Y_train)

        # Extract values from GET request
        try:
            features = [
                float(request.GET['n1']),
                float(request.GET['n2']),
                float(request.GET['n3']),
                float(request.GET['n4']),
                float(request.GET['n5']),
                float(request.GET['n6']),
                float(request.GET['n7']),
                float(request.GET['n8'])
            ]
            pred = model.predict([features])
            result1 = "Positive" if pred == [1] else "Negative"
        except ValueError:
            result1 = "Invalid input"

        return JsonResponse({'result': result1})
