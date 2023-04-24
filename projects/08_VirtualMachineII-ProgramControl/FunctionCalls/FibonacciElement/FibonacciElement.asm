// bootstrap codes
@261
D=A
@SP
M=D

// call Sys.init 0
@Sys.init
0;JMP

// function Main.fibonacci 0
(Main.fibonacci)
@0
D=A
@R13
M=D

(Main.fibonacci$PUSH_LCL_VARS)
@R13
D=M
@Main.fibonacci$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Main.fibonacci$PUSH_LCL_VARS
0;JMP

(Main.fibonacci$END_PUSH_LCL_VARS)

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

// lt
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
@LT_1
D;JLT

D=0
@STORE_1
0;JMP

(LT_1)
D=-1

(STORE_1)

@SP
A=M
M=D

@SP
M=M+1

// if-goto IF_TRUE
@SP
M=M-1
A=M
D=M

@Main.fibonacci$IF_TRUE
D;JNE

// goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP

// label IF_TRUE
(Main.fibonacci$IF_TRUE)

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

// label IF_FALSE
(Main.fibonacci$IF_FALSE)

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

// call Main.fibonacci 1
@Main.fibonacci$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(Main.fibonacci$ret.1)

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

// call Main.fibonacci 1
@Main.fibonacci$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(Main.fibonacci$ret.2)

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

// function Sys.init 0
(Sys.init)
@0
D=A
@R13
M=D

(Sys.init$PUSH_LCL_VARS)
@R13
D=M
@Sys.init$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Sys.init$PUSH_LCL_VARS
0;JMP

(Sys.init$END_PUSH_LCL_VARS)

// push constant 4
@4
D=A

@SP
A=M
M=D

@SP
M=M+1

// call Main.fibonacci 1
@Main.fibonacci$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(Main.fibonacci$ret.3)

// label WHILE
(Sys.init$WHILE)

// goto WHILE
@Sys.init$WHILE
0;JMP

