awk 'BEGIN{

}
{
    if($0 ~ /^interface /){
        in_interface = 1;
        interface_name = $2;
        next;
    }
    if($1 == "ip" && $2 == "access-group") {
        has_access_groupe = 1;
        next;
    }
    if($0 ~ /^!/){
        if(in_interface == 1 && has_access_groupe == 0){
            print(FILENAME " interface " interface_name "  missing ip access-group");
        }
        in_interface = 0;
        has_access_groupe = 0;
        interface_name = "";
        next;
    }
    
}
END {


} ' $*