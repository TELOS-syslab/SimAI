file(REMOVE_RECURSE
  "../../../build/lib/libns3.36.1-bridge-debug.pdb"
  "../../../build/lib/libns3.36.1-bridge-debug.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/libbridge.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
