%{
#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024
#define MAX_STRINGS 100

char* acls_def[MAX_STRINGS];
int acl_def_idx = 0;

char* acls_ref[MAX_STRINGS];
int acl_ref_idx = 0;

char current_line[MAX_LINE_LENGTH];



%}

%x ACLEXTENDED
%x ACLSTANDARD

%%


^ip[ ]access-list[ ]extended.*$       { 
    printf("\ndetected def extended \n" );
    // ecrire une regext pour extraire le dernier mot de la ligne de strdup(yytext)
    
    acls_def[acl_def_idx] = strrchr(strdup(yytext), ' ') + 1;
    acl_def_idx++;

}

^access-list[ ].*$       { 
    printf("\ndetected def standard \n");
    // extract second word of strdup(yytext)
    char * elm = strtok(strdup(yytext), " ");
    char *array[128];
    int i = 0;
    while (elm != NULL)
    {
        array[i++] = elm;
        elm = strtok (NULL, " ");
    }

    acls_def[acl_def_idx] =  array[1];
    
    acl_def_idx++;
}

^[ ]access-class[ ].*$       {
    printf("\ndetected ref\n"); 

    char * elm = strtok(strdup(yytext), " ");
    char *array[128];
    int i = 0;
    while (elm != NULL)
    {
        array[i++] = elm;
        elm = strtok (NULL, " ");
    }

    acls_ref[acl_ref_idx] =  array[1];    
    acl_ref_idx++;


}

^[ ]ip[ ]access-group[ ].*$       {
    printf("\ndetected ref\n"); 
    char * elm = strtok(strdup(yytext), " ");
    char *array[128];
    int i = 0;
    while (elm != NULL)
    {
        array[i++] = elm;
        elm = strtok (NULL, " ");
    }

    acls_ref[acl_ref_idx] =  array[2];    
    acl_ref_idx++;

    /*
    for (int i = 0; i < acl_def_idx; i++) {
        printf("\n%s\n", acls_def[i]);
    }
    for (int i = 0; i < acl_ref_idx; i++) {
        printf("\n%s\n", acls_ref[i]);
    }
    */
    printf("\n__end___\n");

}


(.|\r\n|\n) ;


<<EOF>> {
    for (int idx_def = 0; idx_def < acl_def_idx; idx_def++) {
        int found = 0;
        for (int idx_ref = 0; idx_ref < acl_ref_idx; idx_ref++) {
            if (strcmp(acls_def[idx_def], acls_ref[idx_ref]) == 0) {
                found = 1;
            }
        }
        if (found == 0) {
            printf("\ndef not ref => %s\n", acls_def[idx_def]);
        }
    }
    
    for (int idx_ref = 0; idx_ref < acl_ref_idx; idx_ref++) {

        int found = 0;
        for (int idx_def = 0; idx_def < acl_def_idx; idx_def++) {

            if (strcmp(acls_def[idx_def], acls_ref[idx_ref]) == 0) {
                found = 1;
            }
        }
        if (found == 0) {
            printf("\nref not def => %s\n", acls_ref[idx_ref]);
        }
    }
    printf("Fin du fichier détectée\n");
    return 0; 
}
%%

int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }
   
    FILE* file = fopen(argv[1], "r");

/*
Aide moi a detecter les ACLs declarer, et les ACLs appeler, dans le fichier router.unix
et les stocker dans les tableaux acls_def et acls_ref,
pour ensuite afficher les def qui ne sont pas dans ls ref et les ref qui ne sont ps dansl les def.
en flex bison, ok ? 
Répind copilot ? 

*/
  
    acls_ref[1] = "helllo222";

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    yyin = file;
    yylex();

    fclose(file);

    return 0;
}
