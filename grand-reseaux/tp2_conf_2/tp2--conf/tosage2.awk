gawk '
BEGIN{
    print("g=DiGraph()");
}
{
    print("g.add_edges([(\"" $2, $4 "\")])");
}
END {
    print("g.show()");
    print("g.connected_components()");
}' ./joined.txt
