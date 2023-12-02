use libc::c_int;
use std::ffi::CString;
use std::os::raw::c_char;


extern "C" {
    fn atoi(s: *const c_char) -> c_int;
}


fn main() {
    let s = CString::new("123").unwrap();
    let n = unsafe { atoi(s.as_ptr())};

    println!("{}", n);
    
}
