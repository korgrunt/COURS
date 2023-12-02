use std::io::{self, Write};

use crate::{utils::instructions::Instruction, stack::Stack};

#[derive(Debug)]
pub struct Vm {
    pc: usize,
    instructions: Vec<Instruction>,
    stack: Stack
}

impl Vm {
    
    pub fn new(instructions: Vec<Instruction>) -> Self {
        Vm {
            pc: 0,
            instructions,
            stack: Stack::new(),
        }
    }

    pub fn run(&mut self) {
        while self.pc < self.instructions.len() {
            println!("{:?}", self.instructions[self.pc]);
            match self.instructions[self.pc] {
                Instruction::Push(value) => self.stack.push(value),
                Instruction::Pop => {
                    let _ret = self.stack.pop();
                }
                Instruction::Dup => {
                    let n = self.stack.peek().expect("Peeked on a n empty");
                },
                Instruction::Swap => {
                    let a = self.stack.pop().expect("Pop on a n empty");
                    let b = self.stack.pop().expect("Pop on a n empty");
                    self.stack.push(a);
                    self.stack.push(b);
                },
                Instruction::Out => {
                    let n = self.stack.peek().expect("peeked an empty element");
                    println!("{}", n);
                },
                Instruction::OutC => {
                    let n = self.stack.peek().unwrap_or(&u32::MIN);
                    if let Some(c) = std::char::from_u32(*n) {
                        println!("{}", c);
                    } else {
                        println!("{}", n);
                    }
                },
                Instruction::Add => {
                    let a = self.stack.pop().expect("peeked an empty element");
                    let b = self.stack.pop().expect("peeked an empty element");
                    self.stack.push(a + b);

                },
                Instruction::Div => {
                    let a = self.stack.pop().expect("peeked an empty element");
                    let b = self.stack.pop().expect("peeked an empty element");
                    self.stack.push(a / b);

                },
                Instruction::Mul => {
                    let a = self.stack.pop().expect("peeked an empty element");
                    let b = self.stack.pop().expect("peeked an empty element");
                    self.stack.push(a * b);

                },
                Instruction::Sub => {
                    let a = self.stack.pop().expect("peeked an empty element");
                    let b = self.stack.pop().expect("peeked an empty element");
                    self.stack.push(a - b);

                },
                Instruction::In => {

                    let mut input = String::new();
                    io::stdout().flush().unwrap();
                    io::stdin().read_line(&mut input).expect("Failed to read line");
                    let number: u32 = input.trim().parse().expect("Please enter a valid integer");
                    self.stack.push(number);

                },
                Instruction::Halt => {
                    std::process::exit(0);
                },
                Instruction::Jmp(value) => {
                    self.pc = usize::try_from(value).unwrap();
                },
                Instruction::Jnz(value) => {
                    let n = self.stack.peek().expect("peeked an empty element");
                    if *n != u32::from(u32::MIN) {
                        self.pc = usize::try_from(value).unwrap();
                    }
                },
                Instruction::Jz(value) => {
                    let n = self.stack.peek().expect("peeked an empty element");
                    if *n == u32::from(u32::MIN) {
                        self.pc = usize::try_from(value).unwrap();
                    }
                    
                },
                Instruction::Unknown => {
                    std::process::exit(0);
                },
            }
            self.pc += 1;
        }
    }
}



#[cfg(test)]
mod tests {
    
 

    use crate::utils::{instructions::Instruction, disassembler::disassemble};

    use super::Vm;
    
    #[test]
    fn vm_works() {
        
        let instructionReaded = disassemble("/home/naouaichia/Workspace/COURS/rust/src/steps/step7_2.bin");
         let mut vec: Vec<Instruction> = Vec::new();

        let mut vm = Vm::new(instructionReaded);
        vm.run();
        assert!(true);
    }

    #[test]
    fn vm_works_in() {
        
        let instructionReaded = disassemble("/home/naouaichia/Workspace/COURS/rust/src/steps/step7_3.bin");
         let mut vec: Vec<Instruction> = Vec::new();

        let mut vm = Vm::new(instructionReaded);
        vm.run();
        assert!(true);
    }

    #[test]
    fn vm_works_in_jump() {
        
        let instructionReaded = disassemble("/home/naouaichia/Workspace/COURS/rust/src/steps/step7_4.bin");
         let mut vec: Vec<Instruction> = Vec::new();

        let mut vm = Vm::new(instructionReaded);
        vm.run();
        assert!(true);
    }
}