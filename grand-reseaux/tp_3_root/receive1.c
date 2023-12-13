int main(int argc, char **argv ) {

 

    int i;

 

    for(i=1;i<argc;i++) {

 

     strncpy(filename,argv[i],strlen(argv[i]));

    filename[strlen(argv[i])] = '\0';

 

    yyin = fopen( argv[i], "r" );

    if (yyin != NULL) {

           yylex();

         fclose(yyin);

     } else {

           perror("FILE OPEN ERROR");

           exit(1);

     }

   }

}