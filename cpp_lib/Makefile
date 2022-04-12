# Makefile for Writing Make Files Example

# *****************************************************
# Variables to control Makefile operation

CC = g++
CFLAGS = -Wall -g
OUT = bin/my_lib.dll

all_sources = $(wildcard *.cpp)
all_objects = $(addprefix bin/,$(all_sources:.cpp=.o))

# ****************************************************
# Build lib
all: lib

lib:
	mkdir -p bin
	$(CC) $(CFLAGS) -shared -c cpp_lib.cpp -o bin/lib.so

clean:
	rm -rf ./bin
	rm -f *.o
	rm -f main

# ****************************************************
# Build lib
#all: bin/strings.dll

#bin/strings.dll: $(all_objects)
#	$(CC) $(CFLAGS) -c cpp_lib.cpp -o
#	$(CC) $(CFLAGS) -c main.cpp
#	$(CC) $(CFLAGS) -c cpp_lib.cpp
#	$(CC) $(CFLAGS) -o main main.o cpp_lib.o


#	$(CC) -shared -o $(OUT) $(OBJ)
#
#bin/%.o: %.cpp
#    <how to build objects inside bin dir from cpp of current dir>


# ****************************************************
# Targets needed to bring the executable up to date

main: main.o cpp_lib.o
	$(CC) $(CFLAGS) -o main main.o cpp_lib.o

main.o: main.cpp cpp_lib.h
	$(CC) $(CFLAGS) -c main.cpp

cpp_lib.o: cpp_lib.h
