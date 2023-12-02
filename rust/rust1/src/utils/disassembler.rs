use crate::utils::instructions::Instruction;
use std::fs;

pub fn disassemble(file_path: &str) -> Vec<Instruction> {
    // /home/naouaichia/Downloads/fuzzinglabs.bin
    let contents = fs::read(file_path)
        .expect("Could not read file");

    bincode::deserialize(&contents[..]).expect("Cannot deserialize data")
}



pub fn pretty_print(instructions: &Vec<Instruction>){
    for instruction in instructions {
        println!("{:?}", instruction);
    }
}

/*
pub fn pretty(instructions: &Vec<Instruction>){
    let mut owned_string: String = "".to_owned();
    let borrowed_string: &str = "";
    
    owned_string.push_str(borrowed_string);

    for instruction in instructions {
        owned_string.push_str(instruction.);
        owned_string.push_str("\n");
    }
    return owned_string;
}
*/

#[cfg(test)]
mod tests {

    use crate::utils::disassembler::{disassemble, pretty_print};
    use crate::utils::instructions::Instruction;

    
    #[test]
    fn it_work_too() {
        let instruction_wanted: Vec<Instruction> = vec! [
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



