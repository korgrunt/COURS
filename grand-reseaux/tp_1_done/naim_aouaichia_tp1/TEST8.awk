awk ' 
BEGIN {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST__8");  
    print("");  
}
{
    if($1 == "access-list" && $2 == "110"){


        if($4 == "ip"){
            if(!($5 ~ /^192/)) print("Sur le fichier " FILENAME " l'\''access-list 110 ligne " NR " Ne contien pas une ip src de la classe 192.");
            if(!($7 ~ /^192/)) print("Sur le fichier " FILENAME " l'\''access-list 110 ligne " NR " Ne contien pas une ip dest de la classe 192.");
        
        }
    }

    
} ' ./conf-files/conf*.unix