#!/bin/awk -f

# ./pe-guillaume.awk pe*
BEGIN{
    print("g=DiGraph()");
}
{

    
    if($0 ~ /^hostname/ ) {
        hostname=$2
    }
    
    if($0 ~ /^ ip address/ ) {
        ip_as=$3
        
    }
    
    if($0 ~ /^router/ ) {
        air[ip_as]=$3
    }

    if($0 ~ /^ neighbor/ ) {
        if($3 == "remote-as"){
            print("g.add_edges([(\"" ip_as "\",\"" $2 "\")])  "air[ip_as]" "$4"") 
            print("g.add_edges([(\"" $2 "\",\"" ip_as "\")])  "$4" "air[ip_as]"")
        }
    }
    

}
END {
    print("g.show(layout=\"graphviz\", edge_labels=True, figsize=[8,8], edge_color=\"blue\") ");
    print("g.connected_components()");
}
