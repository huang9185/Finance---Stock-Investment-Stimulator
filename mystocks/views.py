from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from itertools import chain
from operator import attrgetter
from .models import *
import requests, json

API_KEY = 'PAHW27IP6QTSB1Y8'
IMAGE_SEARCH_API = 'AIzaSyDR1k0v_ZwbdObq6R30QCnLWXZQzHd7D-k'
CSE_ID = '9123e75d87a734d2b'

def home(request):
    if request.user.is_authenticated:
        return render(request, "mystocks/home.html")
    else:
        return render(request, "mystocks/login.html")

def history(request):
    if request.method == "GET":
        sells = Sell.objects.filter(user=request.user.id)
        purchases = Purchase.objects.filter(user=request.user.id)
        transactions = sorted(
            chain(sells, purchases),
            key=attrgetter('first_created'),
            reverse=True
        )
        paginator = Paginator(transactions, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "mystocks/history.html", {
            "transactions":page_obj
        })

def watchlist(request):
    if request.method == "GET":
        watches = Watch.objects.filter(user=request.user.id)
        paginator = Paginator(watches, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "mystocks/watchlist.html", {
            "watches": page_obj,
        })

def watch(request, quote, is_watched):
    if (is_watched == 0):
        url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+quote+"&apikey="+API_KEY
        response = requests.get(url).json()
        name = response["Name"]
        watch = Watch(user=request.user.id, quote=quote.upper(), company=name)
        watch.save()
        return JsonResponse({
            'message': 'Stock status is updated to 1 successfully'
        }, safe=False)
    else:
        watch = Watch.objects.filter(user=request.user.id).filter(quote=quote.upper())[0]
        watch.delete()
        return JsonResponse({
            'message': 'Stock is not watched anymore'
        }, safe=False)

def stock(request, quote):
    if request.method == "GET":
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+quote+'&apikey='+API_KEY
        response = requests.get(url).json()['Global Quote'];
        if (Watch.objects.filter(user=request.user.id).filter(quote=quote.upper()).exists() == True):
            is_watched = "true"
        else:
            is_watched = "false"

        if (Share.objects.filter(user=request.user.id).filter(quote=quote.upper()).exists()):
            share = "true"
        else:
            share = "false"

        return render(request, "mystocks/stock.html", {
            "api":API_KEY,
            "quote": quote,
            "open":response["02. open"],
            "high":response["03. high"],
            "low":response["04. low"],
            "price":response["05. price"],
            "volume":response["06. volume"],
            "latest":response["07. latest trading day"],
            "previousclose":response["08. previous close"],
            "change":response["09. change"],
            "changepercent":response["10. change percent"],
            "is_watched": is_watched,
            "share": share
        })

def sell(request, quote):
    if request.method == "GET":
        share = Share.objects.filter(user=request.user.id).get(quote=quote)
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+quote+'&apikey='+API_KEY
        response = requests.get(url).json()
        price = response["Global Quote"]["05. price"]
        return render(request, "mystocks/sell.html", {
            "share": share,
            "price": price
        })
    else:
        number = int(request.POST["number"])
        price = float(request.POST["price"])
        sell = Sell(user=request.user.id, quote=quote, number=number, price=price)
        sell.save()
        share = Share.objects.filter(user=request.user.id).get(quote=quote)
        share.numberTotal = int(share.numberTotal)-number
        if (int(share.numberTotal) == 0):
            share.delete()
        else:
            share.earnedTotal = float(share.earnedTotal)+number*price
            share.save(update_fields=["numberTotal", "earnedTotal"])
        return HttpResponseRedirect(reverse('profile'))

def share(request, quote):
    if request.method == "GET":
        return render(request, "mystocks/share.html", {
            "quote": quote,
            "api": API_KEY,
        })
    elif request.method == "POST":
        price = float(request.POST["price"])
        number = int(request.POST["number"])
        quote = request.POST["quote"]
        purchase = Purchase(
            user=request.user.id,
            quote=quote,
            number=number,
            price=price
        )
        purchase.save()
        if Share.objects.filter(user=request.user.id).filter(quote=quote).exists():
            share = Share.objects.filter(user=request.user.id).filter(quote=quote)[0]
            share.numberTotal = int(share.numberTotal)+number
            share.paidTotal = float(share.paidTotal) + price*number
            share.save(update_fields=["numberTotal", "paidTotal"])
        else:
            share = Share(
                user=request.user.id,
                quote=quote,
                numberTotal=number,
                paidTotal=price*number
            )
            share.save()
        return HttpResponseRedirect(reverse('profile'))

def search(request, category):
    if request.method == "GET":
        return render(request, "mystocks/search.html", {
            "category": category,
            "api": API_KEY,
        })
    else:
        if category == "stock":
            url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+request.POST["input"]+'&apikey='+API_KEY
            response = requests.get(url).json()
            if "01. symbol" in response['Global Quote']:
                return HttpResponseRedirect(reverse('stock', kwargs={'quote':response['Global Quote']["01. symbol"]}))
            else:
                return render(request, "mystocks/search.html", {
                    "category": category,
                    "message": "The stock does not exist",
                    "api": API_KEY,
                })
        else:
            url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+request.POST["input"]+"&apikey="+API_KEY
            response = requests.get(url).json()
            if "Symbol" in response:
                return HttpResponseRedirect(reverse('company', kwargs={'quote':response['Symbol']}))
            else:
                return render(request, "mystocks/search.html", {
                    "category": category,
                    "message": "The company does not exist",
                    "api": API_KEY,
                })

def company(request, quote):
    if request.method == "GET":
        url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+quote+"&apikey="+API_KEY
        response = requests.get(url).json()
        if response == {}:
            return render(request, "mystocks/company.html", {
                "message": "Company information temporarily unavailable"
            })
        else:
            return render(request, "mystocks/company.html", {
                "symbol": response["Symbol"],
                "assettype": response["AssetType"],
                "name": response["Name"],
                "description": response["Description"],
                "currency": response["Currency"],
                "country": response["Country"],
                "sector": response["Sector"],
                "industry": response["Industry"],
                "address": response["Address"],
                "pe": response["PERatio"],
                "peg": response["PEGRatio"],
                "book": response["BookValue"],
                "dividendpshare": response["DividendPerShare"],
                "dividendyield": response["DividendYield"],
                "weekhigh": response["52WeekHigh"],
                "weeklow": response["52WeekLow"],
                "50daymoving": response["50DayMovingAverage"],
                "200daymoving": response["200DayMovingAverage"],
                "exchange": response["Exchange"],
                "fiscalyearend": response["FiscalYearEnd"],
                "latestquarter": response["LatestQuarter"],
                "marketcap": response["MarketCapitalization"],
                "ebitda": response["EBITDA"],
            })

def profile(request):
    if request.method == "GET":
        shares = Share.objects.filter(user=request.user.id)
        return render(request, "mystocks/profile.html", {
            "shares":shares
        })

def register_view(request):
    if request.method == "GET":
        return render(request, "mystocks/register.html")
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        if password != confirm:
            message = "Two passwords are not the same"
        elif User.objects.filter(username=username).exists():
            message = "Username already exists"
        elif User.objects.filter(email=email).exists():
            message = "Email already exists"
        else:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        return render(request, "mystocks/register.html", {
            "message": message
        })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "mystocks/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "mystocks/login.html")

def logout_view(request):
    logout(request)
    return render(request, "mystocks/login.html", {
        "message": "Logged out"
    })