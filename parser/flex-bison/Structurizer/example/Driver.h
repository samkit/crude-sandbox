#include <string>
#include "parser.tab.hh"

using namespace std;
using namespace yy;

#define YY_DECL yy::Parser::token_type yylex(yy::Parser::semantic_type *yylval, yy::Parser::location_type *yylloc, Driver &driver)
YY_DECL;

class Driver {
	public:
		string file_name;
		Driver() {}
		~Driver();
		int parse(const string &file_name);
		void error(const string &error_message);
};
