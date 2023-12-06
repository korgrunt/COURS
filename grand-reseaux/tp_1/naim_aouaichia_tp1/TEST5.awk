awk '{
    # def
    if($1 == "ip" && $2 == "access-list" && $3 == "extended") acl_def[$4] = $0;
    if($1 == "access-list") acl_def[$2] = $0;
    
    # ref
    if($1 == "ip" && $2 == "access-group") acl_ref[$3] = $0;
    if($1 == "access-class") acl_ref[$2] = $0;
    if($1 == "snmp-server") acl_ref[$3] = $0;
    
} 
END {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST_5");  
    for(aclRef in acl_ref) {
        if(!(aclRef in acl_def)) {
            print acl_ref[aclRef], " ======> ref pas def";
        }
    }
    for(aclDef in acl_def) {
        if(!(aclDef in acl_ref)) {
            print acl_def[aclDef],  "======> def pas ref";
        }
    }

} ' ./conf-files/router.unix