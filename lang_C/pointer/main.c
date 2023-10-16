#include <stdio.h>

int main(int argc, char * argv[]){

    int a = 52;
    int* c = NULL;

    printf("La vairable a contient %d \n", a);
    printf("La vairable c contient %p \n", c);

    c = &a;


    printf("La vairable *c contient %d \n", *c);
    printf("La vairable c contient %p \n", c);
    printf("La vairable &a est l'adress de an contenue dans c, et quand on fait *c, on a la valeur de a  %p \n", &a);
    
    return 0;

}
