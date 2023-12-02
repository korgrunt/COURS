use crate::utils::instructions::Instruction;
use std::fs;

pub fn compile(file_path: &str) -> Vec<Instruction> {
    // /home/naouaichia/Downloads/fuzzinglabs.bin
    let contents = fs::read(file_path)
        .expect("Could not read file");

    bincode::deserialize(&contents[..]).expect("Cannot deserialize data")
}


#[cfg(test)]
mod tests {

    use crate::utils::disassembler::{disassemble, pretty_print};
    use crate::utils::instructions::Instruction;

    
    #[test]
    fn simple_test_compilation() {
        let instruction: Vec<Instruction> = compile("exemples/fuzzinlabs");
        assert_eq!(instructions, vec![
            Instruction::push(70),
            Instruction::OutC,
            Instruction::Push(117),
            Instruction::OutC,
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
            Instruction::push(70),
        ]); 
        
        vec! [
            Instruction::Push(70),
            Instruction::OutC,
            Instruction::Push(117),
            Instruction::OutC,
            Instruction::Push(122),
            Instruction::OutC,
            Instruction::Push(122),
            Instruction::OutC,
            Instruction::Push(105),
            Instruction::OutC,
            Instruction::Push(110),
            Instruction::OutC,
            Instruction::Push(103),
            Instruction::OutC,
            Instruction::Push(108),
            Instruction::OutC,
            Instruction::Push(97),
            Instruction::OutC,
            Instruction::Push(98),
            Instruction::OutC,
            Instruction::Push(115),
            Instruction::OutC,
        ];
        
        let result = disassemble("/home/naouaichia/Downloads/fuzzinglabs.bin");
        assert_eq!(instruction_wanted, result);
    }
 
    

}



