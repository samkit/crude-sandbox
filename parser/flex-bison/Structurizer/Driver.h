#include <string>
#include "parser.hh"

#define YY_DECL yy::Parser::token_type \
	yylex(yy::Parser::semantic_type *yylval, \
	      yy::Parser::location_type *yylloc, \
	      Driver &driver)

YY_DECL;

class Driver {
 public:
	string file;

	Driver() {}
	Driver(const string &);

	~Driver();

	int parse();
	void error(const string &message);
};
