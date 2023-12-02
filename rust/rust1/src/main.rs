use crate::utils::instructions;
use crate::utils::instructions::Instruction;
use crate::utils::disassembler::disassemble;
use crate::utils::disassembler::pretty_print;
use crate::utils::mode::Mode;
use clap::Parser;
use vm::Vm;
use std::fs::File;
//use utils::disassembler::pretty;
use std::fs::read_to_string;
use std::io::Write;

mod stack;
mod vm;
mod utils;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {

    #[arg(short, long)]
    path: String,
    
    #[arg(short, long)]
    mode: Mode,

    #[arg(short, long, default_value_t= 1)]
    count: u8,
}


fn main(){

    let args = Args::parse();


    
    match args.mode {
        Mode::Runner => {
            let instructions: Vec<Instruction> = disassemble(&args.path);
            let mut vm = Vm::new(instructions);
            vm.run();
        }
        Mode::Disassembler => {
            let disassembly: Vec<Instruction> = disassemble(&args.path);
            pretty_print(&disassembly);
            //let disassembled = pretty(&disassembly);
            //println!("{:?}", disassembled);
            
            //write_dissassembly()
        }
        Mode::Assembler => {

        
            let mut instructions: Vec<Instruction> = vec![];

            for line in read_to_string("/home/naouaichia/Workspace/COURS/rust/test.svm").unwrap().lines() {
                let line = line.to_string();
                if line.is_empty() {
                    continue;
                }
                let mut tokens = line.split(" ");

                if let Some(instructions_token) = tokens.next() {

                    let instruction = match instructions_token {
                        "push" => {
                            if let Some(number_token) = tokens.next(){
                                if let Ok(n) = number_token.to_string().parse() {
                                    Instruction::Push(n)
                                } else {
                                    panic!("Could get number !")
                                }
                            } else {
                                panic!("Missing agument to push instruction !")
                            }
                        }
                        "pop" => Instruction::Pop,
                        "dup" => Instruction::Dup,
                        "swap" => Instruction::Swap,
                        "out" => Instruction::Out,
                        "add" => Instruction::Add,
                        "sub" => Instruction::Sub,
                        "mul" => Instruction::Mul,
                        "div" => Instruction::Div,
                        "in" => Instruction::In,
                        "halt" => Instruction::Halt,
                        "unknown" => Instruction::Unknown,
                        "jmp" => {
                            if let Some(number_token) = tokens.next(){
                                if let Ok(n) = number_token.to_string().parse() {
                                    Instruction::Jmp(n)
                                } else {
                                    panic!("Could get number !")
                                }
                            } else {
                                panic!("Missing agument to push instruction !")
                            }
                        },
                        "jz" => {
                            if let Some(number_token) = tokens.next(){
                                if let Ok(n) = number_token.to_string().parse() {
                                    Instruction::Jz(n)
                                } else {
                                    panic!("Could get number !")
                                }
                            } else {
                                panic!("Missing agument to push instruction !")
                            }
                        },
                        "jnz" => {
                            if let Some(number_token) = tokens.next(){
                                if let Ok(n) = number_token.to_string().parse() {
                                    Instruction::Jnz(n)
                                } else {
                                    panic!("Could get number !")
                                }
                            } else {
                                panic!("Missing agument to push instruction !")
                            }
                        },
                        &_ => {
                            panic!("Not handle")
                        }
                    };
                }




            }

        
        }

    }

    

}





/*
fn write_to_bin(instruction_or_value: &str){

    let mut file = File::create("foo.bin").expect("Cannot create file");
    file.write_all(&instruction_or_value).expect("cannot write to file");

}

*/