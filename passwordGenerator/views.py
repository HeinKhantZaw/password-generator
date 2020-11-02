from django.shortcuts import render
from zxcvbn import zxcvbn
import random, string


# Create your views here.
def home(req):
    return render(req, 'index.html')


def password(request):
    strengthText = {
        0: "The Worst",
        1: "Very Bad",
        2: "Still Weak",
        3: "Good",
        4: "Strong"
    }
    password_char = ''
    password = ''
    password_length = int(request.GET['pwLength'])
    if request.GET.get('uppercase'):
        password_char += string.ascii_uppercase
    if request.GET.get('lowercase'):
        password_char += string.ascii_lowercase
    if request.GET.get('number'):
        password_char += string.digits
    for x in range(password_length):
        password += random.choice(password_char)
    strength = zxcvbn(password)
    str_strength = strengthText[strength['score']]
    return render(request, 'password.html',
                  {'password': password, 'pwStrength': strength['score'], 'strengthText': str_strength})
