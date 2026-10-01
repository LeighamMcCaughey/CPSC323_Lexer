
#define our token names

TOK_OPERATOR = ['!=', '==', '<=', '>=', '<', '>', '+', '-', '*', '/']
TOK_KEYWORD = ['integer', 'boolean', 'real', 'if', 'else', 'return', 'put', 'get', 'while', 'true', 'false', 'fi']
TOK_SEPERATOR = [')', '(', ';', ':', ',', '.', '{', '}', '@']
TOK_IDENTIFIER = ''
TOK_INTEGER = ''
TOK_REAL = ''
TOK_UNKNOWN = ''

# list of numbers
DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# list of letters
LETTER = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] 



