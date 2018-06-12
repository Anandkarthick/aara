import model_predict as mp
import data_clean as dc

phrase = input("Enter the your question.. : ")

result_str = dc.data_clean(phrase).return_str()

result = mp.model_predict(result_str)


