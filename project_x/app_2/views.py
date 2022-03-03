from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("""
            <h1>Welcome to Lux Kitch</h1>
            <h3>Where serve you the best dish in Lagoss</h3>
    """)

def service(request):
    return HttpResponse("""
            <h2>We make luxury dish</h2>
            <h3>Our Services are:</h3>
            <ul>
                <li>Luxury Special</li>
                <li>Equisite meals</li>
                <li>Kiddies luxury dish</li>
            </ul>
    """)

def partners(request):
    return HttpResponse("""
            <h3>Our Partners are:</h3>
            <ul>
                <li>Eric Kayser</li>
                <li>Landmark Event Centre</li>
                <li>Oriental Hotel</li>
            </ul>
    """)

def about(request):
    return HttpResponse("""
            <h3>We serve the best quisine in Lagos State</h3>
            <ul>
                <li>Our Chef</li>
                <li>Our Menu</li>
            </ul>
    """)

def contact (request):
    return HttpResponse("""
            <h3>Join us at</h3>
            <ul>
                <li>Our Resturant</li>
                <li>Our Resort</li>
            </ul>
    """)