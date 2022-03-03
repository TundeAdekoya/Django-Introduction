from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("""
            <h1>Welcome to Dream Land</h1>
            <h3>Where your dreams come through</h3>
    """)

def service(request):
    return HttpResponse("""
            <h2>We make dreams come true</h2>
            <h3>Our Services are:</h3>
            <ul>
                <li>Scary Houses</li>
                <li>Amusement Parks</li>
                <li>Hunted Boatrides</li>
            </ul>
    """)

def partners(request):
    return HttpResponse("""
            <h3>Our Partners are:</h3>
            <ul>
                <li>Disney</li>
                <li>Netflix</li>
                <li>Youtube Kids</li>
            </ul>
    """)

def about(request):
    return HttpResponse("""
            <h3>We are a cmpany that specializes in people having fun</h3>
            <ul>
                <li>Our History</li>
                <li>Our team</li>
            </ul>
    """)

def contact (request):
    return HttpResponse("""
            <h3>Reach us at</h3>
            <ul>
                <li>Our Office</li>
                <li>Our Email</li>
            </ul>
    """)
