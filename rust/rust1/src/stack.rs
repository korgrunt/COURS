#[derive(Debug)]
pub struct Stack {
    stack: Vec<u32>
}

impl Stack {
    
    pub fn new() -> Stack {
        let stack = Stack {
            stack: Vec::new(),
        };
        return stack;
    }

    pub fn pop(&mut self) -> Option<u32> {
        return self.stack.pop();
    }
    pub fn size(&mut self) -> usize {
        return self.stack.len();
    }
    pub fn push(&mut self, val: u32) {
        self.stack.push(val);
        return ();
    }
    pub fn peek(&mut self) -> Option<&u32> {
        return self.stack.last();

    }
}



#[cfg(test)]
mod tests {
    
    use super::Stack;
    
    #[test]
    fn stack_works() {
        let mut stack = Stack::new();

        println!("the last element of stack is {:?}", stack.size());

        stack.push(33);
        stack.push(13);
        stack.push(23);

        println!("the last element of stack is {:?}", stack.peek().unwrap());

        stack.push(77);

        println!("the last element of stack is {:?}", stack.peek().unwrap());

        stack.pop();

        println!("the last element of stack is {:?}", stack.peek().unwrap());
        assert!(true);
    }
}