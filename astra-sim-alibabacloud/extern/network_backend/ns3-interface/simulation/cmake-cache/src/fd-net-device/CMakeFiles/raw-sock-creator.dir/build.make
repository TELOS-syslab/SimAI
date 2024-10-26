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
include src/fd-net-device/CMakeFiles/raw-sock-creator.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/fd-net-device/CMakeFiles/raw-sock-creator.dir/compiler_depend.make

# Include the progress variables for this target.
include src/fd-net-device/CMakeFiles/raw-sock-creator.dir/progress.make

# Include the compile flags for this target's objects.
include src/fd-net-device/CMakeFiles/raw-sock-creator.dir/flags.make

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/flags.make
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o: ../src/fd-net-device/helper/creator-utils.cc
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o -MF CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o.d -o CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o -c /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/creator-utils.cc

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.i"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/creator-utils.cc > CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.i

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.s"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/creator-utils.cc -o CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.s

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/flags.make
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o: ../src/fd-net-device/helper/encode-decode.cc
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o -MF CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o.d -o CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o -c /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/encode-decode.cc

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.i"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/encode-decode.cc > CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.i

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.s"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/encode-decode.cc -o CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.s

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/flags.make
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o: ../src/fd-net-device/helper/raw-sock-creator.cc
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o -MF CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o.d -o CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o -c /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/raw-sock-creator.cc

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.i"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/raw-sock-creator.cc > CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.i

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.s"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device/helper/raw-sock-creator.cc -o CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.s

# Object files for target raw-sock-creator
raw__sock__creator_OBJECTS = \
"CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o" \
"CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o" \
"CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o"

# External object files for target raw-sock-creator
raw__sock__creator_EXTERNAL_OBJECTS =

../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/creator-utils.cc.o
../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/encode-decode.cc.o
../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/helper/raw-sock-creator.cc.o
../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/build.make
../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug: src/fd-net-device/CMakeFiles/raw-sock-creator.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable ../../../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/raw-sock-creator.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/fd-net-device/CMakeFiles/raw-sock-creator.dir/build: ../build/src/fd-net-device/ns3.36.1-raw-sock-creator-debug
.PHONY : src/fd-net-device/CMakeFiles/raw-sock-creator.dir/build

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/clean:
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device && $(CMAKE_COMMAND) -P CMakeFiles/raw-sock-creator.dir/cmake_clean.cmake
.PHONY : src/fd-net-device/CMakeFiles/raw-sock-creator.dir/clean

src/fd-net-device/CMakeFiles/raw-sock-creator.dir/depend:
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/fd-net-device /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/fd-net-device/CMakeFiles/raw-sock-creator.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/fd-net-device/CMakeFiles/raw-sock-creator.dir/depend

