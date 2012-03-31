	#include <stdio.h>

#define BEFORE_COMMENT_1 // comment 1	/* comment inside comment */

/* comment 2 */

/*
	comment 3
//	comment inside comment
*/

// comment 4 spanning multiple lines

typedef struct xyz {
	char *x;
} xyz_t;

typedef struct single_line_struct { \
	char single_char; \
} single_line_struct_t;

typedef struct abc {
	int a;
	int b[20];
	char c[20][20];
} abc_t;

int main()
{
	printf("Hello\
World\n");

	printf("/* comment inside string */");
	return 0;
}
