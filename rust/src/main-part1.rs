fn main() {
    let x = 5; // immuttable
    let mut y = 7; // muttable
    println!("Value y is {}", y + y);
    y = 8;
    println!("Hello, world!");
    println!("Value is {}", x);
    println!("Value y is {}", y + y);
    let val3: u32 = foofun(89, 99);
    let val4: f32 = foofun_float(89.4, 99.4);

    println!("Value rerturned is {}", val3);
    println!("Value rerturned is {}", val4);

    let a = [10, 20, 30, 40, 50];
    for element in a.iter() {
        println!("value of arr is {}", element);
    }
    let mut counter = 0;
    let result  = loop {
        counter += 1;

        if counter > 10 {
            break counter + 8
        }

    };
    println!("Value result is {}", result);


    let fibo: u32 = fib(14);
    println!("Value result is {}", fibo);

    let mut user1 = User {
        username: String::from("String"),
        email: String::from("String"),
        sign_in_count: 1,
        active: true,
    };

}

struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

fn fib2(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        n => fib(n -1) + fib(n - 2),

    }
}

enum Coin {
    Penny,
    EURO,
    DOLLARS,
    BITCOIN,
}

fn checkCoin(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 0,
        Coin::BITCOIN => 1,
        _ => 4,
    }
}


fn fib(n: u32) -> u32 {
    if n == 0{
        0
    } else if n == 1{
        1
    } else {
        fib(n - 1) + fib(n - 2)
    }
}


fn foofun(val1: u32, val2: u32) -> u32{
    println!("Value val1 is {}", val1 + val2);
    return val1 + val2;
}

fn add(val1: f32, val2: f32) -> f32{
    val1 + val2
}
fn foofun_float(val1: f32, val2: f32) -> f32{
    if(val1 > val2) && (val1 > val2) {
        println!("Value val1 is {} and val2 is {} and result is {}", val1, val2, add(val1, val2));

    }
    println!("Value val1 is {} and val2 is {} and result is {}", val1, val2, add(val1, val2));
    return val1 + val2;
}