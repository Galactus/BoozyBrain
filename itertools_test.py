# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:38:38 2019

@author: Pranav
"""
from utils import *
import serial
import itertools
ingredients=['jus_citrons','jus_cranberry_(canneberges)','vodka','jus_dananas','cola_(coca_cola,_pepsi)','lait']
combi_full = []
for i in [1,2]:
    for combination in itertools.combinations(ingredients, i): 
        combi_full.append(combination)
#print(combi_full)
#-----------------------------------------------------------------------------------
        
#CHANGING THE INPUT FORMAT

new_list = []
for words in combi_full:
    new_list.append('+'.join(words))

#------------------------------------------------------------------------------------------
   
#   INTERACTION PART
 
#print('\n')
print('Choose your primary ingredient')
ingredients_new = ingredients.copy()
for h,value in enumerate(ingredients):
    print('Press %d for:'%(h),value)
    h+=1;
choice = int(input(''))
print('you have chosen:',ingredients[choice])
combi_chosen = []
print('\n')

for i in [1,2,3]:
    for combination in itertools.combinations(ingredients, i):
        combi_chosen.append(combination)
#print(combi_chosen)  
#print('\n')

new_combi_list = []
for words in combi_chosen:
    new_combi_list.append('+'.join(words))
#print(new_combi_list)
#print('\n')

combi_list_edit =[]
limit =(len(new_combi_list))
for values in range(0,limit):    
    if ingredients[choice] in new_combi_list[values]:
        combi_list_edit.append(new_combi_list[values])
#print('\n')        
#print(combi_list_edit)
for h,value in enumerate(combi_list_edit):
    print('Press %d for:'%(h),value)
    h+=1;
choice1 = int(input(''))
print('you have chosen:',combi_list_edit[choice1])

ha = [combi_list_edit[choice1]]
#print(ha)
test_format = dict([(word, True) for word in combi_list_edit])
print('\n')
#print(test_format)
testing = dict()

#testing combinations for verifying classification
#testing = {'rhum_blanc+vanille': True} #negative
#testing = {'chocolat+lait': True} #positive

testing = dict([(word, True) for word in ha])
#print(testing)

 #-------------------------------------------------------------------------------------------
 
 # RUN ANALYSIS/CLASSIFICATION CODE

if __name__ == '__main__':

  # find word scores
    word_scores = create_word_scores()
    evaluate_features(make_full_dict, None)
    numbers_to_test = [10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 6000, 8000]

    # tries the best_word_features mechanism with each of the numbers_to_test of features
    for num in numbers_to_test:
#        print('evaluating best %d word features' % (num))
        best_words = find_best_words(word_scores, num)
        result = evaluate_newfeatures(best_word_features, best_words, testing)
#       input("Press Enter to continue...")
    print('\n')
    print('It is likely that this drink is rated:', result)
   
#---------------------------------------------------------------------------

#COMMUNICATE TO ARDUINO

ser = serial.Serial('com5',9600)    #Create Serial port object called arduinoSerialData 
print (ser.readline())           #read the serial data and print it as line
    
restart = "r";

milk = "m";       #led1-5
cola ="c";        #led2-4
pineapple = "p";  #led3-3
vodka="v";        #led4-2
berry = "b";      #led5-1
lemon = "l";      #led6-0
ser.write(restart.encode())

ha1 = str(ha)
ha1.split("+")
print(ha1)
if ingredients[0] in ha1:
   ser.write(lemon.encode())
   print(lemon)
if ingredients[1] in ha1:
   ser.write(berry.encode())
   print(berry)
if ingredients[2] in ha1:
   ser.write(vodka.encode())
   print(vodka)
if ingredients[3] in ha1:
   ser.write(pineapple.encode())
   print(pineapple)
if ingredients[4] in ha1:
   ser.write(cola.encode())
   print(cola)
if ingredients[5] in ha1:
   ser.write(milk.encode())
   print(milk)
    
ser.close()   
