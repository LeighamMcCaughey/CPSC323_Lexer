## COMPILER SUDO CODE

"""
# establish an array of all the operators, seperators, keywords so we can reference them l8r
# create empty array where the first element is either the word keyword, idetifier, integer, real, seperator, or operator
# this is linked to all of the tokens in the code so itll b like (keyword, if) in an array

if token == [something that starts with a letter] {
    if token == keyword (reference array of keywords from the top) {
        add (keyword, [whatevr thing was determined to be a keyword])
    }
    else {
        //token == identifier;
        put through DFSM :standing_man:
        add (identifier, [whatevr thing was determined to be a identifer])
    }
}

if token == [anything in the operators array] {
    add (operator, [whatever is an operator])
}
if token == [anything in seperator] {
    add (seperator, [whatever is an seperator])
}
if token == [anything in seperator] {
    add (seperator, [whatever is an seperator])
}
if token == [something starting with a number] {
    if (d+) {
        //integer... i think
        put through DFSM :)
        add (integer, [whatever is an integer])
    }
    if (d+.d*) {
        //real
        put through DFSM :)
        add (real, [whatever is an real])
    }
}

DFSM for identifiers {
    whatever makes an identifier dsfm :)
}

DFSM for integer {
    whatever makes an integer dsfm :)
}

DFSM for real {
    whatever makes an real dsfm :)
}

"""

import lexer

with open('input.txt', 'r') as file:
    input = file.read()

tokens = lex(input)

with open('output.txt', 'w') as file:
    for token in tokens:
        file.write(f'<{token[1]}, "{token[0]}">\n')