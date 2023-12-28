awk 'BEGIN{

}
{
    if($0 ~ /^line/){
        line[$0] = $0;
        this = $0;
    }
    if($1 == "access-class") {
        if($3 == "in") {
            line_in[this] = 1;
        }
        if($3 == "out"){
            line_out[this] = 1;
        }
    }
}
END {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST_3");  
    for(row in line) {
        if(! (row in line_in)){
            print row " ======> has not a in config";
        }
        if(! (row in line_out)){
            print row " ======> has not a out and out config";
        }
    }

} ' ./conf-files/router.unix