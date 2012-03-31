%{
	#define YYSTYPE int
%}

%skeleton "lalr1.cc"
%defines
%define parser_class_name "Parser"

%code requires{
	#include <string>
	using namespace std;
	class Driver;
}

%locations
%parse-param { Driver &driver }
%lex-param   { Driver &driver }

%token END 0 "End of file"
%token DIGIT "digit"

%code {
	#include "Driver.h"
}

%%
line: "digit"	{ cout << "Entered digit: " << $1; }
 ;

%%

void yy::Parser::error(const yy::Parser::location_type &l, const string &message)
{
	driver.error(message);
}
