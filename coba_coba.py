from browser import document, alert  
import math

data1 = document['data1']
data2 = document['data2']
button = document['btn']
output = document['output']

rumusbmi = {'hitung': lambda TB, BB: round(BB / ((TB/100) ** 2), 1),
         'data1': 'Tinggi Badan (cm)', 'data2': 'Berat Badan (kg)'}

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan data yang sesuai!!!')
            temp = ''
            data1.value = temp
            return temp
        else:
            return temp
def hitung(num1, num2):
    for key in rumusbmi.keys():
        return rumusbmi['hitung'](num1, num2)
def main(ev):
    num1 = getNum(data1.value)
    num2 = getNum(data2.value)
    result = hitung(num1, num2)
    output.textContent = str(result)
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)  

data1.bind("keypress", keyEnter)
data2.bind("keypress", keyEnter)
