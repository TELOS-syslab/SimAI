file(REMOVE_RECURSE
  "../../../build/lib/libns3.36.1-applications-debug.pdb"
  "../../../build/lib/libns3.36.1-applications-debug.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/libapplications.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
