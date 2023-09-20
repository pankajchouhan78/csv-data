from django.shortcuts import render
import io
import csv
from . models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        file = request.FILES['csv_file']
        # file ki sari field ko decode karne ke liye
        decode_file = file.read().decode('utf-8') # utf-8 ye string ko decode karne ki methods hoti hai.
        # data string me converd hoga matlab bits me isliye io.String ka use kiya hai.
        io_string = io.StringIO(decode_file)
        # next matlab hum ek line chodne wale hai. kyuki wo datetime wati field hai. next ek point aage bada dega. 
        next(io_string)
        # for loop me csv read karega the io_string ke ander converd karega, datetime ke liye delimiter liye hai.
        for row in csv.reader(io_string, delimiter=','):
            date = row[0]
            open_price = float(row[1])
            high_price = float(row[2])
            low_price = float(row[3])
            close_price = float(row[4])
            adj_close_price = float(row[5])
            volume = int(row[6])

            # create all the data
            Stock.objects.create(
                date = date,
                open = open_price,
                high = high_price,
                low = low_price,
                close = close_price,
                adj_close = adj_close_price,
                volume = volume,
            )
        return render(request,"success.html")


        
    return render(request, 'index.html')

