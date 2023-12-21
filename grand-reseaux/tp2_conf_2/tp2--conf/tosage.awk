gawk '
BEGIN{
    print("g=DiGraph()");
}
{
    if($2 != $4){
        print("g.add_edges([(\"" $2 "\",\""$4 "\")])");
    }

}
END {
    print("g.show(layout=\"graphviz\", edge_labels=True, figsize=[8,8], edge_color=\"blue\") ");
    print("g.connected_components()");
}' ./joined.txt
