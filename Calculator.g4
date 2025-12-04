grammar Calculator;

start : variable_assignments? expr      #startCont
      ;

variable_assignments 
  : LEFT_BRACE assignments RIGHT_BRACE      #bracesAssig
      ;

assignments 
  : assignment (COMMA assignment)*          #multipleAssig
      ;

assignment 
  : VAR EQUAL expr                   #assig
      ;

expr:    left=expr op=(PLUS|MINUS) right=expr  # OpExpr
    |    left=expr op=(MULTIPLY|DIVIDE) right=expr  # OpExpr
    |    atom=INT                           # AtomExpr
    |   variable=VAR                       # VarExpr
    |    '(' expr ')'                       # ParenExpr
    ;

// tokens expressed as regular expressions
INT : [0-9]+ ;
VAR : [a-zA-Z_][a-zA-Z0-9_]* ;
WS  :   [ \t]+ -> skip ;
LEFT_BRACE : '{' ;
RIGHT_BRACE : '}' ;
COMMA : ',' ;
LEFT_PAREN : '(' ;
RIGHT_PAREN : ')' ;
PLUS : '+' ;
MINUS : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/' ;
EQUAL : '=' ;