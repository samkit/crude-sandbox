all: $(all_objects) $(all_libraries) $(all_targets)

clean:
	$(RM) $(all_objects) $(all_libraries) $(all_targets)

%: %.o
	$(CXX) -g -o $@ $^ $(LDFLAGS)

include $(modules:%=%/Makerules.mk)
