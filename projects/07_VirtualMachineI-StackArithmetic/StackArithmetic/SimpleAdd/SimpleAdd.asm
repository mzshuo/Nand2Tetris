// push constant 7
@7
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 8
@8
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


(STOP)
@STOP
0;JMP
