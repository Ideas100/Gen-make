import os
import argparse
import gen_make.do_makefile as do

def create_makefile():
    """ create a Makefile
    """
    global path
    EOL = "\n"
    
    path = os.getcwd()
    file_ptr = open(path + "/Makefile", "w+")

    file_ptr.write("#   Gen-make-1.0.0" + EOL)
    file_ptr.write("#   https://github.com/Ideas100/Gen-make" + EOL)
    file_ptr.write("#" + EOL)
    file_ptr.write(EOL)
    
    return file_ptr

def define_arguments():
    """ Argument parser is defined for gen-make
    """
    global arg

    parser = argparse.ArgumentParser(description="Generate's basic Makefile")
    parser.add_argument("-H", action="store", dest="header", nargs="?",
                        help="header file directory path")
    parser.add_argument("-s", action="store", dest="source", nargs="?",
                        help="source file directory path")
    parser.add_argument("-o", action="store", dest="target", nargs="?",
                        help="output file path and name")
    parser.add_argument("-l", action="store", dest="ldlibs", nargs="+", 
                        help="additional linker library")
    parser.add_argument("-v", action="store_true", default=False, 
                        help="modify output verbosity")
    arg = parser.parse_args()

def reformat_path():
    """ Reformatting the input from the argument's.
    """
    global arg, header, source
    
    header = arg.header
    source = arg.source
    if header == None:
        header = "."
    elif header[-1] == "/":
        header = header[:-1]
    if source == None:
        source = "."
    elif source[-1] == "/":
        source = source[:-1]

def verbosity():
    """ Providing verbosity of Makefile Creation
    """
    print("Generate-Makefile: [ gen-make ]") 
    print(" CC       = " + do.CC)
    print(" header   = " + str(do.hfile))
    print(" source   = " + str(do.sfile))
    if arg.ldlibs != None:
        print(" link lib = " + str(arg.ldlibs))
    print(" target   = " + do.target)
    
def main():
    """ Entire Makefile creation is done here!!!
    """
    global arg, header, source

    define_arguments()
    reformat_path()
    do.get_required_files_info(header, source)

    fileptr = create_makefile()
    do.write_makefile_rules(fileptr, header, source, arg.target, arg.ldlibs)
    fileptr.close()
    if arg.v:
        verbosity()
    print("Makefile created path: " + path + "/Makefile")

if __name__ == "__main__":
    main()
    
