#include <stdio.h>

int main(int argc, char * argv[]){

    FILE * file_pointer;

    file_pointer = fopen("input.txt", "r");

    int number;


    fscanf(file_pointer, "%d\n", &number);
    printf("%d", number);
    printf("------");
    
    FILE * file_pointer_target ;
    file_pointer_target = fopen("output.txt", "w+");
    
    fprintf(file_pointer_target, "%d\n", number * 2);
    while(fscanf(file_pointer, "%d\n", &number) != EOF){

        fprintf(file_pointer_target, "%d\n", number * 2);
        printf("%d", number);
        printf("------");
    }

    fclose(file_pointer);  

    printf("      \n\n\n");

    return 0;

}
