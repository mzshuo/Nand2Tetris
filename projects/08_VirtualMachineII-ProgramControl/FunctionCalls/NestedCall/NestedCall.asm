// bootstrap codes
// @256
// D=A
// @SP
// M=D

// call Sys.init 0
@Sys.init
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

// push constant 4000
@4000
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop pointer 0
@SP
M=M-1
A=M
D=M

@THIS
M=D

// push constant 5000
@5000
D=A

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

// call Sys.main 0
@Sys.main$ret.0
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

@Sys.main
0;JMP

(Sys.main$ret.0)

// pop temp 1
@SP
M=M-1
A=M
D=M

@R13
M=D

@5
D=A
@1
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// label LOOP
(Sys.init$LOOP)

// goto LOOP
@Sys.init$LOOP
0;JMP

// function Sys.main 5
(Sys.main)
@5
D=A
@R13
M=D

(Sys.main$PUSH_LCL_VARS)
@R13
D=M
@Sys.main$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Sys.main$PUSH_LCL_VARS
0;JMP

(Sys.main$END_PUSH_LCL_VARS)

// push constant 4001
@4001
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop pointer 0
@SP
M=M-1
A=M
D=M

@THIS
M=D

// push constant 5001
@5001
D=A

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

// push constant 200
@200
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop local 1
@SP
M=M-1
A=M
D=M

@R13
M=D

@LCL
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

// push constant 40
@40
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop local 2
@SP
M=M-1
A=M
D=M

@R13
M=D

@LCL
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

// push constant 6
@6
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop local 3
@SP
M=M-1
A=M
D=M

@R13
M=D

@LCL
D=M
@3
D=D+A
@R14
M=D

@R13
D=M
@R14
A=M
M=D

// push constant 123
@123
D=A

@SP
A=M
M=D

@SP
M=M+1

// call Sys.add12 1
@Sys.add12$ret.1
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

@Sys.add12
0;JMP

(Sys.add12$ret.1)

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

// push local 2
@LCL
D=M
@2
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// push local 3
@LCL
D=M
@3
A=D+A
D=M

@SP
A=M
M=D

@SP
M=M+1

// push local 4
@LCL
D=M
@4
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

// function Sys.add12 0
(Sys.add12)
@0
D=A
@R13
M=D

(Sys.add12$PUSH_LCL_VARS)
@R13
D=M
@Sys.add12$END_PUSH_LCL_VARS
D;JEQ

@SP
A=M
M=0
@SP
M=M+1

@R13
M=M-1

@Sys.add12$PUSH_LCL_VARS
0;JMP

(Sys.add12$END_PUSH_LCL_VARS)

// push constant 4002
@4002
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop pointer 0
@SP
M=M-1
A=M
D=M

@THIS
M=D

// push constant 5002
@5002
D=A

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

// push constant 12
@12
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

