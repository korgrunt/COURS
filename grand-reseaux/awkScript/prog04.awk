awk '
BEGIN{
    i = 0;
}
{
    if($1 == "interface") {
        i++;
        interface[i] = $0;
    }
    if($1 == "ip" && $2 == "address") interface_ip[i] = $0;
} END {
    for(id in interface) {
        print id, interface[id], interface_ip[id];
    }

}' ./../router.unix.txt