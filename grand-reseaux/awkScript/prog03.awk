awk '{
    if($1 == "interface") interface = $0;
    if($1 == "ip" && $2 == "address") print interface, $0;
}' ./../router.unix.txt