# import tokens

operators = ['=', '!=', '==', '<=', '>=', '<', '>', '+', '-', '*', '/']
separators = [')', '(', ';', ':', ',', '.', '{', '}', '@']

# list of numbers
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# list of letters
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] 

# list of keywords
keywords = ['integer', 'boolean', 'real', 'if', 'else', 'return', 'put', 'get', 'while', 'true', 'false', 'fi']



# keyword_class = {
#     'integer' : 'INT', 
#     'boolean' : 'BOOL', 
#     'real' : 'REAL', 
#     'if' : 'IF', 
#     'else' : 'ELSE', 
#     'return' : 'RETURN', 
#     'put' : 'PUT', 
#     'get' : 'GET', 
#     'while' : 'WHILE', 
#     'true' : 'TRUE', 
#     'false' : 'FALSE', 
#     'fi' : 'FI'
# }

def lex(text):
    tokens = []
    i = 0

    while i < len(text):
        #point to the current character
        char = text[i]

        #comment
        if char == '!' and not (i + 1 < len(text) and text[i+1] == '='):
            j = i + 2
            while j < len(text) and text[j] != '!':
                j += 1
            i = j + 1 #skips the closing "!"
            continue

        #ignoring whitespaces
        if char.isspace():
            i += 1
            continue

        #for operators
        twoChar = text[i:i+2]
         #checks for operators like != and <=
        if twoChar in operators:
            tokens.append((twoChar, 'operator'))
            i += 2
            continue
        if char in operators:
            tokens.append((char, 'operator'))
            i += 1
            continue

        #for seperatprs
        if char in separators:
            tokens.append((char, 'separator'))
            i += 1
            continue

        #keywords
        if char.isalpha():
            j = i + 1
            while j < len(text) and text[j] in letters:
                j += 1

            word = text[i:j]

            if word in keywords:
                tokens.append((word, 'keyword'))
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
        if char.isdigit() or ((char == '+' and text[i+1].isdigit()) or (char == '-' and text[i+1].isdigit())):
            j = i + 1

            has_dot = False
            while j < len(text) and (text[j].isdigit() or text[j] == '.'):
                if text[j] == '.':
                    has_dot = True
                j += 1

            if has_dot:
                if text[j-1] == '.':
                    tokens.clear() #maybe change so dont clear whole tokens list
                    tokens.append(('number after dot was expected', 'ERROR'))
                    return tokens
                tokens.append((text[i:j], 'real'))
            else: 
                tokens.append((text[i:j], 'integer'))
            i = j
            continue 
        tokens.append((char, 'ERROR'))
        i += 1

    return tokens

with open('input.txt', 'r') as file:
    input = file.read()

tokens = lex(input)

with open('output.txt', 'w') as file:
    file.write('token\tlexeme\n')
    for token, token_type in tokens:
        file.write(f'{token_type}\t{token}\n')


        class FSM:
            def __init__(self, start_state, states, transitions):
                self.start_state = start_state
                self.states = states 
                self.transitions = transitions # dict: (state, input) -> next_state

            def run(self, input_str):
                state = self.start_state
                for ch in input_str:
                    next_state = self.transitions.get((state, ch))
                    if next_state is None:
                        raise ValueError(f"No transition from {state} on {ch}")
                    state = next_state
                return state

            states = {'start', 'digit', 'letter', 'end'}
            transitions = {
                ('start', 'a'):'letter',
                ('start', '1'):'digit',
                ('start', 'a'):'letter', #letter not character
                ('start', '1'):'digit', # twice
                ('start', ''):'end',
                ('start', ''):'end', #not meaningful
            }

            fsm=FSM('start', states, transitions)
            print(fsm.run(input)) # 'end'


                




