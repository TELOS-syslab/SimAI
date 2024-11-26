# 更新原仓库

##  github fork过的仓库 ， 怎么保证和原仓库同步， 原仓库的更新怎么同步到fork的仓库里面来？  中文回答

在 GitHub 上，如果你 fork 了一个仓库，并希望将原仓库的更新同步到你的 fork 中，可以按照以下步骤操作：

添加上游仓库 (Upstream Repository) 作为远程仓库： 首先，确保你的本地仓库已经关联了原仓库（即上游仓库）。如果你没有添加过上游仓库，可以通过以下命令添加：

git remote add upstream <原仓库的URL>
例如，如果原仓库是 https://github.com/original_owner/repository_name.git，你可以执行：

git remote add upstream https://github.com/original_owner/repository_name.git

git remote add upstream git@github.com:aliyun/SimAI.git

git remote add upstream git@github.com:aliyun/aicb.git
获取原仓库的最新更新： 使用 git fetch 从上游仓库获取最新的更新：

git fetch upstream
合并上游的更新到你的 fork： 获取到上游仓库的更新后，你需要将其合并到你的本地分支。假设你想将更新合并到 main 分支，可以执行以下命令：

git checkout main  # 切换到你的 main 分支
git merge upstream/main  # 将 upstream 仓库的 main 分支合并到你的本地 main 分支
如果你在其他分支上工作，也可以将其合并到对应的分支。

解决冲突（如果有的话）： 如果合并时出现冲突，Git 会提示你手动解决冲突。解决冲突后，记得提交变更：

git add .
git commit -m "Resolved merge conflicts"
推送到你的 GitHub 仓库： 最后，更新合并后的分支推送到你自己的 GitHub 仓库：

git push origin main
小结
通过以上步骤，你可以将原仓库的更新同步到你的 fork 仓库中，确保你的 fork 保持与原仓库的同步。

你也可以定期执行 git fetch upstream 和 git merge upstream/main 来确保你的 fork 不会过时。

# SimAI Components   组件结构

git config --global user.email "843101550@qq.com"

git config --global user.email "tianhao909"

* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/upstream/master

git remote add upstream https://github.com/aliyun/SimAI
git fetch upstream
git checkout remotes/upstream/master
git merge upstream/master

git push origin master

bash  && conda activate fth01


<pre>
        |--- <a href="https://github.com/aliyun/aicb">AICB</a>
SimAI --|--- <a href="https://github.com/aliyun/SimCCL">SimCCL</a>
        |--- <a href="https://github.com/aliyun/SimAI/tree/master/astra-sim-alibabacloud">astra-sim-alibabacloud</a>
        |--- <a href="https://github.com/aliyun/ns-3-alibabacloud">ns-3-alibabacloud</a>
</pre>

这部分展示了 SimAI 的主要组件，每个组件都链接到其 GitHub 仓库，方便访问代码和文档。以下是组件介绍：
AICB: 阿里云的 AI 通信测试工具。
SimCCL: 针对 AI 集体通信的模拟器。
astra-sim-alibabacloud: 一个用于详细 AI 负载模拟的扩展仿真环境。
ns-3-alibabacloud: 自定义版本的 ns-3 网络模拟器。

