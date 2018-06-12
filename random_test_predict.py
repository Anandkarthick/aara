# Change the phrases in the the file to get the prediction.
# Multinomial NB classifer
import random_predict as rp
import data_clean as dc

phrase = input("Enter the your question.. : ")

result_str = dc.data_clean(phrase).return_str()

result = rp.random_predict(result_str)




