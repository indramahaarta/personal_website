from unittest import result
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from collections import namedtuple


# Create your views here.

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def mainview(request):

    return render(request, 'mainview.html')

# Contoh fungsi untuk get data di database
def index(request) :
    cursor = connection.cursor();
    try:
        cursor.execute("Set search_path to Usersystem")
        cursor.execute("Select fname from user_profile")
        result = namedtuplefetchall(cursor)
        
        print(result)
        for i in result:
            print(i.fname + " " + i.email)

    except Exception as e:
        print(e);
    finally:
        cursor.close()

    return HttpResponse("");