# Table of Contents
- [SimAI Overview](#simai-overview)
  - [Introduction](#introduction)
  - [Citation](#citation)
- [Usage](#usage)
  - [Setup](#setup)
    - [From Source Code](#from-source-code)
  - [Use SimAI-Analytical](#use-simai-analytical)
  - [Use SimAI-Simulation](#use-simai-simulation)

# SimAI Overview
## Introduction

**SimAI** is the industry's first full-stack, high-precision **Sim**ulator for **AI** large-scale training. It provides detailed modeling and simulation of the entire LLM training process, encompassing framework, collective communication, network layers, and more. This comprehensive approach offers end-to-end performance data, enabling researchers to:
SimAI 是业内首个全栈高精度的AI大规模训练仿真器。它能对整个大型语言模型（LLM）训练过程进行详细建模和仿真，涵盖框架、集体通信、网络层等。此综合方法提供端到端性能数据，使研究人员可以：

- Analyze training process details 
分析训练过程细节

- Evaluate the time consumption of AI tasks under specific conditions
评估特定条件下 AI 任务的时间消耗

- Evaluate E2E performance gains from various algorithmic optimizations including:
评估各种算法优化的端到端性能提升，包括：

  - Framework parameters settings 框架参数设置
  - Collective communication algorithms 集体通信算法
  - NCCL environment variables NCCL 环境变量
  - Network transmission protocols 网络传输协议
  - Congestion control algorithms 拥塞控制算法
  - Adaptive routing algorithms 自适应路由算法
  - Scale-up/out network topology modifications 网络拓扑结构的横向/纵向扩展
  - ...




Building on pure simulation capabilities, SimAI has evolved into a versatile full-stack toolkit comprising four components ([aicb](https://github.com/aliyun/aicb), [SimCCL](https://github.com/aliyun/SimCCL), [astra-sim-alibabacloud](https://github.com/aliyun/SimAI/tree/master/astra-sim-alibabacloud), [ns-3-alibabacloud](https://github.com/aliyun/ns-3-alibabacloud)). These components can be combined in various ways to achieve different functionalities. Below, we present the six main usage scenarios for SimAI. We encourage users to explore even more possibilities with this powerful tool.
SimAI 已从单纯的仿真能力发展为一个多功能的全栈工具包，由四个组件（aicb、SimCCL、astra-sim-alibabacloud和ns-3-alibabacloud）组成。这些组件可以按多种方式组合，以实现不同功能。以下列出了 SimAI 的六大主要使用场景，并鼓励用户探索更多可能性。

| Scenario | Description | Component Combination |
场景	描述	组件组合
|----------|-------------|------------------------|
| 1. AICB Test Suite | Run communication patterns on GPU clusters using AICB Test suite | [AICB](https://github.com/aliyun/aicb) |
1. AICB 测试套件	使用 AICB 测试套件在 GPU 集群上运行通信模式	AICB

| 2. AICB/AIOB Workload | Model compute/communication patterns of training process to generate workload | [AICB](https://github.com/aliyun/aicb) |
2. AICB/AIOB 工作负载	建模训练过程中的计算/通信模式以生成工作负载	AICB

| 3. Collective Comm Analyze | Break down collective communication operations into point-to-point communication sets | [SimCCL](https://github.com/aliyun/SimCCL) |
3. 集体通信分析	将集体通信操作分解为点对点通信集	SimCCL

| 4. Collective Comm w/o GPU | Perform RDMA collective communication traffic on non-GPU clusters | [AICB](https://github.com/aliyun/aicb) + [SimCCL](https://github.com/aliyun/SimCCL) + [astra-sim-alibabacloud](https://github.com/aliyun/SimAI/tree/master/astra-sim-alibabacloud)(physical) |
4. 无 GPU 的集体通信	在非 GPU 集群上执行 RDMA 集体通信流量	AICB + SimCCL + astra-sim-alibabacloud(物理层)

| 5. SimAI-Analytical | Conduct rapid AICB workload analysis and simulation on any server (ignoring underlying network details) | [AICB](https://github.com/aliyun/aicb) + [astra-sim-alibabacloud](https://github.com/aliyun/SimAI/tree/master/astra-sim-alibabacloud)(analytical) |
5. SimAI-Analytical	在任意服务器上快速进行 AICB 工作负载分析和仿真（忽略底层网络细节）	AICB + astra-sim-alibabacloud(分析层)

| 6. SimAI-Simulation | Perform full simulation on any server | [AICB](https://github.com/aliyun/aicb) + [SimCCL](https://github.com/aliyun/SimCCL) + [astra-sim-alibabacloud](https://github.com/aliyun/SimAI/tree/master/astra-sim-alibabacloud)(simulation) + [ns-3-alibabacloud](https://github.com/aliyun/ns-3-alibabacloud) |
6. SimAI-Simulation	在任意服务器上进行全仿真	AICB + SimCCL + astra-sim-alibabacloud(仿真层) + ns-3-alibabacloud




Below is the architecture diagram of the SimAI Simulator:  
SimAI 仿真器的架构图如下：
![SimAI_Arc](./docs/images/SimAI_Arc.png)

astra-sim-alibabacloud is extended from [astra-sim](https://github.com/astra-sim/astra-sim/tree/ASTRA-sim-1.0), we have integrated NCCL algorithms and added some new features.
astra-sim-alibabacloud 是基于 astra-sim 的扩展版，我们已集成 NCCL 算法并添加了一些新功能。

## Citation

SimAI work has been accepted by NSDI'25 Spring, and it'll be showcased soon.
SimAI的研究成果已被NSDI'25春季会议接收，并即将展示。

Paper name is "SimAI: Unifying Architecture Design and Performance Tunning for Large-Scale Large Language Model Training with Scalability and Precision"  [pdf]() / [slides]() / [video]()
论文标题为“SimAI：统一架构设计与性能调优，实现大规模大语言模型训练的可扩展性和精度”。pdf / slides / video

# Usage

Here are some simple examples, SimAI full tutorials can be found here: [**SimAI@Tutorial**](docs/Tutorial.md), [**aicb@Tutorial**](https://github.com/aliyun/aicb/blob/master/training/tutorial.md), [SimCCL@Tutorial], [ns-3-alibabacloud@Tutorial]
以下是一些简单的示例，SimAI完整的教程可在以下链接中找到：SimAI@Tutorial，aicb@Tutorial，[SimCCL@Tutorial]，[ns-3-alibabacloud@Tutorial]

## Setup 安装

You can follow the instrucitons below to quickly set up the environtments and run SimAI
按照以下说明可以快速设置环境并运行SimAI。

### From Source Code 从源代码安装

The following code has been successfully tested on GCC/G++ 9.4.0, python 3.8.10 in Ubuntu 20.04
以下代码已在GCC/G++ 9.4.0、Python 3.8.10环境下通过测试，系统版本为Ubuntu 20.04。

```bash
# Clone the repository 克隆代码库
$ git clone https://github.com/aliyun/SimAI.git
$ cd ./SimAI/

# Clone submodules 克隆子模块
$ git submodule update --init --recursive
# Make sure use the newest commit 确保使用最新的提交版本
$ git submodule update --remote

# Compile SimAI-Analytical 编译SimAI-Analytical
$ ./scripts/build.sh -c analytical

# Compile SimAI-Simulation (ns3) 编译SimAI-Simulation (ns3)
$ ./scripts/build.sh -c ns3

```

## Use SimAI-Analytical 使用SimAI-Analytical

```bash
$  ./bin/SimAI_analytical -w example/workload_analytical.txt -g 1024 -g_p_s 8 -r results/test- -busbw example/busbw.yaml
```
这里是如何使用SimAI的分析模块的示例。命令行中各参数的含义如下：
-w example/workload_analytical.txt：指定工作负载文件；
-g 1024：表示使用1024个GPU；
-g_p_s 8：每个服务器使用8个GPU；
-r results/test-：输出结果文件前缀；
-busbw example/busbw.yaml：指定带宽文件。
这个命令用于在给定工作负载和配置下执行分析模拟，并输出结果。


## Use SimAI-Simulation  使用SimAI-Simulation

```bash
# Create network topo
$ python3 ./astra-sim-alibabacloud/inputs/topo/gen_HPN_7.0_topo_mulgpus_one_link.py -g 128 -gt A100 -bw 400Gbps -nvbw 2400Gbps

# Running
$ AS_SEND_LAT=3 AS_NVLS_ENABLE=1 ./bin/SimAI_simulator -t 16 -w ./example/microAllReduce.txt -n ./HPN_7_0_128_gpus_8_in_one_server_with_400Gbps_A100

```
此部分是SimAI仿真模块的使用示例：
创建网络拓扑：使用Python脚本生成一个网络拓扑配置。
-g 128：表示使用128个GPU；
-gt A100：指定GPU型号为A100；
-bw 400Gbps：单个链路带宽400Gbps；
-nvbw 2400Gbps：NVLink总带宽2400Gbps。

运行仿真：
AS_SEND_LAT=3：设置网络发送延迟为3微秒；
AS_NVLS_ENABLE=1：启用NVLink仿真；
./bin/SimAI_simulator -t 16：启动16线程运行仿真；
-w ./example/microAllReduce.txt：使用AllReduce示例工作负载文件；
-n ./HPN_7_0_128_gpus_8_in_one_server_with_400Gbps_A100：使用生成的拓扑文件。
此命令用于在指定网络拓扑、带宽、延迟等配置下运行仿真，并模拟分布式计算过程。
