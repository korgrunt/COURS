#include <stdio.h>
#include <stdlib.h>




int main(int argc, char * argv[]){

    printf("Start programm");

    int n = 9;
    char * a = malloc((n + 1) * sizeof(char));
   
    printf("My arg is %d", n);
  
    




    int i = 0;
    while(i < n ){
        a[i] = 'a';
        printf("%c", a[i]);
        i++;
   
    }


    printf("\n______________________\n");
    for(int b = 0; a[b] != '\0'; b++){

        printf("%c", a[b]);
        i++;
   
    }

    printf("%c", '\n');
    free(a); 
    return 0;

}
