
fn main() {
    let mut a = 31;
    let mut b = &mut a;
    *b= 89;
    println!("{:?}", b);
    println!("{:?}", a);
    {
        let mut e = b;
        println!("{:?}", e);
    }
}

