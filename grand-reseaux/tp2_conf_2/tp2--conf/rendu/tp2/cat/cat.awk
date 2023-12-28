#!/bin/awk -f

BEGIN{
     print("g=DiGraph()");
}
{
  if ($0 ~ /^hostname/) {
    current_catalyst = $2;
  } 
  if ($0 ~ /^interface/) {
    last_interface = $2;
  }
  if ($0 ~/^ switchport trunk allowed vlan/){
    # allowed vlan in catalyst
    split($5, allowed_vlan[current_catalyst]["allowed_vlan"], ",");
    for(vlan in allowed_vlan[current_catalyst]["allowed_vlan"]){
      allowed_vlan[current_catalyst]["allowed_vlan"][vlan] = 1;
    }
  }
  if ($0 ~/^ switchport access vlan/){
    catalysts[current_catalyst][last_interface]["access_vlan"] = $4;

    allowed_vlan[current_catalyst][$4][last_interface] = 1;
  }
  
}
END {

    # print vertice
    for(catalyst in catalysts) {
      allowed_vlan_in_catalyst[0];
      for(interface in catalysts[catalyst]) {
          node = catalyst "-" interface
          print("g.add_vertices([\"" node "\"])");        
      }
        
    }

    # print edges
    for(catalyst in catalysts) {
      for(interface in catalysts[catalyst]) {
        node = catalyst "-" interface
        for(inter in allowed_vlan[current_catalyst][catalysts[catalyst][interface]["access_vlan"]]){
          if(interface != inter){
            print("g.add_edges([(\"" catalyst "-" inter "\",\"" catalyst "-" interface "\")])");

          }
        }
      }
    }
    print("g.show(vertex_size=2, figsize=17)");
    print("g.connected_components()");
}
