awk ' 
BEGIN {
    

}
{
    files[FILENAME] = 1;

    if($0 ~ /^crypto map/){
        crypto_map_def[FILENAME][$3] = $3;
        this = $0;
        this_crypto_map_def = $3; # ex: IPSEC_2_1
        this_ip_sec_policy = $5;
        
    }
    # has peer
    if($1 == "set" && $2 == "peer" && $3 ~ /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/) {
        crypto_map_def_has_peer[FILENAME][this_crypto_map_def] = 1;
    }
    # has ip sec
    if($1 == "set" && $2 == "transform-set" ) {
        crypto_map_def_has_ipsec_policy[FILENAME][this_crypto_map_def] = 1;
    }

    # match address
    if($1 == "match" && $2 == "address" ) {
        crypto_map_def_has_ip_filtering[FILENAME][this_crypto_map_def] = $3;
    }
    
    # access list
    if($1 == "access-list") {
        access_list[$2] = 1;
    }
    
    # interface has crypto-map ref
    if($0 == "interface" && $1 ~ /^FastEthernet/) {
        fast_ethernet_has_crypto_map[FILENAME][$1] = 0;
        this_fast_ethernet = $1;
    }
    if($0 ~ /^ crypto map/){
        fast_ethernet_has_crypto_map[FILENAME][this_fast_ethernet] = $3;
    }

    
} 
END {
    print("TEST_NAME: TEST__9");  
    print("");
    for(file in files) {
        file_has_conf = 0;
        
        for(crypto_map in crypto_map_def[file]) {
            file_has_conf = 1;
            file_has_conf_with_peer = 0;
            if(crypto_map_def_has_peer[file][crypto_map] == 1){
                file_has_conf_with_peer = 1
            } 
            if(!(crypto_map_def_has_ipsec_policy[file][crypto_map] == 1)) print "No ipsec policy found for " crypto_map  " in file " file;
            if(!(access_list[crypto_map_def_has_ip_filtering[file][crypto_map]] == 1)) print "No corresponding declaration ip filtering found for " crypto_map  " in file " file;
            #print file crypto_map_def[file][crypto_map];
            if(file_has_conf_with_peer == 0) print "No configuation crypto map with peer in " file;
            if(file_has_conf_with_peer == 0) print file;
            if(file_has_conf_with_peer == 0) print crypto_map;
        }
        for (interface in fast_ethernet_has_crypto_map[file]){
            
            if(!(length(crypto_map_def[file][fast_ethernet_has_crypto_map[file][interface]]) > 0)) print "No declared crypto map used in " file " for interface " interface;
        }
        if(file_has_conf == 0) print "No configuation crypto map found in " file;
    }
}' ./conf-files/conf*.unix


# print("FILENAME: " FILENAME);  
#    print("TEST_NAME: TEST__9");  
#    print("");
#    for(file in files) {
#        file_has_crypto_map = 0;
#        file_has_crypto_map_with_ip_sec = 0;
#        for(crypto_map in crypto_map_def[FILENAME]) {
#            if(crypto_map_def[FILENAME][crypto_map] != "") file_has_crypto_map = 1;
#            if(crypto_map_def_has_ipsec_policy[FILENAME][crypto_map] == 1) file_has_crypto_map_with_ip_sec = 1;
#        }
#        if(file_has_crypto_map == 0) print "in " file ", for " crypto_map_def[FILENAME][crypto_map] " has not crypto map configuration";
#        if(file_has_crypto_map_with_ip_sec == 0) print "in " file ", for " crypto_map_def[FILENAME][crypto_map] " has crypto map but no ipsec policy";
#
#
#    }
#
#    for(fast_ethernet in fast_ethernet_has_crypto_map[FILENAME]){
#        if(fast_ethernet_has_crypto_map[FILENAME][fast_ethernet] == 0) print fast_ethernet " has no crypto map ref";
#    }
