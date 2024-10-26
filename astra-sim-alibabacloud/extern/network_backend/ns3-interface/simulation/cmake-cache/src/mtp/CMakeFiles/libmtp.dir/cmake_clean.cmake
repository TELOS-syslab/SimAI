file(REMOVE_RECURSE
  "../../../build/lib/libns3.36.1-mtp-debug.pdb"
  "../../../build/lib/libns3.36.1-mtp-debug.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/libmtp.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
