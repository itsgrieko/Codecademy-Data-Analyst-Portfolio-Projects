"""
Aim of this project is to manipulate and navigate through a given data set of Jeopardy questions, answers, and other information.
"""

import pandas as pd
import os
pd.set_option('display.max_colwidth', None)
pd.set_option('max_columns', None)

LOCATION = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(LOCATION, 'jeopardy.csv')

j_data = pd.read_csv(my_file)
print(j_data.head(5))

#Cleaning column names
j_data.columns=['Show_number','Air_date','Round','Category','Value','Question','Answer']

# Function that filters through the questions to find questions that contain a desired word or list of words
def filter_data(data, words):
	# Changes the words to lowercase
	# Returns true if all words in the list appear in the question
  	filter = lambda x: all(word.lower() in x.lower() for word in words)
  	# Applies the filter to the Question column and returns the rows where the function returned True
  	return data.loc[data["Question"].apply(filter)]

# Test filter_data
#filtered = filter_data(j_data, ["King", "England"])
#print(filtered["Question"])

# Adding a new column that converts value column to floats
j_data.Value = j_data.Value.apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)
#print(j_data.Value)

test_set = filter_data(j_data, ["King", "England"])
avg = test_set.Value.mean()
#print(avg)

def find_unique(filtered_data):
	return filtered_data.Answer.value_counts()

print(find_unique(test_set))