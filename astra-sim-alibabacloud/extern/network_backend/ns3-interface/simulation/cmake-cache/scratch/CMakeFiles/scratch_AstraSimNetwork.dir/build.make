# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache

# Include any dependencies generated for this target.
include scratch/CMakeFiles/scratch_AstraSimNetwork.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include scratch/CMakeFiles/scratch_AstraSimNetwork.dir/compiler_depend.make

# Include the progress variables for this target.
include scratch/CMakeFiles/scratch_AstraSimNetwork.dir/progress.make

# Include the compile flags for this target's objects.
include scratch/CMakeFiles/scratch_AstraSimNetwork.dir/flags.make

scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o: scratch/CMakeFiles/scratch_AstraSimNetwork.dir/flags.make
scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o: ../scratch/AstraSimNetwork.cc
scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o: scratch/CMakeFiles/scratch_AstraSimNetwork.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o -MF CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o.d -o CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o -c /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/scratch/AstraSimNetwork.cc

scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.i"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/scratch/AstraSimNetwork.cc > CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.i

scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.s"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/scratch/AstraSimNetwork.cc -o CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.s

# Object files for target scratch_AstraSimNetwork
scratch_AstraSimNetwork_OBJECTS = \
"CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o"

# External object files for target scratch_AstraSimNetwork
scratch_AstraSimNetwork_EXTERNAL_OBJECTS =

../build/scratch/ns3.36.1-AstraSimNetwork-debug: scratch/CMakeFiles/scratch_AstraSimNetwork.dir/AstraSimNetwork.cc.o
../build/scratch/ns3.36.1-AstraSimNetwork-debug: scratch/CMakeFiles/scratch_AstraSimNetwork.dir/build.make
../build/scratch/ns3.36.1-AstraSimNetwork-debug: /usr/lib/x86_64-linux-gnu/libsqlite3.so
../build/scratch/ns3.36.1-AstraSimNetwork-debug: /usr/lib/x86_64-linux-gnu/librt.a
../build/scratch/ns3.36.1-AstraSimNetwork-debug: /usr/lib/x86_64-linux-gnu/libxml2.so
../build/scratch/ns3.36.1-AstraSimNetwork-debug: /usr/lib/x86_64-linux-gnu/libxml2.so
../build/scratch/ns3.36.1-AstraSimNetwork-debug: /usr/lib/x86_64-linux-gnu/libsqlite3.so
../build/scratch/ns3.36.1-AstraSimNetwork-debug: /usr/lib/x86_64-linux-gnu/librt.a
../build/scratch/ns3.36.1-AstraSimNetwork-debug: scratch/CMakeFiles/scratch_AstraSimNetwork.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../build/scratch/ns3.36.1-AstraSimNetwork-debug"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/scratch_AstraSimNetwork.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
scratch/CMakeFiles/scratch_AstraSimNetwork.dir/build: ../build/scratch/ns3.36.1-AstraSimNetwork-debug
.PHONY : scratch/CMakeFiles/scratch_AstraSimNetwork.dir/build

scratch/CMakeFiles/scratch_AstraSimNetwork.dir/clean:
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch && $(CMAKE_COMMAND) -P CMakeFiles/scratch_AstraSimNetwork.dir/cmake_clean.cmake
.PHONY : scratch/CMakeFiles/scratch_AstraSimNetwork.dir/clean

scratch/CMakeFiles/scratch_AstraSimNetwork.dir/depend:
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/scratch /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/scratch/CMakeFiles/scratch_AstraSimNetwork.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : scratch/CMakeFiles/scratch_AstraSimNetwork.dir/depend

