#include <string.h>
#include "Driver.h"

int main(int argc, char **argv)
{
	Driver driver(argv[1]);

	return driver.parse();
}
