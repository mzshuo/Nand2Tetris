// push constant 17
@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 17
@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// eq
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
@EQ_1
D;JEQ

D=0
@STORE_1
0;JMP

(EQ_1)
D=-1

(STORE_1)

@SP
A=M
M=D

@SP
M=M+1

// push constant 17
@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 16
@16
D=A

@SP
A=M
M=D

@SP
M=M+1

// eq
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
@EQ_2
D;JEQ

D=0
@STORE_2
0;JMP

(EQ_2)
D=-1

(STORE_2)

@SP
A=M
M=D

@SP
M=M+1

// push constant 16
@16
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 17
@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// eq
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
@EQ_3
D;JEQ

D=0
@STORE_3
0;JMP

(EQ_3)
D=-1

(STORE_3)

@SP
A=M
M=D

@SP
M=M+1

// push constant 892
@892
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 891
@891
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
@LT_4
D;JLT

D=0
@STORE_4
0;JMP

(LT_4)
D=-1

(STORE_4)

@SP
A=M
M=D

@SP
M=M+1

// push constant 891
@891
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 892
@892
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
@LT_5
D;JLT

D=0
@STORE_5
0;JMP

(LT_5)
D=-1

(STORE_5)

@SP
A=M
M=D

@SP
M=M+1

// push constant 891
@891
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 891
@891
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
@LT_6
D;JLT

D=0
@STORE_6
0;JMP

(LT_6)
D=-1

(STORE_6)

@SP
A=M
M=D

@SP
M=M+1

// push constant 32767
@32767
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 32766
@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// gt
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
@GT_7
D;JGT

D=0
@STORE_7
0;JMP

(GT_7)
D=-1

(STORE_7)

@SP
A=M
M=D

@SP
M=M+1

// push constant 32766
@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 32767
@32767
D=A

@SP
A=M
M=D

@SP
M=M+1

// gt
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
@GT_8
D;JGT

D=0
@STORE_8
0;JMP

(GT_8)
D=-1

(STORE_8)

@SP
A=M
M=D

@SP
M=M+1

// push constant 32766
@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 32766
@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// gt
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
@GT_9
D;JGT

D=0
@STORE_9
0;JMP

(GT_9)
D=-1

(STORE_9)

@SP
A=M
M=D

@SP
M=M+1

// push constant 57
@57
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 31
@31
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 53
@53
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

// push constant 112
@112
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

// neg
@SP
M=M-1
A=M
D=M
D=-D

@SP
A=M
M=D

@SP
M=M+1

// and
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
D=D&M
@SP
A=M
M=D

@SP
M=M+1

// push constant 82
@82
D=A

@SP
A=M
M=D

@SP
M=M+1

// or
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
D=D|M
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


(STOP)
@STOP
0;JMP
