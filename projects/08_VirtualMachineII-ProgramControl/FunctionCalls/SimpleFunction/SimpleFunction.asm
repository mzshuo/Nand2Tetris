// function SimpleFunction.test 2
(SimpleFunction.test)
@2
D=A
@R13
M=D

(SimpleFunction.test$PUSH_LCL_VARS)
@R13
D=M
@SimpleFunction.test$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@SimpleFunction.test$PUSH_LCL_VARS
0;JMP

(SimpleFunction.test$END_PUSH_LCL_VARS)

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

// push local 1
@LCL
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

// not
@SP
M=M-1
A=M
D=M
D=!D

@SP
A=M
M=D

@SP
M=M+1

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

// return
@5
D=A
@LCL
A=M
A=A-D
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D

@ARG
D=M
@SP
M=D+1

@LCL
M=M-1
A=M
D=M
@THAT
M=D

@LCL
M=M-1
A=M
D=M
@THIS
M=D

@LCL
M=M-1
A=M
D=M
@ARG
M=D

@LCL
M=M-1
A=M
D=M
@LCL
M=D

@R13
A=M
0;JMP


(STOP)
@STOP
0;JMP
