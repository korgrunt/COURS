use std::net::Shutdown::Read;

fn main() {

    let args: Vec<String> = std::env::args().collect();

    if args.len() < 4 {
        println!("Bad argument goodby");
        return;
    }

    println!("Ok go");


    let operation = &args[1];
    let val1: u32 = args[2].parse().expect("Bad parsing for u32");
    let val2: u32 = args[3].parse().expect("Bad parsing for u32");
    println!("calc calc {:?}", calc(operation.to_lowercase(), val1, val2).unwrap());

}

fn add(a: u32, b: u32) -> Result<u32, String> {
   Ok(a + b)
}
fn sub(a: u32, b: u32) -> Result<u32, String> {
   Ok(a - b)
}
fn mul(a: u32, b: u32) -> Result<u32, String> {
    Ok(a * b)
}
fn div(a: u32, b: u32) -> Result<u32, String> {
    if b == 0{
        return Err("Cannot divide by 0".to_string());
    }
    Ok(a / b)
}
fn calc(n: String, a: u32, b: u32) -> Result<u32, String> {
    match n.as_str() {
        "+" => add(a, b),
        "-" => sub(a, b),
        "/" => div(a, b),
        "*" => mul(a, b),
        _ => Ok(a),
    }
}