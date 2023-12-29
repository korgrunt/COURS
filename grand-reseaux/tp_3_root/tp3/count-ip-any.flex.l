%{
#include <stdio.h>

int count_ip = 0;
int count_any = 0;

%}

%%

ip    { count_ip++; }
any   { count_any++; }



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

    printf("Nombre de mots 'ip': %d\n", count_ip);
    printf("Nombre de mots 'any': %d\n", count_any);

    return 0;
}