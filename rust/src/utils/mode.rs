use clap::{ValueEnum};



#[derive(Clone, Copy, PartialEq, Debug, PartialOrd, Eq, Ord, ValueEnum)]
pub enum Mode {
    Disassembler,
    Assembler,
    Runner,
}
