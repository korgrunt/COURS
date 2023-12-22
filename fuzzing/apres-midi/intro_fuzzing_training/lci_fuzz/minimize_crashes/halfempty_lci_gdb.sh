#!/bin/sh

# You need to change the program counter for each target
expected_pc="0x52ed8c"

tempfile=`mktemp` && cat > ${tempfile}
result=1

trap 'rm -f ${tempfile}; exit ${result}' EXIT TERM ALRM

gdb -q									\
	-ex "r"								\
	-ex "q (\$pc == $expected_pc)" \
	--args ../lci/lci ${tempfile}

# Check if we were killed with SIGSEGV
if test $? -eq 1; then
    result=0 # We want this input
fi