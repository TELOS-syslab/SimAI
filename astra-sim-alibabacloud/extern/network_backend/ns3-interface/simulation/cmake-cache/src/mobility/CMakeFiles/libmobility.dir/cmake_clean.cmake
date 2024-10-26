file(REMOVE_RECURSE
  "../../../build/lib/libns3.36.1-mobility-debug.pdb"
  "../../../build/lib/libns3.36.1-mobility-debug.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/libmobility.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
