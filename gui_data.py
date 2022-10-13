import numpy as np
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random 
from matplotlib.animation import FuncAnimation
import statistics
import json

plt.style.use('fivethirtyeight')
# Generating x and y-values
x = []
y = []

start_pressed = 0

# Fungsi-fungsi statistika
def min_val(nilai):
    minimum = min(nilai)
    return minimum

def max_val(nilai):
    maksimum = max(nilai)
    return maksimum

def median_val(nilai):
    median = statistics.median(nilai)
    return median

def avg_val(nilai):
    total = sum(nilai)
    length = len(nilai)
    average = total/length
    return average

def start_graph():
    print('start')   

def pause_graph():
    plt.close('all')

# function to add to JSON
def write_json(new_data, filename='data_cadIT.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["array"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        print('JSON Ditulis!')
        
# Variabel data sensor untuk Temperature dan Humidity

Min_T = []
Max_T = []
Median_T = []
Average_T= []

Min_H = []
Max_H = []
Median_H = []
Average_H= []

time_val1 = []
time_val2 = []
Temp_val = []
Hum_val = []

index = count()
awal = {
    "array" : [

    ]
}

# Start button
axButn2 = plt.axes([0.5, 0.1, 0.1, 0.1])
btn2 = Button(
  axButn2, label="Start", color='pink', hovercolor='tomato')

# Stop button
axButn3 = plt.axes([0.7, 0.1, 0.1, 0.1])
btn3 = Button(
  axButn3, label="Stop", color='pink', hovercolor='tomato')


# Write JSON
with open("data_cadIT.json","w") as outfile:
        json.dump(awal, outfile)

def animate(i):
    plt.suptitle("Sensor data Room 1")
    
    # Plot Temperature
    time_val1.append(next(index))
    Temp_val.append(random.randint(18,30))
    
    Min_T.append(min_val(Temp_val))
    Max_T.append(max_val(Temp_val))
    Median_T.append(median_val(Temp_val))
    Average_T.append(avg_val(Temp_val))

    
    plt.subplot(1,2,1)
    plt.cla()
    plt.subplots_adjust (left=0.1, bottom = 0.5, top= 0.8)
    
    plt.plot(time_val1,Min_T, label = 'Min')
    plt.plot(time_val1,Max_T, label = 'Max')
    plt.plot(time_val1,Median_T, label = 'Median')
    plt.plot(time_val1,Average_T, label = 'Average')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend(loc='upper left')

    # Plot Humidity
    time_val2.append(next(index))
    Hum_val.append(random.randint(30,50))

    Min_H.append(min_val(Hum_val))
    Max_H.append(max_val(Hum_val))
    Median_H.append(median_val(Hum_val))
    Average_H.append(avg_val(Hum_val))

    plt.subplot(1,2,2)
    plt.cla()
    plt.plot(time_val2,Min_H, label='Min')
    plt.plot(time_val2,Max_H, label='Max')
    plt.plot(time_val2,Median_H, label='Median')
    plt.plot(time_val2,Average_H, label='Average')
    plt.xlabel('Time')
    plt.ylabel('Humidity')
    plt.legend(loc='upper right')

    tulis = {
      "temperature": Temp_val,
      "Min T": min_val(Temp_val),
      "Max T": max_val(Temp_val),
      "Median T": median_val(Temp_val),
      "Average T": avg_val(Temp_val),
      "humidity": Hum_val,
      "Min H": min_val(Hum_val),
      "Max H": max_val(Hum_val),
      "Median H": median_val(Hum_val),
      "Average H": avg_val(Hum_val),
    }

    write_json(tulis)


ani = FuncAnimation(plt.gcf(), animate,interval=2000)


def stopp(event):
    print('stop pressed')
    ani.event_source.stop()


btn3.on_clicked(stopp)

def startt(event):
    print('start pressed')
    ani.event_source.start()

while(btn2.on_clicked(startt)):
    
    if(btn3.on_clicked(stopp)):
        current_value()
        start_pressed =1
        print('stop - this is current')
    

print('Start GUI')
plt.show() 
