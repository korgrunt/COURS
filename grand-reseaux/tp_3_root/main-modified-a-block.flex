%{
#include <stdio.h>
%}

%x INTERFACE

%%
^interface[ ].*$    { 
    printf("Ligne Interface : %s\n",yytext);
    BEGIN INTERFACE;
    }
(.|\n)  ;

<INTERFACE>^[ ]*ip[ ]*address.*$  { printf("----> ip address  %s\n",yytext); }
(.|\n)  ;

<INTERFACE>^!$  { BEGIN INITIAL; }
(.|\n)  ;

%%
int main() {
    yylex();
    return 0;
}


