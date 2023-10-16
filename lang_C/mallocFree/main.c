#include <stdio.h>




int main(int argc, char * argv[]){


    int* a = (int *) malloc(1000 * sizeof(int));
    free(a);
    int* b = (int *) malloc(1000 * sizeof(int));




    return 0;

}
