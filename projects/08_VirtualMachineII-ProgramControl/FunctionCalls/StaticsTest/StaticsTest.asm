// bootstrap codes
@261
D=A
@SP
M=D

// call Sys.init 0
@Sys.init
0;JMP

// function Class1.set 0
(Class1.set)
@0
D=A
@R13
M=D

(Class1.set$PUSH_LCL_VARS)
@R13
D=M
@Class1.set$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Class1.set$PUSH_LCL_VARS
0;JMP

(Class1.set$END_PUSH_LCL_VARS)

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

// pop static 0
@SP
M=M-1
A=M
D=M

@Class1.0
M=D

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

// pop static 1
@SP
M=M-1
A=M
D=M

@Class1.1
M=D

// push constant 0
@0
D=A

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

// function Class1.get 0
(Class1.get)
@0
D=A
@R13
M=D

(Class1.get$PUSH_LCL_VARS)
@R13
D=M
@Class1.get$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Class1.get$PUSH_LCL_VARS
0;JMP

(Class1.get$END_PUSH_LCL_VARS)

// push static 0
@Class1.0
D=M

@SP
A=M
M=D

@SP
M=M+1

// push static 1
@Class1.1
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

// push constant 6
@6
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

// call Class1.set 2
@Class1.set$ret.0
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
@2
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class1.set
0;JMP

(Class1.set$ret.0)

// pop temp 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@5
D=A
@0
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// push constant 23
@23
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 15
@15
D=A

@SP
A=M
M=D

@SP
M=M+1

// call Class2.set 2
@Class2.set$ret.1
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
@2
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class2.set
0;JMP

(Class2.set$ret.1)

// pop temp 0
@SP
M=M-1
A=M
D=M

@R13
M=D

@5
D=A
@0
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// call Class1.get 0
@Class1.get$ret.2
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
@0
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class1.get
0;JMP

(Class1.get$ret.2)

// call Class2.get 0
@Class2.get$ret.3
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
@0
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class2.get
0;JMP

(Class2.get$ret.3)

// label WHILE
(Sys.init$WHILE)

// goto WHILE
@Sys.init$WHILE
0;JMP

// function Class2.set 0
(Class2.set)
@0
D=A
@R13
M=D

(Class2.set$PUSH_LCL_VARS)
@R13
D=M
@Class2.set$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Class2.set$PUSH_LCL_VARS
0;JMP

(Class2.set$END_PUSH_LCL_VARS)

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

// pop static 0
@SP
M=M-1
A=M
D=M

@Class2.0
M=D

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

// pop static 1
@SP
M=M-1
A=M
D=M

@Class2.1
M=D

// push constant 0
@0
D=A

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

// function Class2.get 0
(Class2.get)
@0
D=A
@R13
M=D

(Class2.get$PUSH_LCL_VARS)
@R13
D=M
@Class2.get$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Class2.get$PUSH_LCL_VARS
0;JMP

(Class2.get$END_PUSH_LCL_VARS)

// push static 0
@Class2.0
D=M

@SP
A=M
M=D

@SP
M=M+1

// push static 1
@Class2.1
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

