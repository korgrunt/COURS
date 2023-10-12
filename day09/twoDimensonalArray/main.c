#include <stdio.h>
#include <stdlib.h>




int main(int argc, char * argv[]){

    int X = 9;
    int Y = 10;

    printf("step1 \n");
    int ** damier = malloc(X * sizeof(int * ));


    printf("step2 \n");
    for(int i = 0; i < X; i++){

        damier[i] = malloc(Y * sizeof(int));
    }


    printf("step3 \n");
    for(int i = 0; i < X; i++){

        for(int a = 0; a < Y; a++){

            damier[i][a] = 99;
        }
    }

    printf("step4 \n");


    for(int i = 0; i < X; i++){

        if(i  != X - 1){
        for(int a = 0; a < Y; a++){

            printf("%d", damier[i][a]);
            printf("\n");
            printf("nextSpace\n");
            printf("%d", damier[i+1][a+1]);
        }
        }
        printf("\n");
    }

    printf("step5 \n");

    for(int i = 0; i < X; i++){

        free(damier[i]);
    }
    free(damier);
    return 0;

}
