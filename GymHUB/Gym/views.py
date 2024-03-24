from django.shortcuts import render,redirect
from Gym.forms import ContactForm
from django.contrib import messages
# Create your views here.
def index(request):
    contactform=ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        messages.success(request,'Your information have been submitted!!')
        def __str__(self):
            return self.name
        return redirect("index")
    return render(request,'index.html',{'forms':ContactForm})