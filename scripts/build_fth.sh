```bash
SCRIPT_DIR=$(dirname "$(realpath $0)") # 获取当前脚本所在目录的绝对路径，并赋给变量SCRIPT_DIR
ROOT_DIR=$(realpath "${SCRIPT_DIR:?}"/..) # 获取当前脚本所在父目录的绝对路径，并赋给ROOT_DIR
NS3_DIR="${ROOT_DIR:?}"/ns-3-alibabacloud # 设置NS3目录路径
SIMAI_DIR="${ROOT_DIR:?}"/astra-sim-alibabacloud # 设置SIMAI目录路径
SOURCE_NS3_BIN_DIR="${SIMAI_DIR:?}"/extern/network_backend/ns3-interface/simulation/build/scratch/ns3.36.1-AstraSimNetwork-debug # 设置NS3二进制文件路径
SOURCE_ANA_BIN_DIR="${SIMAI_DIR:?}"/build/simai_analytical/build/simai_analytical/SimAI_analytical # 设置分析模拟器二进制文件路径
SOURCE_PHY_BIN_DIR="${SIMAI_DIR:?}"/build/simai_phy/build/simai_phynet/SimAI_phynet # 设置物理网络二进制文件路径

TARGET_BIN_DIR="${SCRIPT_DIR:?}"/../bin # 设置目标二进制目录路径
function compile { # 定义一个名为compile的函数
    local option="$1" # 接收函数参数
    case "$option" in # 根据传入的参数执行不同的操作
    "ns3")
        mkdir -p "${TARGET_BIN_DIR:?}" # 创建目标二进制目录路径
        rm -rf "${SIMAI_DIR:?}"/extern/network_backend/ns3-interface/ # 删除原有的模拟器接口目录
        mkdir -p "${SIMAI_DIR:?}"/extern/network_backend/ns3-interface # 创建新的模拟器接口目录
        cp -r "${NS3_DIR:?}"/* "${SIMAI_DIR:?}"/extern/network_backend/ns3-interface # 复制NS3代码到接口目录
        cd "${SIMAI_DIR:?}" # 切换到SIMAI目录
        ./build.sh -lr ns3 # 构建并链接NS3相关模块
        ./build.sh -c ns3 # 编译NS3模块
        ln -s "${SOURCE_NS3_BIN_DIR:?}" "${TARGET_BIN_DIR:?}"/SimAI_simulator;; # 创建NS3模拟器的符号链接
    "phy")
        mkdir -p "${TARGET_BIN_DIR:?}" # 创建目标二进制目录路径
        cd "${SIMAI_DIR:?}" # 切换到SIMAI目录
        ./build.sh -lr phy # 构建并链接物理网络相关模块
        ./build.sh -c phy # 编译物理网络模块
        ln -s "${SOURCE_PHY_BIN_DIR:?}" "${TARGET_BIN_DIR:?}"/SimAI_phynet;; # 创建物理网络二进制文件的符号链接
    "analytical")
        mkdir -p "${TARGET_BIN_DIR:?}" # 创建目标二进制目录路径
        mkdir -p "${ROOT_DIR:?}"/results # 创建存储结果的目录
        cd "${SIMAI_DIR:?}" # 切换到SIMAI目录
        ./build.sh -lr analytical # 构建并链接分析模块
        ./build.sh -c analytical # 编译分析模块
        ln -s "${SOURCE_ANA_BIN_DIR:?}" "${TARGET_BIN_DIR:?}"/SimAI_analytical;; # 创建分析模拟器的符号链接
    esac
}

function cleanup_build { # 定义一个名为cleanup_build的函数用于清理构建
    local option="$1" # 接收函数参数
    case "$option" in # 根据传入的参数执行不同的操作
    "ns3")
        rm  "${TARGET_BIN_DIR:?}"/SimAI_simulator # 删除NS3模拟器的符号链接
        rm -rf "${SIMAI_DIR:?}"/extern/network_backend/ns3-interface/ # 删除NS3接口目录
        cd "${SIMAI_DIR:?}" # 切换到SIMAI目录
        ./build.sh -lr ns3;; # 清理NS3相关模块
    "phy")
        rm  "${TARGET_BIN_DIR:?}"/SimAI_phynet # 删除物理网络二进制文件的符号链接
        cd "${SIMAI_DIR:?}" # 切换到SIMAI目录
        ./build.sh -lr phy;; # 清理物理网络相关模块
    "analytical")
        rm  "${TARGET_BIN_DIR:?}"/SimAI_analytical # 删除分析模拟器的符号链接
        cd "${SIMAI_DIR:?}" # 切换到SIMAI目录
        ./build.sh -lr analytical;; # 清理分析模块
    esac
}

# Main Script
case "$1" in # 根据传入的参数执行不同的操作
-l|--clean)
    cleanup_build "$2";; # 清理构建
-c|--compile)
    compile "$2";; # 编译
-h|--help|*)
    printf -- "help message\n" # 打印帮助信息
    printf -- "-c|--compile mode supported ns3/phy/analytical  (example:./build.sh -c ns3)\n" # 打印编译模式示例
    printf -- "-l|--clean  (example:./build.sh -l ns3)\n" # 打印清理模式示例
    printf -- "-lr|--clean-result mode  (example:./build.sh -lr ns3)\n" # 打印清理结果模式示例
esac
```