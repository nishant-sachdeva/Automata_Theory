import json


with open('input.json') as json_file:
    data = json.load(json_file)
    for p in data:
        pass
        # print (p, " : ", data[p])

# this gives me the input file just the way I want it

input_number_of_states = data['states']  # this just gave me the number of states
input_alphabet = data['letters']

input_function = data['t_func']

input_start = data['start']

input_final = data['final']

# we now have the parameters to start our work with, now we will construct the output dfa
output_number_of_states = pow(2, input_number_of_states)
outut_alphabet = input_alphabet
output_start = input_start

# output_function banana padhega , and output states bhi,

for state in range(0,output_number_of_states):
    # we will make the dfa for this state now,
     
    