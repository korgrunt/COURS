#include <stdio.h>



void modifyValue(int * toModify){


    *toModify = 777;
    return;

}

int main(int argc, char * argv[]){


    int a = 9;
    printf("Variable has value %d \n", a);

   
    modifyValue(&a);


    printf("Variable now has value %d \n", a);
    return 0;

}
