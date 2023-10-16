#include <stdio.h>

int main(int argc, char * argv[]){

    int varInt = 0; 
    char varChar = 0; 

    // stop if agrument for convertion is invalid
    if(argc != 2){
        printf("Not enough arg, yyou should provide a for asci2int or i for int2ascii ! ");
        return 0;
    }

    // mode asci to int
    if(argv[1][0] == 'a') {
        printf("Veuillez saisir un char: ");
        scanf("%c", &varChar); // save as char
        printf("Vous avez saisie : %d\n  ", varChar); // print as int
        return 1;

    // mode int to asci
    } else if(argv[1][0] == 'i') {

        printf("Veuillez saisir un entier: ");
        scanf("%d", &varInt); // save as int
        printf("Vous avez saisie : %c\n  ", varInt); // print as char
        return 0;

    // Error bad argument for conversion mode
    } else {
        printf("Erreur de saisie ! ");
    }

    return 0;

}
