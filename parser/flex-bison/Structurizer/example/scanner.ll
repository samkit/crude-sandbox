%{
	#include <string>
	#include "parser.tab.hh"
	#include "Driver.h"
	using namespace std;
	using namespace yy;
	#define yyterminate() return yy::Parser::token::END
%}

%option noyywrap

%%

[[:digit:]]+	{ *yylval = atoi(yytext); return yy::Parser::token::DIGIT; }

(?s:.)			{ cout << yytext; }

%%

int Driver::parse(const string &file_name)
{
	this->file_name = file_name;
	yyin = fopen(file_name.c_str(), "r");
	if(NULL == yyin) {
		cout << "Error opening input file\n";
		exit(1);
	}

	Parser parser(*this);		// takes a driver
	return parser.parse();
}

void Driver::error(const string &error_string) {
	cout << error_string << endl;
}

Driver::~Driver()
{
	cout << "Closing file\n";
	fclose(yyin);
}
