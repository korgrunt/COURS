awk 'BEGIN{

    password_encryption_enabled = 0  ;
}
{
    if($0 ~ /^service password-encryption$/) {
        password_encryption_enabled = 1;
    }        
}
END {
    print("FILENAME: " FILENAME);  
    print("TEST_NAME: TEST_1");  
    if(password_encryption_enabled == 1) {
        print("service password-encryption is configured");
    } else {
        print("service password-encryption is NOT configured");
    }
} ' ./conf-files/router.unix