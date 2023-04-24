// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


 // while(True):
 //     press = RAM[KBD]
 //     if (RAM[KBD] == 0) {
 //         set screen to all white
 // 	}
 //	else {
 //	    set screen to all black
 // 	}


    @8192
    D = A
    @boundary
    M = D     // boundary = 8192 = (256*512)/16

  (BEGIN)
    @pos
    M = 0    // pos = 0

    @KBD
    D = M
    @WHITE
    D; JEQ    // if RAM[KBD]==0: jump to WHITE
    @BLACK
    D; JNE    // if RAM[KBD]!=0: jump to BLACK

  (WHITE)
    @SCREEN
    D = A
    @pos
    A = D + M
    M = 0    // set RAM[SCREEN+pos] to white

    @pos
    M = M + 1    // pos = pos + 1

    @pos
    D = M
    @boundary
    D = D - M
    @BEGIN
    D; JEQ    // if pos==boundary: jump to BEGIN
    @WHITE
    0; JMP    // else: jump to WHITE

  (BLACK)
    @SCREEN
    D = A
    @pos
    A = D + M
    M = -1    // set RAM[SCREEN+pos] to black

    @pos
    M = M + 1    // pos = pos + 1

    @pos
    D = M
    @boundary
    D = D - M
    @BEGIN
    D; JEQ    // if pos==boundary: jump to BEGIN
    @BLACK
    0; JMP    // else: jump to BLACK
    
    

    