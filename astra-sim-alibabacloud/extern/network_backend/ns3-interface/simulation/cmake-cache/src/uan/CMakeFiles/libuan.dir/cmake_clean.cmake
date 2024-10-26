file(REMOVE_RECURSE
  "../../../build/lib/libns3.36.1-uan-debug.pdb"
  "../../../build/lib/libns3.36.1-uan-debug.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/libuan.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
