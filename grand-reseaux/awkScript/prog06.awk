awk '{
    if($1 == "interface") {
        interface = $0;
    }
    if($1 == "ip" && $2 == "address" && $3 ~ /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/) {
        print interface, $0;
    }
}' ./../router.unix.txt