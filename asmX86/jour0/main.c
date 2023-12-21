#include <stdio.h>

int my_function(char * str){
   printf("Hello, World!");
   return 1;
}

int main() {
   // printf() displays the string inside quotation
   printf("\n start \n");
   int val = my_function("\n hello world! \n");
   int val_2 = val + 3;
   printf("\n %d end \n ", val_2);
   return 0;
}
