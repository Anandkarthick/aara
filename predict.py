import model_predict as mp
import data_clean as dc
from os import system
import time

phrase = input("Enter the your question.. : ")

result_str = dc.data_clean(phrase).return_str()

result = mp.model_predict(result_str).return_intent()

def conv(data):
    if data[0] == 'id_auto':
        system('say your auto insurance identity card is on the way')
    elif data[0] == 'id_home':
        system('say your home insurance identity card is on the way')
    elif data[0] == 'id':
        system('say which one? auto or home')
        time.sleep(3)


conv(result)
