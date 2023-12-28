#!/bin/awk -f

BEGIN{
     print("g=DiGraph()");
}
{
  if ($0 ~ /^crypto map/) {
    last_ipsec = $3;
    ip_dest_index = 0;
  } else if ($0 ~ /^ set peer/) {
    ip_sec[last_ipsec]["dest"][ip_dest_index] = $3;
    ip_dest_index++;
  } else if ($0 ~ /^ ip address/) {
    last_ip_src = $3;
    ip_src_index = 0;
    interfaces[last_ip_src] = last_interface;
  } else if ($0 ~ /^ crypto map/) {
    ip_sec[$3]["src"][ip_src_index] = last_ip_src;
    ip_src_index++;
  } else if ($0 ~ /^interface/) {
    last_interface = $2;
  }

}
END {

    # Ajouter les nœuds
    for(ipsec in ip_sec) {    
        
        for(ipsrc_idx in ip_sec[ipsec]["src"]) {
            ip_src_vertice = "@" ip_sec[ipsec]["src"][ipsrc_idx] "(" interfaces[ip_sec[ipsec]["src"][ipsrc_idx]] ")";
            print("g.add_vertices([\"" ip_src_vertice "\"])")

            for(ipdest_idx in ip_sec[ipsec]["dest"]) {
                ip_dest_vertice = "@("  ip_sec[ipsec]["dest"][ipdest_idx] ")";

                print("g.add_vertices([\"" ip_dest_vertice "\"])")

                print("g.add_edges([(\"" ip_src_vertice "\",\"" ip_dest_vertice "\")])");
            }
        }
    }


   
    print("g.show(vertex_size=0.2, figsize=5)");
    print("g.connected_components()");

}
