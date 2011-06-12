local_dir := $(ROOT_DIR)/src1
local_src := print_hello.cpp
local_objects := $(local_src:%.cpp=$(local_dir)/%.o)
local_libraries := $(local_dir)/libprinthello.a

all_inc += $(ROOT_DIR)/src1
all_objects += $(local_objects)
all_libraries += $(local_libraries)

$(local_libraries): $(local_objects)
	@echo $(local_libraries) $(local_objects)
	$(AR) r $@ $^

include $(wildcard $(ROOT_DIR)/deps/*.deps)
