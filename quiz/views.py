from django.http import HttpResponse
from sklearn.cluster import KMeans
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
import numpy as np
import pandas as pd
import xlwt
from xlwt import Workbook
import pickle
from secureapp import settings
from sklearn.cluster import KMeans
from django.shortcuts import render


def question(request):
    if request.method == 'POST':
        response = get_personality(
            request.POST.get('answer1', None),
            request.POST.get('answer2', None),
            request.POST.get('answer3', None),
            request.POST.get('answer4', None),
            request.POST.get('answer5', None),
            request.POST.get('answer6', None),
            request.POST.get('answer7', None),
            request.POST.get('answer8', None),
            request.POST.get('answer9', None),
            request.POST.get('answer10', None),
            request.POST.get('answer11', None),
            request.POST.get('answer12', None),
            request.POST.get('answer13', None),
            request.POST.get('answer14', None),
            request.POST.get('answer15', None))
        if response != 4:
            print('SUCCESS')
            return redirect('CLhome')
        else:
            print('FAIL')
            user = User.objects.filter(username=request.user)
            user.update(is_active=0)
            return redirect('Clientlogin')

    return render(request, 'quiz.html')


def get_personality(EXT1, EXT2, EXT3, EST1, EST2, EST3, AGR1, AGR2, AGR3, CSN1, CSN2, CSN3, OPN1, OPN2, OPN3):
    pickle_in = open("model", "rb")
    model = pickle.load(pickle_in)
    
    answers = EXT1, EXT2, EXT3, EST1, EST2, EST3, AGR1, AGR2, AGR3, CSN1, CSN2, CSN3, OPN1, OPN2, OPN3
    
    input_data = [EXT1, EXT2, EXT3, EST1, EST2, EST3, AGR1, AGR2, AGR3, CSN1, CSN2, CSN3, OPN1, OPN2, OPN3]
    print(input_data)

    my_data = input_data

    wb = Workbook()
    sheet5 = wb.add_sheet('Sheet 5')

    sheet5.write(0, 0, "EXT1")
    sheet5.write(0, 1, "EXT2")
    sheet5.write(0, 2, "EXT3")
    sheet5.write(0, 3, "EST1")
    sheet5.write(0, 4, "EST2")
    sheet5.write(0, 5, "EST3")
    sheet5.write(0, 6, "AGR1")
    sheet5.write(0, 7, "AGR2")
    sheet5.write(0, 8, "AGR3")
    sheet5.write(0, 9, "CSN1")
    sheet5.write(0, 10, "CSN2")
    sheet5.write(0, 11, "CSN3")
    sheet5.write(0, 12, "OPN1")
    sheet5.write(0, 13, "OPN2")
    sheet5.write(0, 14, "OPN3")

    sheet5.write(1, 0, EXT1)
    sheet5.write(1, 1, EXT2)
    sheet5.write(1, 2, EXT3)
    sheet5.write(1, 3, EST1)
    sheet5.write(1, 4, EST2)
    sheet5.write(1, 5, EST3)
    sheet5.write(1, 6, AGR1)
    sheet5.write(1, 7, AGR2)
    sheet5.write(1, 8, AGR3)
    sheet5.write(1, 9, CSN1)
    sheet5.write(1, 10, CSN2)
    sheet5.write(1, 11, CSN3)
    sheet5.write(1, 12, OPN1)
    sheet5.write(1, 13, OPN2)
    sheet5.write(1, 14, OPN3)

    wb.save('xlwt example.xls')

    my_data = pd.read_excel('xlwt example.xls')
    

    my_personality = model.predict(my_data)
    print('My Personality Cluster: ', my_personality)

    # Summing up the my question groups
    col_list = list(my_data)
    ext = col_list[0:3]
    est = col_list[3:6]
    agr = col_list[6:9]
    csn = col_list[9:12]
    opn = col_list[12:15]

    my_sums = pd.DataFrame()
    my_sums['extroversion'] = my_data[ext].sum(axis=1) / 3
    my_sums['neurotic'] = my_data[est].sum(axis=1) / 3
    my_sums['agreeable'] = my_data[agr].sum(axis=1) / 3
    my_sums['conscientious'] = my_data[csn].sum(axis=1) / 3
    my_sums['open'] = my_data[opn].sum(axis=1) / 3
    my_sums['cluster'] = my_personality
    print('Sum of my question groups : ')
    print(my_sums)
    return my_personality
