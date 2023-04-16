student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (index,value) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def get_nato_alphabet():
    
    user_input = input("Enter a word for Nato phonetic translation: ").upper()
    try:
        output_message = [nato_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        get_nato_alphabet()
    else: 
        print(output_message)  
        
  
get_nato_alphabet()