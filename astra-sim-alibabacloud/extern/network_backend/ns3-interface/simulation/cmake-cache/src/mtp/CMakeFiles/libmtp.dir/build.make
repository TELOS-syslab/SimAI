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
include src/mtp/CMakeFiles/libmtp.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/mtp/CMakeFiles/libmtp.dir/compiler_depend.make

# Include the progress variables for this target.
include src/mtp/CMakeFiles/libmtp.dir/progress.make

# Include the compile flags for this target's objects.
include src/mtp/CMakeFiles/libmtp.dir/flags.make

# Object files for target libmtp
libmtp_OBJECTS =

# External object files for target libmtp
libmtp_EXTERNAL_OBJECTS = \
"/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp/CMakeFiles/libmtp-obj.dir/model/logical-process.cc.o" \
"/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp/CMakeFiles/libmtp-obj.dir/model/mtp-interface.cc.o" \
"/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp/CMakeFiles/libmtp-obj.dir/model/multithreaded-simulator-impl.cc.o"

../build/lib/libns3.36.1-mtp-debug.so: src/mtp/CMakeFiles/libmtp-obj.dir/model/logical-process.cc.o
../build/lib/libns3.36.1-mtp-debug.so: src/mtp/CMakeFiles/libmtp-obj.dir/model/mtp-interface.cc.o
../build/lib/libns3.36.1-mtp-debug.so: src/mtp/CMakeFiles/libmtp-obj.dir/model/multithreaded-simulator-impl.cc.o
../build/lib/libns3.36.1-mtp-debug.so: src/mtp/CMakeFiles/libmtp.dir/build.make
../build/lib/libns3.36.1-mtp-debug.so: /usr/lib/x86_64-linux-gnu/librt.a
../build/lib/libns3.36.1-mtp-debug.so: /usr/lib/x86_64-linux-gnu/libsqlite3.so
../build/lib/libns3.36.1-mtp-debug.so: src/mtp/CMakeFiles/libmtp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Linking CXX shared library ../../../build/lib/libns3.36.1-mtp-debug.so"
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/libmtp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/mtp/CMakeFiles/libmtp.dir/build: ../build/lib/libns3.36.1-mtp-debug.so
.PHONY : src/mtp/CMakeFiles/libmtp.dir/build

src/mtp/CMakeFiles/libmtp.dir/clean:
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp && $(CMAKE_COMMAND) -P CMakeFiles/libmtp.dir/cmake_clean.cmake
.PHONY : src/mtp/CMakeFiles/libmtp.dir/clean

src/mtp/CMakeFiles/libmtp.dir/depend:
	cd /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/src/mtp /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp /mnt/fth/software2/SimAI/astra-sim-alibabacloud/extern/network_backend/ns3-interface/simulation/cmake-cache/src/mtp/CMakeFiles/libmtp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/mtp/CMakeFiles/libmtp.dir/depend
