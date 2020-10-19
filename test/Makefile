#   Gen-make-1.0.0
#   https://github.com/Ideas100/Gen-make
#

CC       := g++
SRCS     := $(addprefix ./, print.cpp hello.cpp)
OBJS     := $(SRCS:.cpp=.o)

all: $(OBJS)
	$(CC) $(OBJS) -o hello

.PHONY: clean
clean :
	rm $(OBJS)
	rm hello
