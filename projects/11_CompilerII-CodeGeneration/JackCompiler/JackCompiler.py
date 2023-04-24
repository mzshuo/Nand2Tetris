import sys
import os
import CompilationEngine


def compileFile(input_file):
    """
    Parse the input .jack file and output an .XML file accordingly.
    """
    parser = CompilationEngine.CompilationEngine(input_file)
    parser.compile_class()


if __name__ == '__main__':
    input = sys.argv[1]

    # Input is a single .jack source file.
    if (os.path.isfile(input)):
        compileFile(input)

    # Input is a directory containing one or more .jack source files.
    elif (os.path.isdir(input)):
        for file in os.listdir(input):
            if os.path.splitext(file)[1] == '.jack':
                file_path = os.path.join(input, file)
                compileFile(file_path)
