#!/bin/awk -f

# ./pe-guillaume.awk pe*
BEGIN{
    print("g=DiGraph()");
}
{

    

    print("g.add_edges([(\"" $2 "\",\"" $3 "\")])") 


}
END {
    print("g.show(layout=\"graphviz\", edge_labels=True, figsize=[8,8], edge_color=\"blue\") ");
    print("g.connected_components()");
}
