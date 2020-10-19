import sys
import glob

# SRC = [c :: gcc], [c++ :: g++], [both :: error], [nothing :: error]
SRC = "c"
CC = "gcc"

sfile = []
hfile = []
target = ""

def get_source_type(src_path):
    """ To get the source extension [c or cpp file]
    
    src_path : source file path
    """
    SRC = ""
    CC = ""
    clist = glob.glob(src_path + "/*.c")
    cpplist = glob.glob(src_path + "/*.cpp")

    if len(clist) > 0 and len(cpplist) > 0:
        SRC = "both"
    elif len(clist) == 0 and len(cpplist) == 0:
        SRC = "nothing"
    else:
        if len(clist) > 0:
            SRC, CC = "c", "gcc"
        elif len(cpplist) > 0:
            SRC, CC = "cpp", "g++"

    return SRC, CC

def get_source_files_info(src_path):
    """ Returns list of cfile or cppfile

    src_path : source file path
    """
    global SRC
    tmps = []
    
    files = glob.glob(src_path + "/*." + SRC)
    for f in files:
        if src_path == ".":
            f = f.replace("./", "")
        tmps.append(f)
    return tmps

def get_header_files_info(inc_path):
    """ Returns list of header files
    
    inc_path: header file path
    """
    tmph = []
    
    files = glob.glob(inc_path + "/*.h")
    for f in files:
        if inc_path == ".":
            f = f.replace("./", "")
        tmph.append(f)
    return tmph
        
def get_target_file_info(src_path, inc_path):
    """ Returns only the target file
    
    src_path : source file path
    inc_path : header file path
    """
    global SRC, sfile, hfile
    tmps, tmph = [], []
    
    for s in sfile:
        s = s.replace(src_path + '/', '')
        s = s.replace('.' + SRC, '')
        tmps.append(s)
    for h in hfile:
        h = h.replace(inc_path + '/', '')
        h = h.replace('.h', '')
        tmph.append(h)

    for s in tmps:
        if s not in tmph:
            return s

def get_required_files_info(inc_path, src_path):
    """ collects source, header, target files information.

    inc_path : header file path
    src_path : source file path
    """
    global SRC, CC, sfile, hfile, target

    SRC, CC = get_source_type(src_path)
    if SRC == "both":
        print("ERROR: Too many types of source file's !")
        sys.exit()
    elif SRC == "nothing":
        print("ERROR: No source file found !")
        print("       gen-make require's atleast one source file")
        sys.exit()

    sfile = get_source_files_info(src_path)
    hfile = get_header_files_info(inc_path)
    target = get_target_file_info(src_path, inc_path)

def write_compilation_variable(file_ptr, path, ldlibs):
    """ Write compilation variable's
    
    file_ptr : file pointer of Makefile
    path     : header file path 
    ldlibs   : linker library 
    """
    global SRC, CC
    EOL = "\n"

    file_ptr.write("CC       := " + CC + EOL)

    if SRC == "c" and path != ".":
        file_ptr.write("CFLAGS   := -I " + path + EOL)
    elif SRC == "cpp" and path != ".":
        file_ptr.write("CXXFLAGS := -I " + path + EOL)
    
    if ldlibs != None:
        file_ptr.write("LDLIBS   :=")
        for lib in ldlibs:
            file_ptr.write(lib.replace(lib, " -" + lib))
        file_ptr.write(EOL)

def write_object_variable(file_ptr, path):
    """ Write's source and object variable
 
    file_ptr: file pointer of Makefile
    path    : source file path 
    """
    global sfile
    EOL = "\n"
    tmps = []
    
    for s in sfile:
        s = s.replace(path + '/', '')
        tmps.append(s)
        
    src = " ".join(tmps)
    file_ptr.write("SRCS     := $(addprefix " + path + "/, " + src + ")" + EOL)
    file_ptr.write("OBJS     := $(SRCS:."+ SRC + "=" +".o)" + EOL)
    file_ptr.write(EOL)

def write_rules(file_ptr, out, ldlibs):
    """ Write target and dependencies

    file_ptr: file pointer of Makefile
    out     : target filename if mentoined additionally
    ldlibs  : linker library
    """
    global target
    EOL = "\n"
    tab = "\t"

    if out != "":
        target = out
    # target and dependencies
    file_ptr.write("all: $(OBJS)" + EOL)
    # receipe 
    file_ptr.write(tab + "$(CC) $(OBJS)")
    if ldlibs != None:
        file_ptr.write(" $(LDLIBS)")
    file_ptr.write(" -o " + target + EOL)
    file_ptr.write(EOL)
    
def write_phony_rules(file_ptr):
    """ Write phony rules.
    
    file_ptr: file pointer of Makefile
    """
    global target
    EOL = '\n'
    tab = '\t'

    file_ptr.write(".PHONY: clean" + EOL)
    file_ptr.write("clean :" + EOL)
    file_ptr.write(tab + "rm $(OBJS)" + EOL)
    file_ptr.write(tab + "rm " + target + EOL)

def write_makefile_rules(file_ptr, header, source, target, ldlib):
    """ Making rules for makefile
    
    file_ptr: file pointer of makefile
    header  : header path
    source  : source file path
    target  : target file name
    ldlib   : linker library
    """
    if target == None:
        target = ""
    write_compilation_variable(file_ptr, header, ldlib)
    write_object_variable(file_ptr, source)
    write_rules(file_ptr, target, ldlib)
    write_phony_rules(file_ptr)
