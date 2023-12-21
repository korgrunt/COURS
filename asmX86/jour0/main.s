	.file	"main.c"
	.intel_syntax noprefix
	.text
	.section	.rodata
.LC0:
	.string	"Hello, World!"
	.text
	.globl	my_function
	.type	my_function, @function
my_function:
	push	ebp
	mov	ebp, esp
	push	ebx
	sub	esp, 4
	call	__x86.get_pc_thunk.ax
	add	eax, OFFSET FLAT:_GLOBAL_OFFSET_TABLE_
	sub	esp, 12
	lea	edx, .LC0@GOTOFF[eax]
	push	edx
	mov	ebx, eax
	call	printf@PLT
	add	esp, 16
	mov	eax, 1
	mov	ebx, DWORD PTR -4[ebp]
	leave
	ret
	.size	my_function, .-my_function
	.section	.rodata
.LC1:
	.string	"\n start "
.LC2:
	.string	"\n hello world! \n"
.LC3:
	.string	"\n %d end \n "
	.text
	.globl	main
	.type	main, @function
main:
	lea	ecx, 4[esp]
	and	esp, -16
	push	DWORD PTR -4[ecx]
	push	ebp
	mov	ebp, esp
	push	ebx
	push	ecx
	sub	esp, 16
	call	__x86.get_pc_thunk.bx
	add	ebx, OFFSET FLAT:_GLOBAL_OFFSET_TABLE_
	sub	esp, 12
	lea	eax, .LC1@GOTOFF[ebx]
	push	eax
	call	puts@PLT
	add	esp, 16
	sub	esp, 12
	lea	eax, .LC2@GOTOFF[ebx]
	push	eax
	call	my_function
	add	esp, 16
	mov	DWORD PTR -16[ebp], eax
	mov	eax, DWORD PTR -16[ebp]
	add	eax, 3
	mov	DWORD PTR -12[ebp], eax
	sub	esp, 8
	push	DWORD PTR -12[ebp]
	lea	eax, .LC3@GOTOFF[ebx]
	push	eax
	call	printf@PLT
	add	esp, 16
	mov	eax, 0
	lea	esp, -8[ebp]
	pop	ecx
	pop	ebx
	pop	ebp
	lea	esp, -4[ecx]
	ret
	.size	main, .-main
	.section	.text.__x86.get_pc_thunk.ax,"axG",@progbits,__x86.get_pc_thunk.ax,comdat
	.globl	__x86.get_pc_thunk.ax
	.hidden	__x86.get_pc_thunk.ax
	.type	__x86.get_pc_thunk.ax, @function
__x86.get_pc_thunk.ax:
	mov	eax, DWORD PTR [esp]
	ret
	.section	.text.__x86.get_pc_thunk.bx,"axG",@progbits,__x86.get_pc_thunk.bx,comdat
	.globl	__x86.get_pc_thunk.bx
	.hidden	__x86.get_pc_thunk.bx
	.type	__x86.get_pc_thunk.bx, @function
__x86.get_pc_thunk.bx:
	mov	ebx, DWORD PTR [esp]
	ret
	.ident	"GCC: (Ubuntu 13.2.0-4ubuntu3) 13.2.0"
	.section	.note.GNU-stack,"",@progbits
