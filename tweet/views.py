from django.shortcuts import render

from .apps import TweetConfig
from django.http import JsonResponse, request, response
from rest_framework.views import APIView
from django.http import HttpResponse
import pickle
# Create your views here.




#def get(request):
        #if request.method =='GET':

            # get text from request
#            search = request.GET.get('search') 
            
            # vectorize text
#            vector = TweetConfig.vectorizer.transform([search])

            # predict based on vector
#            prediction = TweetConfig.model.predict(vector)[0]

#            if(prediction == 0):
#                predict = 'Negative'
#            if(prediction == 1):
#                predict = 'Positive'
            
            #build response
#            response = {'text_sentiment': predict}

            # return response
            #return JsonResponse(response)
            #return render(request, 'index.html',{'response':response})
#            return HttpResponse(response)


def home(request):
    return render(request,"index.html")

def predict(request):
    if request.method == 'POST':
        data = pickle.load(open('tweet\models\models.p', 'rb'))
        
        model = data['model']
        vectorizer = data['vectorizer']
        search = request.POST.get('search') 
        vector = vectorizer.transform([search])
        prediction = model.predict(vector)[0]
        if(prediction == 0):
            predict = 'Negative ☹ '
        if(prediction == 1):
            predict = 'Positive 🙂'
        context = {'search': search , 'Text_Sentiment': predict}    

        return render(request, 'index.html', context)

