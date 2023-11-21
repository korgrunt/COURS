use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, PartialEq, Debug)]
#[allow(dead_code)]
pub enum Instruction {
    Push(u32),
    Pop,
    Dup,// duplicate the top of the stack
    Swap,// swap the two values at the top of the stack
    
    Add,
    Sub,
    Mul,
    Div,

    In, // Read number from stdin
    Out, // print u32
    OutC,// print char if possible
    
    Jmp(u32),// Jump to instruction
    Jz(u32), // jump to instruction if top of stack is 0
    Jnz(u32),// jump to instruction if top of the stack is not 0
    
    Halt,// Stop the vm
    
    Unknown,
}
