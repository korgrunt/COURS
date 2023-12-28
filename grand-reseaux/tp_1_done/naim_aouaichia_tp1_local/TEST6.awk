awk '
{
    if($0 ~ /^interface/){
        this = $0;
        interface_mode_trunk[FILENAME][this] = 0;
        interface_trunk_encapsulation[FILENAME][this] = 0;
        interface_native_vlan[FILENAME][this] = 0;
        interface_allowed_vlan[FILENAME][this] = 0;
        interface_port_security[FILENAME][this] = 0;
        interface_mode_access[FILENAME][this] = 0;
    }
    if($2 == "mode" && $3 == "trunk") {
        interface_mode_trunk[FILENAME][this] = 1;
    }
    if($2 == "trunk" && $3 == "encapsulation") {
        interface_trunk_encapsulation[FILENAME][this] = 1;
    }
    if($2 == "trunk" && $3 == "native" && $4 == "vlan") {
        interface_native_vlan[FILENAME][this] = 1;
    }
    if($2 == "trunk" && $3 == "allowed" && $4 == "vlan") {
        interface_allowed_vlan[FILENAME][this] = 1;
    }
    if($2 == "port-security") {
        interface_port_security[FILENAME][this] = 1;
    }
    if($2 == "mode" && $3 == "access") {
        interface_mode_access[FILENAME][this] = 1;
    }
    
} 
END {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST_6");  
    print("");  
    for(filename in interface_mode_trunk) {

        for(interface in interface_mode_trunk[filename]) {
   
            if (interface_mode_trunk[filename][interface] == 1) {
                

                if (interface_trunk_encapsulation[filename][interface] == 0) {
                    print "Interface " interface " in mode trunk, in file" filename;
                    print "Error: N'\''implémente pas « trunk encapsulation »\n";            
                }
                if (interface_native_vlan[filename][interface] == 0) {
                    print "Interface " interface " in mode trunk, in file" filename;
                    print "Error: N'\''implémente pas « native vlan »\n";
                }
                if (interface_allowed_vlan[filename][interface] == 0) {
                    print "Interface " interface " in mode trunk, in file" filename;
                    print "Error: N'\''Implémente pas « allowed vlan »\n";
                } 
                if (interface_port_security[filename][interface] == 1) {
                    print "Interface " interface " in mode trunk, in file" filename;
                    print "Error: Implémente « port security »\n";
                } 
                if (interface_mode_access[filename][interface] == 1) {
                    print "Interface " interface " in mode trunk, in file" filename;
                    print "Error: Implémente « mode access »\n";
                }  
                
            } 
            
            
        }
    }
    
} ' ./conf-files/cat*.unix