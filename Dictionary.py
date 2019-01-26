# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:37:54 2019

@author: Sayantan Ghosh
"""
import json
from difflib import get_close_matches #Library for checking similarities between words
data = json.load(open("data.json"))

def translate(w):
    w = w.lower() #Passing the word into lowercase Alphabet
    if w in data:
          return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        Yn = input("Did you mean %s insted? Enter Y for yes and N for No "% get_close_matches(w,data.keys())[0])
        if Yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif Yn == "N":
            return "The word is incorrect!Please double check it!"
        else:
            return "Sorry!We didnt find the word"


    else:
      return "The Word doesnot exist in our dictionary"
word = input("Enter the word to be search in the dictionary: ")
meaning= translate(word)
if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)
