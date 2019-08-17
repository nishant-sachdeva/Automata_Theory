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

output_states = []
output_final = []

for i in range (0, pow(2, input_number_of_states)):
    # now we will run that exponential thing
    state = []
    for j in range(0, input_number_of_states):
        if (i & (1<<j)):
            # then that means that weight in valid
            state.append(j)
    output_states.append(state)
    for j in state:
        if j in input_final:
            output_final.append(state)
            


# we have all the output states now, 
# presently we will start forming the output values

modified_input = {}

for ele in input_function:
    a = str(ele[0])
    b = ele[1]
    c = a + b
    modified_input[c] = ele[2]


# print(modified_input)
output_function = []

for state in output_states:
    for letter in input_alphabet:
        # I have to form a list that will have the current state
        cur = []
        cur.append(state)
        cur.append(letter)
        codomain = []
        # that gives me the elements, now I have to form the output
        for s in state:
            c = str(s) + str(letter)
            if c in modified_input:
                codomain.extend(modified_input[c])
        set(codomain)
        list(codomain)
        cur.append(codomain)

        output_function.append(cur)


for output in output_function:
    print(output)


output = {}

output['states'] = pow(2, input_number_of_states)
output['letters'] = input_alphabet
output['t_func'] = output_function
output['start'] = 0
output['final'] = output_final

with open('output.json', 'w') as outfile:
    json.dump(output, outfile)




