#include <stdio.h>

int main(){

    int varInt = 0;
    printf("Veuillez saisir un entier: ");

    if(scanf("%d", &varInt) != 1){

        printf("Erreur de saisie ! ");
        return 1;

    }

    printf("Vous avez saisie : %d\n  ", varInt);


}
