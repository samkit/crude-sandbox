# Top level non recursive makefile

include Makevars.mk

all_inc :=
all_objects :=
all_libraries :=
all_targets :=

all:

modules := src1 src2

include $(modules:%=%/Makefile)

include Makerules.mk
