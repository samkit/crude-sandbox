ROOT_DIR := $(PWD)

CC := g++
CXXFLAGS += $(all_inc:%=-I%)
LDFLAGS += -L.
LDFLAGS += $(all_libraries:lib%.a=-l%)

object_storage := $(ROOT_DIR)/objs
lib_storage := $(ROOT_DIR)/libs

vpath %.hpp $(modules)
vpath %.cpp $(modules)

-include $(modules:%=%/Makevars.mk)
