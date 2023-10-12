#include <stdio.h>
#include <stdlib.h>




int main(int argc, char * argv[]){

    int X = 9;
    int Y = 10;
    int Z = 10;

    printf("step1 \n");
    int *** damier = malloc(X * sizeof(int ** ));


    printf("step2 \n");
    for(int i = 0; i < X; i++){

        damier[i] = malloc(Y * sizeof(int *));

        for(int idx = 0; idx < Y; idx++){

            damier[i][idx] = malloc(Z * sizeof(int));

        }
    }


    printf("step3 \n");
    for(int i = 0; i < X; i++){

        printf("step3.1 %d\n", i);
        for(int a = 0; a < Y; a++){

            printf("step3.2 %d\n", a);
            for(int c = 0; c < Z; c++){

                printf("step3.3 %d\n", c);
                damier[i][a][c] = 1;
            }
        }
    }

    printf("step4 \n");


    for(int i = 0; i < X; i++){

        for(int a = 0; a < Y; a++){

            for(int b = 0; b < Z; b++){

                printf("%d", damier[i][a][b]);
            }
            printf("Last dimension printed\n");
        }
        printf("Two dimension printed\n");
    }
    printf("First dimension printed\n");

    printf("step5 \n");

    for(int i = 0; i < X; i++){

        for(int e = 0; e < Y; e++){

            free(damier[i][e]);
        }
        free(damier[i]);
    }
    free(damier);
    return 0;

}
