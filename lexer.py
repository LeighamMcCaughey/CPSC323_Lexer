

#arrays of all lexeme token names

operators = ['=', '!=', '==', '<=', '>=', '<', '>', '+', '-', '*', '/']
separators = [')', '(', ';', ':', ',', '.', '{', '}', '@']

# list of numbers
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# list of letters
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] 

# list of keywords
keywords = ['integer', 'boolean', 'real', 'if', 'else', 'return', 'put', 'get', 'while', 'true', 'false', 'fi']

#names each character
def char_class(c):
    if c.isdigit(): return 'digit'
    if c.isalpha(): return 'letter'
    if c == '.':    return 'dot'
    return 'other'

#FSM :party:
class FSM:
    def __init__(self, transitions, accepting, start='S'):
        self.transitions = transitions  # dict: (state, char_class) -> next_state
        self.accepting = accepting # dict: state -> token
        self.start = start

    def run(self, input_str, i):
        state = self.start #the starting state
        last_accept = None # the tokken typefor the longest accepted token
        last_end = i #the index right after last_accept

        #these are our pointers helping us step through the code
        j = i 

        #while the pointer is smaller than the length of the input
        #go to the next transtion and get that information
        #if the next transition doesnt exist, break
        while j < len(input_str):
            next_transition = self.transitions.get((state, char_class(input_str[j])))
            if next_transition is None:
                break
            state = next_transition
            j += 1
            
            if state in self.accepting: # if state does exist,
                #pointer goes one forward
                #if the state is an accepting state, the whole token can be read
                #stores 2 things: the token type, and the index
                last_accept = self.accepting[state]
                last_end = j
        return last_accept, last_end #return the whole accepted token and the index where it ended

#create the int and real lexer object

number_fsm = FSM(
    transitions={('S','digit'):'INT', ('INT','digit'):'INT',
                 ('INT','dot'):'DOT', ('DOT','digit'):'REAL',
                 ('REAL','digit'):'REAL'},
    accepting={'INT':'integer', 'REAL':'real'},
)

#create the identifier lexer object
identifier_fsm = FSM(
    transitions={('S','letter'):'ID', ('ID','letter'):'ID', ('ID','digit'):'ID'},
    accepting={'ID':'identifier'},
)

#main lexer
def lex(text):
    tokens = []
    i = 0

    while i < len(text):
        #point to the current character
        char = text[i]

        #comment
        if char == '!' and not (i + 1 < len(text) and text[i+1] == '='):
            j = i + 1
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

        # for ID and keywords
        if char.isalpha(): # if character is in the alphabet
            #call the FSM !! :)
            token_type, end = identifier_fsm.run(text, i)
            word = text[i:end]
            if word in keywords:
                tokens.append((word, 'keyword'))
            else:
                tokens.append((word, 'identifier'))
            i = end
            continue
        #for ints and reals
        if char.isdigit(): #if character is a digit
            token_type, end = number_fsm.run(text, i)
            tokens.append((text[i:end], token_type))
            i = end
            continue

    return tokens

with open('input.txt', 'r') as file:
    input_text = file.read()

#tokens = lex(input_text)
i = 0
with open('output.txt', 'w') as output:
    file.write('token\tlexeme\n')
    while True:
        token_type, lexeme, i = lex(input_text, i)
        if token_type is None:
            break
        output.write(f'{token_type}\t{lexeme}\n')


                




