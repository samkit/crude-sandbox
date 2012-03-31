	/* Search FIXME to fix */
	/* Search CHECKME to test */
	/* Search UNCOMMENT to uncomment code */
	/* Search PERFORMANCE to get a performace fix */

	/*
	 * Important enhancements:
	 * 1. Handle struct inside struct, and recursively.
	 * 2. Handle union inside struct, and recursively.
	 * 3. Handle typedef(s), and recursively.
	 * 4. Better error handling -> In case of syntax
	 *    errors, user should know the exact point of
	 *    wrong syntax.
	 */
%code requires{
	#include <map>
	#include <string>
	#include "parser.hh"
	#include "Entity.h"
	class Driver;
	using namespace std;
}

%define parser_class_name "Parser"
%parse-param { Driver &driver }
%lex-param { Driver &driver }

%union {
	string *word;
	long number;
}

%output="parser.cc"
%defines
%skeleton "lalr1.cc"
%locations

%code {
	#include "Driver.h"
}

%token END 0 "end of file"
%token <word> SZ_STRING
%token <word> SZ_STRUCT
%token <word> SZ_TYPEDEF
%token <word> SZ_UNION
%token <number> SZ_NUMBER

%type <word> struct_definition
%type <word> declarations single_declaration
%type <word> data_type data_members single_data_member
%type <word> word
%type <word> dimensions					/* FIXME: change <word> again to <dimensions> */
%type <number> single_dimension

%%

file:						/* empty */					{ ; }
 |							file SZ_STRING				{ ; }
 |							file struct_definition		{ ; }
 ;

struct_definition:			optional_typedef SZ_STRUCT word '{' declarations '}' word ';'
									{ cout << "\nstructure extracted: " << *$<word>3 << " " << *$<word>7 << '\n'; }
							/* FIXME: When primary or secondary typedefed struct name is not present,
							 *        then it should be handled.
							 */
 ;

optional_typedef:			/* empty */									{ ; }
 |							SZ_TYPEDEF									{ ; }
 ;

declarations:				/* empty */									{ ; }
 |							declarations single_declaration				{ ; }
 ;

single_declaration:			data_type data_members ';' optional_new_line	{
																				SingleElement single_element = new SingleElement;
																			}
 ;

data_type:					SZ_STRING					{ cout << "\t" << *$<word>1;		}
 |							SZ_STRUCT SZ_STRING			{ cout << "\tstruct " << *$<word>2;	}
 ;

data_members:				single_data_member					{ ; }
 |							data_members ',' single_data_member	{ ; }

single_data_member:			variable_name dimensions				{ ;	}
 |							'(' variable_name dimensions ')'		{ ;	}
 |							'(' variable_name ')' dimensions		{ ;	}
 ;
							/* FIXME: If variables can be declared like:
							 * int [10] a ;
							 * then, this should be fixed.
							 */

variable_name:				pointers SZ_STRING				{
																cout << " " << *$<word>2;
																Dimensions dimensions = new Dimensions;
															}
 ;

pointers:					/* empty */						{ ; }
 |							pointers '*'					{ cout << " *"; }
 ;

word:						/* empty */						{ ; }
 |							SZ_STRING						{ $<word>$ = new string(*$<word>1); delete $<word>1; }
 ;

dimensions:					/* empty */						{ ; }
 |							dimensions single_dimension		{ ; }
 ;

single_dimension:			'[' SZ_NUMBER ']'				{
																dimensions.insert($<number>2);
																cout << " [" << $<number>2 << "]" ;
															}
 ;

optional_new_line:			/* empty */
 |							'\n'
 ;

%%

void yy::Parser::error(const location_type &l, const string &message)
{
	driver.error(message);
}
