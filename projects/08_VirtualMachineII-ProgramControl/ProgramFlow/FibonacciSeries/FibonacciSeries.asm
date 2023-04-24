// push argument 1
@ARG
D=M
@1
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// pop pointer 1
@SP
M=M-1
A=M
D=M

@THAT
M=D

// push constant 0
@0
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop that 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@THAT
D=M
@0
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// push constant 1
@1
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop that 1
@SP
M=M-1
A=M
D=M

@R13
M=D

@THAT
D=M
@1
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// push argument 0
@ARG
D=M
@0
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// push constant 2
@2
D=A

@SP
A=M
M=D

@SP
M=M+1

// sub
@SP
M=M-1
A=M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
D=D-M
@SP
A=M
M=D

@SP
M=M+1

// pop argument 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@ARG
D=M
@0
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// label MAIN_LOOP_START
(FibonacciSeries.null$MAIN_LOOP_START)

// push argument 0
@ARG
D=M
@0
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// if-goto COMPUTE_ELEMENT
@SP
M=M-1
A=M
D=M

@FibonacciSeries.null$COMPUTE_ELEMENT
D;JMP

// goto END_PROGRAM
@FibonacciSeries.null$END_PROGRAM
0;JMP

// label COMPUTE_ELEMENT
(FibonacciSeries.null$COMPUTE_ELEMENT)

// push that 0
@THAT
D=M
@0
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// push that 1
@THAT
D=M
@1
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
D=D+M
@SP
A=M
M=D

@SP
M=M+1

// pop that 2
@SP
M=M-1
A=M
D=M

@R13
M=D

@THAT
D=M
@2
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// push pointer 1
@THAT
D=M

@SP
A=M
M=D

@SP
M=M+1

// push constant 1
@1
D=A

@SP
A=M
M=D

@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
D=D+M
@SP
A=M
M=D

@SP
M=M+1

// pop pointer 1
@SP
M=M-1
A=M
D=M

@THAT
M=D

// push argument 0
@ARG
D=M
@0
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// push constant 1
@1
D=A

@SP
A=M
M=D

@SP
M=M+1

// sub
@SP
M=M-1
A=M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
D=D-M
@SP
A=M
M=D

@SP
M=M+1

// pop argument 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@ARG
D=M
@0
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// goto MAIN_LOOP_START
@FibonacciSeries.null$MAIN_LOOP_START
0;JMP

// label END_PROGRAM
(FibonacciSeries.null$END_PROGRAM)


(STOP)
@STOP
0;JMP
