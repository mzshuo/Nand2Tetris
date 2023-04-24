import sys
import os
import CompilationEngine


def analyzeFile(input_file):
    """
    Parse the input .jack file and output an .XML file accordingly.
    """
    parser = CompilationEngine.CompilationEngine(input_file)
    parser.compile_class()


if __name__ == '__main__':
    input = sys.argv[1]

    # Input is a single source file.
    if (os.path.isfile(input)):
        analyzeFile(input)

    # Input is a directory containing one or more .jack source files.
    elif (os.path.isdir(input)):
        for file in os.listdir(input):
            if os.path.splitext(file)[1] == '.jack':
                file_path = os.path.join(input, file)
                analyzeFile(file_path)
