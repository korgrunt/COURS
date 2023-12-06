awk 'BEGIN{
    is_snmp_community_ro = 0; 
}
{
    if($0 ~ /^snmp-server/ && $3 == "RO" && NF == 5) {
        is_snmp_community_ro = 1;
    } 
}
END {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST_2");  
    if(is_snmp_community_ro == 1){
        print("snmp-server is set in READ ONLY");
    } else {
        print("snmp-server is not set in READ ONLY");
    }
} ' ./conf-files/router.unix