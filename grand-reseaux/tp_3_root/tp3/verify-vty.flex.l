%{
#include <stdio.h>

char current_line[1024];
int access_class_in = 0;
int access_class_out = 0;

%}

%x VTY

%%

^line[ ]vty[ ].*$       { 
    access_class_in = 0;
    access_class_out = 0;
    strcpy(current_line, yytext);
    BEGIN VTY;
}
(.|\n)           ;

<VTY>^[ ]access-class[ ].*in$   { 
    access_class_in = 1;
}
<VTY>^[ ]access-class[ ].*out$   { 
    access_class_out = 1;
}
<VTY>^!$  {
    if (access_class_in == 0 && access_class_out == 0) {
        printf("Error: access-class not set on line vty => %s\n", current_line);
    }
    BEGIN INITIAL;
}

%%

int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE* file = fopen(argv[1], "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    yyin = file;
    yylex();

    fclose(file);

    return 0;
}
