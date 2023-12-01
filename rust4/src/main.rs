use regex::Regex;
use std::fs;
use std::time::{Duration, Instant};

fn without_threads(  ){

    
    
    let contents = fs::read_to_string("/home/naouaichia/Workspace/COURS/rust4/data.json").expect("Quelque chose s'est mal passé lors de la lecture du fichier");
    
    println!("________________");
    let patterns = vec![
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}", 
        r"\+?\d[\d -]{8,12}\d",                            
    ];

    for pattern in patterns {
        let re = Regex::new(&pattern).expect("issue  regex");
        let count = re.find_iter(&contents).count();
        println!("Pattern: {}, Matches found: {}", pattern, count);
    }

    println!("________________");
}



fn main() {

    let start = Instant::now();
    
    without_threads();
    let duration = start.elapsed();

    println!("Execution duration: {:?}", duration);

}
