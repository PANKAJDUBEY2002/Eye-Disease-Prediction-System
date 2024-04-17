from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import io
import numpy as np
from PIL import Image
from django.http import JsonResponse, HttpResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

import joblib
# Load the saved machine learning model
#model = joblib.load('eye_disease_classification_model.pkl')


# Create your views here.
from django.http import HttpResponse
from EyeDisease.forms import EyeImageForm
def form_input(request):
    res=render(request,'EyeDisease/image_form.html')
    return res
def app(request):
    res=render(request,'EyeDisease/form.html')
    return res
@csrf_exempt
def upload_eye_image(request):
    if request.method == 'POST':
        # Load the model
        model = load_model('my_model.h5')

        # Check if 'eye_image' exists in request.FILES
        if 'eye_image' not in request.FILES:
            return JsonResponse({'error': 'No image found in request'}, status=400)

        # Get the uploaded image file
        image_file = request.FILES['eye_image']
        image_data = image_file.read()

        # Convert image data to a NumPy array
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((60, 60))  # Resize the image to match the input size expected by the model
        image_array = np.array(image)
        image_array = image_array.astype('float32') / 255.0  # Normalize pixel values

        # Preprocess the image data (if needed)
        # Example: Normalize pixel values, convert to grayscale, etc.

        # Make predictions using the loaded model
        prediction = model.predict(np.expand_dims(image_array, axis=0))
        predict=np.argmax(prediction)

        # Prepare the response
        return HttpResponse(predict)
        response_data = {
            'prediction': predict  # Convert prediction to list for JSON serialization
        }

        # Return the prediction as a JSON response
        return JsonResponse(response_data)

    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=400)
