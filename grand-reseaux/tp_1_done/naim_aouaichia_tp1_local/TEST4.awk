awk 'BEGIN{

}
{
    if($0 ~ /^interface/){
        this = $0;
        interface_valid_ip[this] = 0;
        interface_has_access_group[this] = 0;
    }
    if($1 == "ip" && $2 == "address" && $3 ~ /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/) {
        interface_valid_ip[this] = 1;
    }
    if($2 == "access-group") {
        interface_has_access_group[this] = 1;
    }
}
END {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST_4");  
    for(row in interface_valid_ip) {
        if(interface_valid_ip[row] == 1 && interface_has_access_group[row] == 1){
            print row " ======> has an access goupe";
        } else {
            print row " ======> has not access goupe";
        }
        
    }

} ' ./conf-files/router.unix