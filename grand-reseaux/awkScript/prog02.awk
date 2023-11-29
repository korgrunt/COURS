awk '{
    if($1 == "interface") print $0;
}' ./../router.unix.txt