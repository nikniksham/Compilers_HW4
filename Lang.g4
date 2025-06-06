grammar Lang;

// Parser Rules
program: statement* EOF;

statement
    : assignment_statement
    | if_statement
    | while_statement
    | print_statement
    ;

assignment_statement: ID EQ expression SEMI;
if_statement: IF LPAREN expression RPAREN LBRACE program RBRACE (ELSE LBRACE program RBRACE)?;
while_statement: WHILE LPAREN expression RPAREN LBRACE program RBRACE;
print_statement: PRINT expression SEMI;

expression
    : expression (MUL | DIV) expression # MulDivExpr
    | expression (ADD | SUB) expression # AddSubExpr
    | expression (LT | GT | LTE | GTE | EQEQ | NEQ) expression # CompExpr
    | atom                               # AtomExpr
    ;

atom
    : INT
    | FLOAT
    | STRING
    | ID
    | LPAREN expression RPAREN
    ;

// Lexer Rules
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
PRINT   : 'print';

ID      : [a-zA-Z_][a-zA-Z_0-9]*;
INT     : [0-9]+ | '-'[0-9]+; // Support for signed integers
FLOAT   : [0-9]+'.'[0-9]+ | '-'[0-9]+'.'[0-9]+; // Support for signed floats
STRING  : '\'' (~['\\] | '\\' .)* '\'' | '"' (~["\\] | '\\' .)* '"'; // String literals with escape sequences

MUL     : '*';
DIV     : '/';
ADD     : '+';
SUB     : '-';

EQ      : '=';
EQEQ    : '==';
NEQ     : '!=';
GT      : '>';
LT      : '<';
GTE     : '>=';
LTE     : '<=';

LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
SEMI    : ';';

WS      : [ \t\r\n]+ -> skip; // Skip whitespace
COMMENT : '//' .*? '\r'? '\n' -> skip; // Skip single-line comments, handle both line ending styles