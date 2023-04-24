// push constant 0
@0
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop local 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@LCL
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

// label LOOP_START
(BasicLoop.null$LOOP_START)

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

// push local 0
@LCL
D=M
@0
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

// pop local 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@LCL
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

// if-goto LOOP_START
@SP
M=M-1
A=M
D=M

@BasicLoop.null$LOOP_START
D;JMP

// push local 0
@LCL
D=M
@0
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1


(STOP)
@STOP
0;JMP
