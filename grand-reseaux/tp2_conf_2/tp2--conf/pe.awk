awk 'BEGIN{

}
{
    if(NR == 0){
        hostnames[$0] = $0;
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
    print("PE-VRFname import/export rt")
    for(pe in peList) {
        for(vrf in vrfList[pe]) {
            for(inputOutput in vrfList) {
                vrfList[pe]
            }  
            
        }    
    }

} ' ./pe*