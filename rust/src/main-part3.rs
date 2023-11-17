use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();

    let n1  = rng.gen::<u8>();
    let n2: u16 = rng.gen();

   println!("Random u8: {}", n1);
    println!("Random u8: {}", n2);
}
