build:
	make clean
	flex lexer.l
	bison --report=state -d parser.y
	g++ -g -c lexer.cpp
	g++ -g -c parser.cc
	g++ -g -c main.cc
	g++ -o Structurizer parser.o lexer.o main.o

clean:
	rm -f lex*.c* parse*.c* parse*.h* *.hh *.o* Structurizer
