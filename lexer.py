# import tokens

operators = ['!=', '==', '<=', '>=', '<', '>', '+', '-', '*', '/']
seperators = [')', '(', ';', ':', ',', '.', '{', '}', '@']

# list of numbers
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# list of letters
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] 

# list of keywords
keywords = ['integer', 'boolean', 'real', 'if', 'else', 'return', 'put', 'get', 'while', 'true', 'false', 'fi']



keyword_class = {
    'integer' : 'INT', 
    'boolean' : 'BOOL', 
    'real' : 'REAL', 
    'if' : 'IF', 
    'else' : 'ELSE', 
    'return' : 'RETURN', 
    'put' : 'PUT', 
    'get' : 'GET', 
    'while' : 'WHILE', 
    'true' : 'TRUE', 
    'false' : 'FALSE', 
    'fi' : 'FI'
}

def lex(input):
    tokens = []
    i = 0

    while i < len(input):
        #point to the current character
        char = input[i]

        #comment
        if char == '!' and input[i + 1 < len(input)] == '!':
            j = i + 2
            while j < len(input) and input[j] != '\n':
                j += 1
            i = j
            continue

        #ignoring whitespaces
        if char.isspace():
            i += 1
            continue

        #for operators
        if char in operators:
            if i+1 < len(input) and input[i+1] == '=' and char + '=' in operators:
                tokens.append((char + '=', 'operator'))
                i += 2
            else:
                tokens.append((char, 'operator'))
                i += 1
            continue

        #for seperatprs
        if char in seperators:
            tokens.append((char, 'seperator'))
            i += 1
            continue

        #keywords
        if char.isalpha():
            j = i + 1
            while j < len(input) and input[j] in letters:
                j += 1

            word = input[i:j]

            if word in keywords:
                tokens.append((word, keyword_class[word]))
            # identifiers

            # this checks if the second char is not in the 
            # alphabet or numbers or an underscore then error
            elif not word[1:].isalnum() or not word[1:] == '_':
                tokens.clear()
                tokens.append(('invalid ID', 'ERROR'))
                return tokens
            i = j
            continue

        #Ints and floats
        if char.isdigit() or ((char == '+' and input[i+1].isdigit()) or (char == '-' and input[i+1].isdigit())):
            j = i + 1

            has_dot = False
            while j < len(input) and (input[j].isdigit() or input[j] == '.'):
                if input[j] == '.':
                    has_dot = True
                j += 1

            if has_dot:
                if input[j-1] == '.':
                    tokens.clear() #maybe change so dont clear whole tokens list
                    tokens.append(('number after dot was expected', 'ERROR'))
                    return tokens
                tokens.append((input[i:j], 'real'))
            else: 
                tokens.append((input[i:j], 'integer'))
            i = j
            continue 
        tokens.append((char, 'ERROR'))
        i += 1

    return tokens

with open('input.txt', 'r') as file:
    input = file.read()

tokens = lex(input)

with open('output.txt', 'w') as file:
    for token in tokens:
        file.write(f'<{token[1]}, "{token[0]}">\n')


        # class FSM:
        #     def init(self, start_state, states, transitions):
        #         self.start_state = start_state
        #         self.states = states 
        #         self.transitions = transitions # dict: (state, input) -> next_state

        #     def run(self, input_str):
        #         state = self.start_state
        #         for ch in input_str:
        #             next_state = self.transitions.get((state, ch))
        #             if next_state is None:
        #                 raise ValueError(f"No transition from {state} on {ch}")
        #             state = next_state
        #         return state

        #     states = {'start', 'digit', 'letter', 'end'}
        #     transitions = {
        #         ('start', 'a'):'letter',
        #         ('start', '1'):'digit',
        #         ('start', 'a'):'letter',
        #         ('start', '1'):'digit',
        #         ('start', ''):'end',
        #         ('start', ''):'end', 
        #     }

        #     fsm=FSM('start', states, transitions)
        #     print(fsm.run(input)) # 'end'


                




