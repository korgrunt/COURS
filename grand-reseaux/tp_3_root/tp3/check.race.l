%{
#include <stdio.h>
#include <unistd.h>

char filename[200];
char interface[100];
short ip_valide;
short access_group;








%}

%x INTERFACE

%%

^interface[ ].*$    { 
    snprintf(interface,100,"%s",yytext);
    access_group = 0;
    BEGIN INTERFACE;
}
(.|\n)           ;

<INTERFACE>^[ ]ip[ ]access-group[ ].*$   { 
    access_group =1;
}
<INTERFACE>(.|\n)   ;
<INTERFACE>^!$  {
    if(access_group == 0){
        fprintf(yyin, "%s interface %s missing ip access-group\n", filename, interface);
    }
    BEGIN INITIAL;
}


%%


int main(int argc, char **argv ) {
    int i;

    
    const pid_t id = getpid();
    


    for(i=1;i<argc;i++) {
        sprintf(filename, "./output_process_%i.txt", id);

     //strncpy(filename,argv[i],strlen(argv[i]));

    //filename[strlen(argv[i])] = '\0';
    printf(yyin);
    printf("%s\n", filename);
    yyin = fopen( filename, "w" );

    if (yyin != NULL) {
           yylex();
         //fclose();
     } else {
           perror("FILE OPEN ERROR");
           exit(1);
     }
   }
}