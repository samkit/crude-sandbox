	/* Search FIXME to fix */
	/* Search CHECKME to test */
	/* Search UNCOMMENT to uncomment code */
	/* Search PERFORMANCE to get a performace fix */

	/*
	 * Objective:
	 * 1. Remove comments.
	 * 2. Recognize tokens.
	 *
	 * Pre-requisite:
	 * 1. C code should be compilable.
	 * 2. C code should be precompiled.
	 *
	 * Precaution:
	 * 1. All matches are greedy in nature,
	 *    and tries to match longest matching string.
	 *    As a workaround, we are checking single characters
	 *    when we could have done with .* greedy set.
	 *    This is will be overhead and should be in FIXME.
	 *    Using (?s:.) in place of (?s:.)* is a tradeoff and
	 *    will impact performace.
	 *
	 * Known limitations:
	 * 1. Cannot remove inline comments spanning multiple lines,
	 *    using line continuation character.
	 */
%{
	#include <string>
	#include "parser.hh"
	#include "Driver.h"
	using namespace yy;
	using namespace std;
	#define yyterminate() return yy::Parser::token::END
%}

%option outfile="lexer.cpp"
%option noyywrap

WORD [[:alpha:]_][[:alnum:]_]*

NUMBER [[:digit:]]+

%x INSIDE_COMMENTS
%x INSIDE_STRING

%%

<*>(?s:\\\n)						{
										yyless(yyleng - 2);
										yyinput();
										yyinput();
									}
									/* eat line continuation character
									 * 1. CHECKME: Check without below condition <*>\\$
									 *    and output should match other than line
									 *    continuation character.
									 */

\"									BEGIN(INSIDE_STRING);
<INSIDE_STRING>\"					BEGIN(INITIAL);
<INSIDE_STRING>(?s:.)				/* eat string literals, as they cannot be part of struct. */
									/* PERFORMANCE: Here we cannot use (?s:.)* because of it greedy nature. */
									/* Using (?s:.) is a tradeoff and will impact performace.
									 * CHECKME: To test greedy nature, see test case program.
									 * remove_comment_from_this.c
									 */


"/*"								BEGIN(INSIDE_COMMENTS);		/* eat multiline comments -> starts */
<INSIDE_COMMENTS>"*/"				BEGIN(INITIAL);				/* eat multiline comments <- ends */
<INSIDE_COMMENTS>(?s:.)				/* eat multiline comments. */
									/* PERFORMANCE: Here we cannot use (?s:.)* because of it greedy nature.*/
									/* Using (?s:.) is a tradeoff and will impact performace.
									 * CHECKME: To test greedy nature, see test case program.
									 * remove_comment_from_this.c
									 */

"//".*								/* remove inline comments */
									/* FIXME: inline comments spanning multiple
									 * lines by using line continuation character,
									 * are not removed.
									 */

^[[:space:]]*#.*					/* eat preprocessor directives */

struct								return Parser::token::SZ_STRUCT;

typedef								return Parser::token::SZ_TYPEDEF;

union								return Parser::token::SZ_UNION;

{WORD}								{
										yylval->word = new string(yytext);
										return Parser::token::SZ_STRING;
									}

{NUMBER}							{
										yylval->number = atol(yytext);
										/* FIXME: Add suitable code to handle
										 * yylval.number == 0
										 */
										return Parser::token::SZ_NUMBER;
									}
"*"  |
";"  |
"("  |
")"  |
"{"  |
"}"  |
"]"  |
"["									{ return Parser::token_type(yytext[0]); }

.									;/* UNCOMMENT: add suitable code */

%%

Driver::Driver(const string &file_name)
:file(file_name)
{
	yyin = (FILE *)fopen(file.c_str(), "r");
	if(NULL == yyin) {
		cout << "Error opening input file " << file << endl;
		exit(1);
	}
	cout << "File " << file << " opened\n";
}

Driver::~Driver()
{
	cout << "Closing file " << file << endl;
	fclose(yyin);
}

int Driver::parse()
{
	yy::Parser parser(*this);

	return parser.parse();
}

void Driver::error(const string &message)
{
	cout << "Error: " << message << endl;
}
