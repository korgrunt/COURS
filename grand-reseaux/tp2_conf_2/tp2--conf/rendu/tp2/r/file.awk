#!/bin/awk -f

BEGIN{
     print("g=DiGraph()");
}
{
  if ($1 == "ip" && $2 == "address") {
    current_ip_in_as = $3;
  } else if ($1 == "router" && $2 == "bgp") {
    current_as = $3;
  } else if ($1 == "neighbor" && $3 == "remote-as") {
    as_connection[current_as][current_ip_in_as][$4][$2] = 1
    #print current_as " " current_ip_in_as " " $4 " " $2
  } 
}
END {

    # Ajouter les nœuds
    for(asSrc in as_connection) {    
        array_of_as[asSrc] = 1
        for(ipSrc in as_connection[asSrc]) {
            for(asDest in as_connection[asSrc][ipSrc]) {
                array_of_as[asDest] = 1
            }
        }
    }


    for(uniqAs in array_of_as) {
        print("g.add_vertices([\"" uniqAs "\"])")
    }


    for(asSrc in as_connection) {
        
        for(ipSrc in as_connection[asSrc]) {
            for(asDest in as_connection[asSrc][ipSrc]) {
                for(ipDest in as_connection[asSrc][ipSrc][asDest]) {
                    if(as_connection[asSrc][ipSrc][asDest][ipDest] == 1){
                        if(as_connection[asDest][ipDest][asSrc][ipSrc] == 1){
                            print("g.add_edges([(\"" asSrc "\",\"" asDest "\")])");
                            # print asSrc " " asDest " over " ipSrc " " ipDest;
                        } 
                    }
                    
                }
            }
        }

    }

    print("g.show()");
    print("g.connected_components()");

}
