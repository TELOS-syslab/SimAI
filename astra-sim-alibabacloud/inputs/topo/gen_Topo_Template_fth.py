# """
# 此文件可以生成 AlibabaHPN、Spectrum-X、DCN+ 的拓扑结构。
# 用户可以根据需要自由定制拓扑。
# """

import argparse
import warnings

def Rail_Opti_SingleToR(parameters):
    # 获取每个 ASW（接入交换机）连接的节点数
    nodes_per_asw = parameters['nics_per_aswitch']
    # 获取每个段中的 ASW 交换机数，这里假设每个服务器的 GPU 数量作为 ASW 的数量
    asw_switch_num_per_segment = parameters['gpu_per_server']
    # 计算段数，根据总 GPU 数和每个段中的节点数（nodes_per_asw * asw_switch_num_per_segment）
    if(parameters['gpu'] % (nodes_per_asw * asw_switch_num_per_segment) == 0):
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment))
    else:
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment))+1
    
    # 检查段数是否与 ASW 交换机数匹配，如果不匹配则调整 ASW 交换机数并发出警告
    if(segment_num != parameters['asw_switch_num'] / asw_switch_num_per_segment):
        warnings.warn("Error relations between total GPU Nums and total aws_switch_num.\n \
                         The correct asw_switch_num is set to "+str(segment_num * asw_switch_num_per_segment))
        parameters['asw_switch_num'] = segment_num * asw_switch_num_per_segment
    # 打印 ASW 交换机数
    print("asw_switch_num: " + str(parameters['asw_switch_num']))
    # 检查段数是否超过单个 Pod 的容量，如果超过则抛出异常
    if segment_num > int(parameters['asw_per_psw'] /  asw_switch_num_per_segment):
        raise ValueError("Number of GPU exceeds the capacity of Rail_Optimized_SingleToR(One Pod)")
    # 设置 Pod 数为 1
    pod_num = 1
    # 打印 PSW（聚合交换机）交换机数
    print("psw_switch_num: " + str(parameters['psw_switch_num']))
    # 打印拓扑创建信息，包括段数和 Pod 数
    print("Creating Topology of totally " + str(segment_num) + " segment(s), totally "+ str(pod_num) + " pod(s)." )  

    # 计算 NV（网络虚拟化）交换机数，根据 GPU 数和每个服务器的 NV 交换机数
    nv_switch_num = (int)(parameters['gpu'] / parameters['gpu_per_server']) * parameters['nv_switch_per_server']
    # 计算总节点数，包括 GPU、ASW、PSW 和 NV 交换机
    nodes = (int) (parameters['gpu'] + parameters['asw_switch_num'] + parameters['psw_switch_num']+ nv_switch_num ) # 
    # 计算服务器数，根据 GPU 数和每个服务器的 GPU 数
    servers = parameters['gpu'] / parameters['gpu_per_server']
    # 计算交换机节点数，包括 PSW、ASW 和 NV 交换机
    switch_nodes = (int)(parameters['psw_switch_num'] + parameters['asw_switch_num'] + nv_switch_num) # 
    # 计算链接数，包括 PSW 到 ASW 的链接、服务器到 ASW 的链接以及服务器到 NV 交换机的链接
    links = (int)(parameters['psw_switch_num']/pod_num * parameters['asw_switch_num'] + servers * asw_switch_num_per_segment
                  + servers * parameters['nv_switch_per_server'] * parameters['gpu_per_server']) # 
    # 根据拓扑类型设置文件名
    if parameters['topology'] == 'Spectrum-X':
        file_name = "Spectrum-X_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    else:
        file_name = "Rail_Opti_SingleToR_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    # 打开文件进行写入
    with open(file_name, 'w') as f:
        # 打印文件名
        print(file_name)
        # 构造第一行，包含节点数、每个服务器的 GPU 数、NV 交换机数、其他交换机数、链接数和 GPU 类型
        first_line = str(nodes)+" "+str(parameters['gpu_per_server'])+" "+str(nv_switch_num)+" "+str(switch_nodes-nv_switch_num)+" "+str(int(links))+" "+str(parameters['gpu_type'])
        f.write(first_line)
        f.write('\n')
        # 初始化 NV、ASW、PSW 和 DSW（数据中心交换机）交换机列表
        nv_switch = []
        asw_switch = []
        psw_switch = []
        dsw_switch = []
        # 构造第二行，包含所有交换机节点的索引
        sec_line = ""
        nnodes = nodes - switch_nodes
        for i in range(nnodes, nodes):
            sec_line = sec_line + str(i) + " "
            # 填充 NV 交换机列表
            if len(nv_switch) < nv_switch_num:
                nv_switch.append(i)
            # 填充 ASW 交换机列表
            elif len(asw_switch) < parameters['asw_switch_num']:
                asw_switch.append(i)
            # 填充 PSW 交换机列表
            elif len(psw_switch) < parameters['psw_switch_num']:
                psw_switch.append(i)
            # 填充 DSW 交换机列表
            else:
                dsw_switch.append(i)
        f.write(sec_line)
        f.write('\n')
        # 初始化索引变量
        ind_asw = 0
        curr_node = 0
        group_num = 0
        group_account = 0
        ind_nv = 0
        # 遍历每个 GPU 节点
        for i in range(parameters['gpu']):
            curr_node = curr_node + 1
            # 如果当前节点超过每个服务器的 GPU 数，则重置并更新 NV 交换机索引
            if curr_node > parameters['gpu_per_server']:
                curr_node = 1
                ind_nv = ind_nv + parameters['nv_switch_per_server']
            # 遍历每个 NV 交换机，创建 GPU 到 NV 交换机的链接
            for j in range(0, parameters['nv_switch_per_server']):
                #cnt += 1
                line = str(i)+" "+str(nv_switch[ind_nv+j])+" "+str(parameters['nvlink_bw'])+" "+str(parameters['nv_latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')
            # 创建 GPU 到 ASW 交换机的链接
            line = str(i)+" "+str(asw_switch[group_num*asw_switch_num_per_segment+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])
            f.write(line)
            f.write('\n')
            # 更新索引
            ind_asw = ind_asw + 1
            group_account = group_account + 1
            
            if ind_asw == asw_switch_num_per_segment:
                ind_asw = 0
            if group_account == (parameters['gpu_per_server'] * parameters['nics_per_aswitch']):
                group_num = group_num + 1
                group_account = 0

        # 创建 ASW 到 PSW 的链接
        for i in asw_switch: # asw - psw
                for j in psw_switch:
                    line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])
                    f.write(line)
                    f.write('\n')

def Rail_Opti_DualToR_SinglePlane(parameters):
    # 获取每个 ASW（接入交换机）连接的节点数
    nodes_per_asw = parameters['nics_per_aswitch']
    # 获取每个段中的 ASW 交换机数，这里假设每个服务器的 GPU 数量的两倍作为 ASW 的数量
    asw_switch_num_per_segment = parameters['gpu_per_server']*2
    # 计算段数，根据总 GPU 数和每个段中的节点数（nodes_per_asw * asw_switch_num_per_segment/2）
    if(parameters['gpu'] % (nodes_per_asw * asw_switch_num_per_segment/2) == 0):
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment/2))
    else:
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment/2))+1
    
    # 检查段数是否与 ASW 交换机数匹配，如果不匹配则调整 ASW 交换机数并发出警告
    if(segment_num != parameters['asw_switch_num'] / asw_switch_num_per_segment):
        warnings.warn("Error relations between total GPU Nums and total aws_switch_num.\n \
                         The correct asw_switch_num is set to "+str(segment_num * asw_switch_num_per_segment))
        parameters['asw_switch_num'] = segment_num * asw_switch_num_per_segment
    # 打印 ASW 交换机数
    print("asw_switch_num: " + str(parameters['asw_switch_num']))
    # 检查段数是否超过单个 Pod 的容量，如果超过则抛出异常
    if segment_num > int(parameters['asw_per_psw'] / (asw_switch_num_per_segment/2)):
        raise ValueError("Number of GPU exceeds the capacity of Rail_Optimized_SingleToR(One Pod)")
    # 设置 Pod 数为 1
    pod_num = 1
    # 打印 PSW（聚合交换机）交换机数
    print("psw_switch_num: " + str(parameters['psw_switch_num']))
    # 打印拓扑创建信息，包括段数和 Pod 数
    print("Creating Topology of totally " + str(segment_num) + " segment(s), totally "+ str(pod_num) + " pod(s)." )  

    # 计算 NV（网络虚拟化）交换机数，根据 GPU 数和每个服务器的 NV 交换机数
    nv_switch_num = (int)(parameters['gpu'] / parameters['gpu_per_server']) * parameters['nv_switch_per_server']
    # 计算总节点数，包括 GPU、ASW、PSW 和 NV 交换机
    nodes = (int) (parameters['gpu'] + parameters['asw_switch_num'] + parameters['psw_switch_num']+ nv_switch_num ) # 
    # 计算服务器数，根据 GPU 数和每个服务器的 GPU 数
    servers = parameters['gpu'] / parameters['gpu_per_server']
    # 计算交换机节点数，包括 PSW、ASW 和 NV 交换机
    switch_nodes = (int)(parameters['psw_switch_num'] + parameters['asw_switch_num'] + nv_switch_num) # 
    # 计算链接数，包括 PSW 到 ASW 的链接、服务器到 ASW 的链接以及服务器到 NV 交换机的链接
    links = (int)(parameters['psw_switch_num']/pod_num * parameters['asw_switch_num'] + servers * asw_switch_num_per_segment
                  + servers * parameters['nv_switch_per_server'] * parameters['gpu_per_server']) # 
    # 根据拓扑类型设置文件名
    if parameters['topology'] == 'AlibabaHPN':
        file_name = "AlibabaHPN_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_DualToR_SinglePlane_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    else:
        file_name = "Rail_Opti_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_DualToR_SinglePlane_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    # 打开文件进行写入
    with open(file_name, 'w') as f:
        # 打印文件名
        print(file_name)
        # 构造第一行，包含节点数、每个服务器的 GPU 数、NV 交换机数、其他交换机数、链接数和 GPU 类型
        first_line = str(nodes)+" "+str(parameters['gpu_per_server'])+" "+str(nv_switch_num)+" "+str(switch_nodes-nv_switch_num)+" "+str(int(links))+" "+str(parameters['gpu_type'])
        f.write(first_line)
        f.write('\n')
        # 初始化 NV、ASW 和 PSW 交换机列表
        nv_switch = []
        asw_switch_1 = []
        asw_switch_2 = []
        psw_switch = []
        dsw_switch = []
        # 构造第二行，包含所有交换机节点的索引
        sec_line = ""
        nnodes = nodes - switch_nodes
        for i in range(nnodes, nodes):
            sec_line = sec_line + str(i) + " "
            # 填充 NV 交换机列表
            if len(nv_switch) < nv_switch_num:
                nv_switch.append(i)
            # 填充第一组 ASW 交换机列表
            elif len(asw_switch_1) < parameters['asw_switch_num']/2:
                asw_switch_1.append(i)
            # 填充第二组 ASW 交换机列表
            elif len(asw_switch_2) < parameters['asw_switch_num']/2:
                asw_switch_2.append(i)
            # 填充 PSW 交换机列表
            elif len(psw_switch) < parameters['psw_switch_num']:
                psw_switch.append(i)
            # 填充 DSW 交换机列表
            else:
                dsw_switch.append(i)
        f.write(sec_line)
        f.write('\n')
        # 初始化索引变量
        ind_asw = 0
        curr_node = 0
        group_num = 0
        group_account = 0
        ind_nv = 0
        # 遍历每个 GPU 节点
        for i in range(parameters['gpu']):
            curr_node = curr_node + 1
            # 如果当前节点超过每个服务器的 GPU 数，则重置并更新 NV 交换机索引
            if curr_node > parameters['gpu_per_server']:
                curr_node = 1
                ind_nv = ind_nv + parameters['nv_switch_per_server']
            # 遍历每个 NV 交换机，创建 GPU 到 NV 交换机的链接
            for j in range(0, parameters['nv_switch_per_server']):
                #cnt += 1
                line = str(i)+" "+str(nv_switch[ind_nv+j])+" "+str(parameters['nvlink_bw'])+" "+str(parameters['nv_latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')
            # 创建 GPU 到第一组 ASW 交换机的链接
            line = str(i)+" "+str(asw_switch_1[group_num*int(asw_switch_num_per_segment/2)+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])
            f.write(line)
            f.write('\n')
            
            # 创建 GPU 到第二组 ASW 交换机的链接
            line = str(i)+" "+str(asw_switch_2[group_num*int(asw_switch_num_per_segment/2)+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])
            f.write(line)
            f.write('\n')

            # 更新索引
            ind_asw = ind_asw + 1
            group_account = group_account + 1
            
            if ind_asw == int(asw_switch_num_per_segment/2):
                ind_asw = 0
            if group_account == (parameters['gpu_per_server'] * parameters['nics_per_aswitch']):
                group_num = group_num + 1
                group_account = 0

        # 创建 ASW 到 PSW 的链接
        for i in asw_switch_1: # asw - psw
            for j in psw_switch:
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')
        for i in asw_switch_2: # asw - psw
            for j in psw_switch:
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')

def Rail_Opti_DualToR_DualPlane(parameters):
    # 获取每个 ASW（接入交换机）连接的节点数
    nodes_per_asw = parameters['nics_per_aswitch']
    # 获取每个段中的 ASW 交换机数，这里假设每个服务器的 GPU 数量的两倍作为 ASW 的数量
    asw_switch_num_per_segment = parameters['gpu_per_server']*2
    # 计算段数，根据总 GPU 数和每个段中的节点数（nodes_per_asw * asw_switch_num_per_segment/2）
    if(parameters['gpu'] % (nodes_per_asw * asw_switch_num_per_segment/2) == 0):
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment/2))
    else:
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment/2))+1
    
    # 检查段数是否与 ASW 交换机数匹配，如果不匹配则调整 ASW 交换机数并发出警告
    if(segment_num != parameters['asw_switch_num'] / asw_switch_num_per_segment):
        warnings.warn("Error relations between total GPU Nums and total aws_switch_num.\n \
                         The correct asw_switch_num is set to "+str(segment_num * asw_switch_num_per_segment))
        parameters['asw_switch_num'] = segment_num * asw_switch_num_per_segment
    # 打印 ASW 交换机数
    print("asw_switch_num: " + str(parameters['asw_switch_num']))
    # 检查段数是否超过单个 Pod 的容量，如果超过则抛出异常
    if segment_num > int(parameters['asw_per_psw'] / (asw_switch_num_per_segment/2)):
        raise ValueError("Number of GPU exceeds the capacity of Rail_Optimized_SingleToR(One Pod)")
    # 设置 Pod 数为 1
    pod_num = 1
    # 打印 PSW（聚合交换机）交换机数
    print("psw_switch_num: " + str(parameters['psw_switch_num']))
    # 打印拓扑创建信息，包括段数和 Pod 数
    print("Creating Topology of totally " + str(segment_num) + " segment(s), totally "+ str(pod_num) + " pod(s)." )  

    # 计算 NV（网络虚拟化）交换机数，根据 GPU 数和每个服务器的 NV 交换机数
    nv_switch_num = (int)(parameters['gpu'] / parameters['gpu_per_server']) * parameters['nv_switch_per_server']
    # 计算总节点数，包括 GPU、ASW、PSW 和 NV 交换机
    nodes = (int) (parameters['gpu'] + parameters['asw_switch_num'] + parameters['psw_switch_num']+ nv_switch_num ) # 
    # 计算服务器数，根据 GPU 数和每个服务器的 GPU 数
    servers = parameters['gpu'] / parameters['gpu_per_server']
    # 计算交换机节点数，包括 PSW、ASW 和 NV 交换机
    switch_nodes = (int)(parameters['psw_switch_num'] + parameters['asw_switch_num'] + nv_switch_num) # 
    # 计算链接数，包括 PSW 到 ASW 的链接、服务器到 ASW 的链接以及服务器到 NV 交换机的链接
    links = (int)(parameters['psw_switch_num']/pod_num/2 * parameters['asw_switch_num'] + servers * asw_switch_num_per_segment
                  + servers * parameters['nv_switch_per_server'] * parameters['gpu_per_server']) # 
    # 根据拓扑类型设置文件名
    if parameters['topology'] == 'AlibabaHPN':
        file_name = "AlibabaHPN_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_DualToR_DualPlane_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    else:
        file_name = "Rail_Opti_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_DualToR_DualPlane_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    # 打开文件进行写入
    with open(file_name, 'w') as f:
        # 打印文件名
        print(file_name)
        # 构造第一行，包含节点数、每个服务器的 GPU 数、NV 交换机数、其他交换机数、链接数和 GPU 类型
        first_line = str(nodes)+" "+str(parameters['gpu_per_server'])+" "+str(nv_switch_num)+" "+str(switch_nodes-nv_switch_num)+" "+str(int(links))+" "+str(parameters['gpu_type'])
        f.write(first_line)
        f.write('\n')
        # 初始化 NV、ASW 和 PSW 交换机列表
        nv_switch = []
        asw_switch_1 = []
        asw_switch_2 = []
        psw_switch_1 = []
        psw_switch_2 = []
        dsw_switch = []
        # 构造第二行，包含所有交换机节点的索引
        sec_line = ""
        nnodes = nodes - switch_nodes
        for i in range(nnodes, nodes):
            sec_line = sec_line + str(i) + " "
            # 填充 NV 交换机列表
            if len(nv_switch) < nv_switch_num:
                nv_switch.append(i)
            # 填充第一组 ASW 交换机列表
            elif len(asw_switch_1) < parameters['asw_switch_num']/2:
                asw_switch_1.append(i)
            # 填充第二组 ASW 交换机列表
            elif len(asw_switch_2) < parameters['asw_switch_num']/2:
                asw_switch_2.append(i)
            # 填充第一组 PSW 交换机列表
            elif len(psw_switch_1) < parameters['psw_switch_num']/2:
                psw_switch_1.append(i)
            # 填充第二组 PSW 交换机列表
            elif len(psw_switch_2) < parameters['psw_switch_num']/2:
                psw_switch_2.append(i)
            # 填充 DSW 交换机列表
            else:
                dsw_switch.append(i)
        f.write(sec_line)
        f.write('\n')
        # 初始化索引变量
        ind_asw = 0
        curr_node = 0
        group_num = 0
        group_account = 0
        ind_nv = 0
        # 遍历每个 GPU 节点
        for i in range(parameters['gpu']):
            curr_node = curr_node + 1
            # 如果当前节点超过每个服务器的 GPU 数，则重置并更新 NV 交换机索引
            if curr_node > parameters['gpu_per_server']:
                curr_node = 1
                ind_nv = ind_nv + parameters['nv_switch_per_server']
            # 遍历每个 NV 交换机，创建 GPU 到 NV 交换机的链接
            for j in range(0, parameters['nv_switch_per_server']):
                #cnt += 1
                line = str(i)+" "+str(nv_switch[ind_nv+j])+" "+str(parameters['nvlink_bw'])+" "+str(parameters['nv_latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')
            # 创建 GPU 到第一组 ASW 交换机的链接
            line = str(i)+" "+str(asw_switch_1[group_num*int(asw_switch_num_per_segment/2)+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])
            f.write(line)
            f.write('\n')
            
            # 创建 GPU 到第二组 ASW 交换机的链接
            line = str(i)+" "+str(asw_switch_2[group_num*int(asw_switch_num_per_segment/2)+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])
            f.write(line)
            f.write('\n')

            # 更新索引
            ind_asw = ind_asw + 1
            group_account = group_account + 1
            
            if ind_asw == int(asw_switch_num_per_segment/2):
                ind_asw = 0
            if group_account == (parameters['gpu_per_server'] * parameters['nics_per_aswitch']):
                group_num = group_num + 1
                group_account = 0

        # 创建 ASW 到 PSW 的链接
        for i in asw_switch_1: # asw - psw
            for j in psw_switch_1:
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')
        for i in asw_switch_2: # asw - psw
            for j in psw_switch_2:
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])
                f.write(line)
                f.write('\n')

def No_Rail_Opti_SingleToR(parameters):
    nodes_per_asw = parameters['nics_per_aswitch']  # 每个接入交换机（ASW）的节点数
    asw_switch_num_per_segment = 1  # 每个段的接入交换机数量
    if(parameters['gpu'] % (nodes_per_asw * asw_switch_num_per_segment) == 0):  # 判断GPU总数是否能整除每段的节点数
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment))  # 计算段数
    else:
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment))+1  # 如果不能整除，段数加1
    
    if(segment_num != parameters['asw_switch_num'] / asw_switch_num_per_segment):  # 检查段数与ASW数量是否匹配
        warnings.warn("Error relations between total GPU Nums and total aws_switch_num.\n \
                         The correct asw_switch_num is set to "+str(segment_num * asw_switch_num_per_segment))  # 警告并修正ASW数量
        parameters['asw_switch_num'] = segment_num * asw_switch_num_per_segment  # 更新ASW数量
    print("asw_switch_num: " + str(parameters['asw_switch_num']))  # 打印ASW数量
    if segment_num > int(parameters['asw_per_psw'] /  asw_switch_num_per_segment):  # 检查段数是否超过单个Pod的容量
        raise ValueError("Number of GPU exceeds the capacity of Rail_Optimized_SingleToR(One Pod)")  # 抛出异常
    pod_num = 1  # 设置Pod数量为1
    print("psw_switch_num: " + str(parameters['psw_switch_num']))  # 打印PSW数量
    print("Creating Topology of totally " + str(segment_num) + " segment(s), totally "+ str(pod_num) + " pod(s)." )  # 打印拓扑信息

    nv_switch_num = (int)(parameters['gpu'] / parameters['gpu_per_server']) * parameters['nv_switch_per_server']  # 计算NVSwitch数量
    nodes = (int) (parameters['gpu'] + parameters['asw_switch_num'] + parameters['psw_switch_num']+ nv_switch_num )  # 计算总节点数
    servers = parameters['gpu'] / parameters['gpu_per_server']  # 计算服务器数量
    switch_nodes = (int)(parameters['psw_switch_num'] + parameters['asw_switch_num'] + nv_switch_num)  # 计算交换机节点数
    links = (int)(parameters['psw_switch_num']/pod_num * parameters['asw_switch_num'] + servers * parameters['gpu_per_server']
                  + servers * parameters['nv_switch_per_server'] * parameters['gpu_per_server'])  # 计算链路数量
    if parameters['topology'] == 'DCN+':  # 根据拓扑类型生成文件名
        file_name = "DCN+SingleToR_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    else:
        file_name = "No_Rail_Opti_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_SingleToR_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    with open(file_name, 'w') as f:  # 打开文件写入拓扑信息
        print(file_name)  # 打印文件名
        first_line = str(nodes)+" "+str(parameters['gpu_per_server'])+" "+str(nv_switch_num)+" "+str(switch_nodes-nv_switch_num)+" "+str(int(links))+" "+str(parameters['gpu_type'])  # 第一行内容
        f.write(first_line)  # 写入第一行
        f.write('\n')  # 换行
        nv_switch = []  # 初始化NVSwitch列表
        asw_switch = []  # 初始化ASW列表
        psw_switch = []  # 初始化PSW列表
        dsw_switch = []  # 初始化DSW列表
        sec_line = ""  # 初始化第二行内容
        nnodes = nodes - switch_nodes  # 计算非交换机节点数
        for i in range(nnodes, nodes):  # 遍历所有节点
            sec_line = sec_line + str(i) + " "  # 添加节点编号到第二行
            if len(nv_switch) < nv_switch_num:  # 判断是否为NVSwitch
                nv_switch.append(i)  # 添加到NVSwitch列表
            elif len(asw_switch) < parameters['asw_switch_num']:  # 判断是否为ASW
                asw_switch.append(i)  # 添加到ASW列表
            elif len(psw_switch) < parameters['psw_switch_num']:  # 判断是否为PSW
                psw_switch.append(i)  # 添加到PSW列表
            else:  # 剩余为DSW
                dsw_switch.append(i)  # 添加到DSW列表
        f.write(sec_line)  # 写入第二行
        f.write('\n')  # 换行
        ind_asw = 0  # 初始化ASW索引
        curr_node = 0  # 初始化当前节点计数
        group_num = 0  # 初始化组号
        group_account = 0  # 初始化组内计数
        ind_nv = 0  # 初始化NVSwitch索引
        for i in range(parameters['gpu']):  # 遍历所有GPU
            curr_node = curr_node + 1  # 当前节点计数加1
            if curr_node > parameters['gpu_per_server']:  # 如果超过每台服务器的GPU数量
                curr_node = 1  # 重置当前节点计数
                ind_nv = ind_nv + parameters['nv_switch_per_server']  # 更新NVSwitch索引
            for j in range(0, parameters['nv_switch_per_server']):  # 遍历每个NVSwitch
                line = str(i)+" "+str(nv_switch[ind_nv+j])+" "+str(parameters['nvlink_bw'])+" "+str(parameters['nv_latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
                f.write(line)  # 写入链路信息
                f.write('\n')  # 换行
            line = str(i)+" "+str(asw_switch[group_num*asw_switch_num_per_segment+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
            f.write(line)  # 写入链路信息
            f.write('\n')  # 换行
            group_account = group_account + 1  # 组内计数加1
            
            if group_account == nodes_per_asw:  # 如果组内计数达到每段的节点数
                group_num = group_num + 1  # 组号加1
                group_account = 0  # 重置组内计数

        for i in asw_switch:  # 遍历所有ASW
            for j in psw_switch:  # 遍历所有PSW
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
                f.write(line)  # 写入链路信息
                f.write('\n')  # 换行

def No_Rail_Opti_DualToR(parameters):
    nodes_per_asw = parameters['nics_per_aswitch']  # 每个接入交换机（ASW）的节点数
    asw_switch_num_per_segment = 2  # 每个段的接入交换机数量
    if(parameters['gpu'] % (nodes_per_asw * (asw_switch_num_per_segment/2)) == 0):  # 判断GPU总数是否能整除每段的节点数
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment/2))  # 计算段数
    else:
        segment_num = (int)(parameters['gpu']/ (nodes_per_asw * asw_switch_num_per_segment/2))+1  # 如果不能整除，段数加1
    if(segment_num != parameters['asw_switch_num'] / asw_switch_num_per_segment):  # 检查段数与ASW数量是否匹配
        warnings.warn("Error relations between total GPU Nums and total aws_switch_num.\n \
                         The correct asw_switch_num is set to "+str(segment_num * asw_switch_num_per_segment))  # 警告并修正ASW数量
        parameters['asw_switch_num'] = segment_num * asw_switch_num_per_segment  # 更新ASW数量
    print("asw_switch_num: " + str(parameters['asw_switch_num']))  # 打印ASW数量
    if segment_num > int(parameters['asw_per_psw'] /  asw_switch_num_per_segment):  # 检查段数是否超过单个Pod的容量
        raise ValueError("Number of GPU exceeds the capacity of Rail_Optimized_SingleToR(One Pod)")  # 抛出异常
    pod_num = 1  # 设置Pod数量为1
    print("psw_switch_num: " + str(parameters['psw_switch_num']))  # 打印PSW数量
    print("Creating Topology of totally " + str(segment_num) + " segment(s), totally "+ str(pod_num) + " pod(s)." )  # 打印拓扑信息

    nv_switch_num = (int)(parameters['gpu'] / parameters['gpu_per_server']) * parameters['nv_switch_per_server']  # 计算NVSwitch数量
    nodes = (int) (parameters['gpu'] + parameters['asw_switch_num'] + parameters['psw_switch_num']+ nv_switch_num )  # 计算总节点数
    servers = parameters['gpu'] / parameters['gpu_per_server']  # 计算服务器数量
    switch_nodes = (int)(parameters['psw_switch_num'] + parameters['asw_switch_num'] + nv_switch_num)  # 计算交换机节点数
    links = (int)(parameters['psw_switch_num']/pod_num * parameters['asw_switch_num'] + servers * parameters['gpu_per_server']*2
                  + servers * parameters['nv_switch_per_server'] * parameters['gpu_per_server'])  # 计算链路数量
    if parameters['topology'] == 'DCN+':  # 根据拓扑类型生成文件名
        file_name = "DCN+DualToR_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    else:
        file_name = "No_Rail_Opti_"+str(parameters['gpu'])+"g_"+str(parameters['gpu_per_server'])+"gps_DualToR_"+parameters['bandwidth']+"_"+parameters['gpu_type']
    with open(file_name, 'w') as f:  # 打开文件写入拓扑信息
        print(file_name)  # 打印文件名
        first_line = str(nodes)+" "+str(parameters['gpu_per_server'])+" "+str(nv_switch_num)+" "+str(switch_nodes-nv_switch_num)+" "+str(int(links))+" "+str(parameters['gpu_type'])  # 第一行内容
        f.write(first_line)  # 写入第一行
        f.write('\n')  # 换行
        nv_switch = []  # 初始化NVSwitch列表
        asw_switch_1 = []  # 初始化ASW1列表
        asw_switch_2 = []  # 初始化ASW2列表
        psw_switch = []  # 初始化PSW列表
        dsw_switch = []  # 初始化DSW列表
        sec_line = ""  # 初始化第二行内容
        nnodes = nodes - switch_nodes  # 计算非交换机节点数
        for i in range(nnodes, nodes):  # 遍历所有节点
            sec_line = sec_line + str(i) + " "  # 添加节点编号到第二行
            if len(nv_switch) < nv_switch_num:  # 判断是否为NVSwitch
                nv_switch.append(i)  # 添加到NVSwitch列表
            elif len(asw_switch_1) < parameters['asw_switch_num']/2:  # 判断是否为ASW1
                asw_switch_1.append(i)  # 添加到ASW1列表
            elif len(asw_switch_2) < parameters['asw_switch_num']/2:  # 判断是否为ASW2
                asw_switch_2.append(i)  # 添加到ASW2列表
            elif len(psw_switch) < parameters['psw_switch_num']:  # 判断是否为PSW
                psw_switch.append(i)  # 添加到PSW列表
            else:  # 剩余为DSW
                dsw_switch.append(i)  # 添加到DSW列表
        f.write(sec_line)  # 写入第二行
        f.write('\n')  # 换行
        ind_asw = 0  # 初始化ASW索引
        curr_node = 0  # 初始化当前节点计数
        group_num = 0  # 初始化组号
        group_account = 0  # 初始化组内计数
        ind_nv = 0  # 初始化NVSwitch索引
        for i in range(parameters['gpu']):  # 遍历所有GPU
            curr_node = curr_node + 1  # 当前节点计数加1
            if curr_node > parameters['gpu_per_server']:  # 如果超过每台服务器的GPU数量
                curr_node = 1  # 重置当前节点计数
                ind_nv = ind_nv + parameters['nv_switch_per_server']  # 更新NVSwitch索引
            for j in range(0, parameters['nv_switch_per_server']):  # 遍历每个NVSwitch
                line = str(i)+" "+str(nv_switch[ind_nv+j])+" "+str(parameters['nvlink_bw'])+" "+str(parameters['nv_latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
                f.write(line)  # 写入链路信息
                f.write('\n')  # 换行
            line = str(i)+" "+str(asw_switch_1[group_num*int(asw_switch_num_per_segment/2)+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
            f.write(line)  # 写入链路信息
            f.write('\n')  # 换行

            line = str(i)+" "+str(asw_switch_2[group_num*int(asw_switch_num_per_segment/2)+ind_asw])+" "+str(parameters['bandwidth'])+" "+str(parameters['latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
            f.write(line)  # 写入链路信息
            f.write('\n')  # 换行
            group_account = group_account + 1  # 组内计数加1

            if group_account == nodes_per_asw:  # 如果组内计数达到每段的节点数
                group_num = group_num + 1  # 组号加1
                group_account = 0  # 重置组内计数

        for i in asw_switch_1:  # 遍历所有ASW1
            for j in psw_switch:  # 遍历所有PSW
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
                f.write(line)  # 写入链路信息
                f.write('\n')  # 换行
        for i in asw_switch_2:  # 遍历所有ASW2
            for j in psw_switch:  # 遍历所有PSW
                line = str(i) + " " + str(j) +" "+ str(parameters['ap_bandwidth'])+" " +str(parameters['latency'])+" "+str(parameters['error_rate'])  # 生成链路信息
                f.write(line)  # 写入链路信息
                f.write('\n')  # 换行


def main():
    parser = argparse.ArgumentParser(description='Python script for generating a topology for SimAI')  # 创建参数解析器

    # 整体结构参数
    parser.add_argument('-topo','--topology', type=str, default=None,help='Template for AlibabaHPN, Spectrum-X, DCN+')  # 拓扑模板
    parser.add_argument('--ro', action='store_true',help='use rail-optimized structure')  # 是否使用Rail-Optimized结构
    parser.add_argument('--dt',action='store_true', help='enable dual ToR, only for DCN+')  # 是否启用Dual ToR（仅限DCN+）
    parser.add_argument('--dp', action='store_true', help='enable dual_plane, only for AlibabaHPN')  # 是否启用Dual Plane（仅限AlibabaHPN）
    parser.add_argument('-g','--gpu',type=int,default=None,help='gpus num, default 32')  # GPU数量，默认32
    parser.add_argument('-er','--error_rate',type=str,default=None,help='error_rate, default 0')  # 错误率，默认0

    # 主机内参数
    parser.add_argument('-gps','--gpu_per_server',type=int,default=None,help='gpu_per_server, default 8')  # 每台服务器的GPU数量，默认8
    parser.add_argument('-gt','--gpu_type',type=str,default=None,help='gpu_type, default H100')  # GPU类型，默认H100
    parser.add_argument('-nsps','--nv_switch_per_server',type=int,default=None,help='nv_switch_per_server, default 1')  # 每台服务器的NVSwitch数量，默认1
    parser.add_argument('-nvbw','--nvlink_bw',type=str,default=None,help='nvlink_bw, default 2880Gbps')  # NVLink带宽，默认2880Gbps
    parser.add_argument('-nl','--nv_latency',type=str,default=None,help='nv switch latency, default 0.000025ms')  # NVSwitch延迟，默认0.000025ms
    parser.add_argument('-l','--latency',type=str,default=None,help='nic latency, default 0.0005ms')  # NIC延迟，默认0.0005ms

    # 段内参数
    parser.add_argument('-bw','--bandwidth',type=str,default=None,help='nic to asw bandwidth, default 400Gbps')  # NIC到ASW的带宽，默认400Gbps
    parser.add_argument('-asn','--asw_switch_num',type=int,default=None,help='asw_switch_num, default 8')  # ASW数量，默认8
    parser.add_argument('-npa','--nics_per_aswitch',type=int,default=None,help='nnics per asw, default 64')  # 每个ASW的NIC数量，默认64

    # Pod内参数
    parser.add_argument('-psn','--psw_switch_num',type=int,default=None,help='psw_switch_num, default 64')  # PSW数量，默认64
    parser.add_argument('-apbw','--ap_bandwidth',type=str,default=None,help='asw to psw bandwidth,default 400Gbps')  # ASW到PSW的带宽，默认400Gbps   
    parser.add_argument('-app','--asw_per_psw',type=int,default=None,help='asw for psw')  # 每个PSW的ASW数量
    args = parser.parse_args()  # 解析参数

    default_parameters = []  # 初始化默认参数列表
    parameters = analysis_template(args, default_parameters)  # 分析模板并生成参数
    if not parameters['rail_optimized']:  # 如果未启用Rail-Optimized结构
        if parameters['dual_plane']:  # 如果启用了Dual Plane
            raise ValueError("Sorry, None Rail-Optimized Structure doesn't support Dual Plane")  # 抛出异常
        if parameters['dual_ToR']:  # 如果启用了Dual ToR
            No_Rail_Opti_DualToR(parameters)  # 调用Dual ToR函数
        else:  # 否则
            No_Rail_Opti_SingleToR(parameters)  # 调用Single ToR函数
    else:  # 如果启用了Rail-Optimized结构
        if parameters['dual_ToR']:  # 如果启用了Dual ToR
            if parameters['dual_plane']:  # 如果启用了Dual Plane
                Rail_Opti_DualToR_DualPlane(parameters)  # 调用Dual ToR Dual Plane函数
            else:  # 否则
                Rail_Opti_DualToR_SinglePlane(parameters)  # 调用Dual ToR Single Plane函数
        else:  # 如果未启用Dual ToR
            if parameters['dual_plane']:  # 如果启用了Dual Plane
                raise ValueError("Sorry, Rail-optimized Single-ToR Structure doesn't support Dual Plane")  # 抛出异常
            Rail_Opti_SingleToR(parameters)  # 调用Single ToR函数

def analysis_template(args, default_parameters):
    # Basic default parameters  # 定义基础默认参数
    default_parameters = {'rail_optimized': True, 'dual_ToR': False, 'dual_plane': False, 'gpu': 32, 'error_rate':0,
                          'gpu_per_server': 8, 'gpu_type': 'H100', 'nv_switch_per_server': 1, 
                          'nvlink_bw': '2880Gbps','nv_latency': '0.000025ms', 'latency': '0.0005ms',
                          'bandwidth': '400Gbps', 'asw_switch_num': 8,  'nics_per_aswitch': 64,
                          'psw_switch_num': 64, 'ap_bandwidth': "400Gbps", 'asw_per_psw' : 64}  # 初始化默认参数字典
    parameters = {}  # 创建空字典用于存储最终参数
    parameters['topology'] = args.topology  # 获取拓扑类型参数
    parameters['rail_optimized'] = bool(args.ro)  # 获取是否启用Rail-Optimized结构
    parameters['dual_ToR'] = bool(args.dt)  # 获取是否启用Dual ToR
    parameters['dual_plane'] = bool(args.dp)  # 获取是否启用Dual Plane

    if parameters['topology'] == 'Spectrum-X':  # 如果拓扑类型为Spectrum-X
        default_parameters.update({
            'gpu': 4096  # 更新默认GPU数量为4096
        })
        parameters.update({
            'rail_optimized': True,  # 启用Rail-Optimized结构
            'dual_ToR': False,  # 禁用Dual ToR
            'dual_plane': False,  # 禁用Dual Plane
        })
    elif parameters['topology'] == 'AlibabaHPN':  # 如果拓扑类型为AlibabaHPN
        default_parameters.update({
            'gpu': 15360,  # 更新默认GPU数量为15360
            'bandwidth': '200Gbps',  # 更新带宽为200Gbps
            'asw_switch_num': 240,  # 更新ASW数量为240
            'nics_per_aswitch': 128,  # 更新每个ASW的NIC数量为128
            'psw_switch_num': 120,  # 更新PSW数量为120
            'asw_per_psw':240  # 更新每个PSW的ASW数量为240
        })
        parameters.update({
            'rail_optimized': True,  # 启用Rail-Optimized结构
            'dual_ToR': True,  # 启用Dual ToR
            'dual_plane': False,  # 禁用Dual Plane
        })
        if args.dp:  # 如果启用了Dual Plane
            default_parameters.update({
                'asw_per_psw':120  # 更新每个PSW的ASW数量为120
            })
            parameters.update({
                'rail_optimized': True,  # 启用Rail-Optimized结构
                'dual_ToR': True,  # 启用Dual ToR
                'dual_plane': True,  # 启用Dual Plane
            })
    elif parameters['topology'] == 'DCN+':  # 如果拓扑类型为DCN+
        default_parameters.update({
            'gpu': 512,  # 更新默认GPU数量为512
            'asw_switch_num': 8,  # 更新ASW数量为8
            'asw_per_psw':8,  # 更新每个PSW的ASW数量为8
            'psw_switch_num': 8  # 更新PSW数量为8
        })
        parameters.update({
            'rail_optimized': False,  # 禁用Rail-Optimized结构
            'dual_ToR': False,  # 禁用Dual ToR
            'dual_plane': False,  # 禁用Dual Plane
        })
        if args.dt:  # 如果启用了Dual ToR
            default_parameters.update({
                'bandwidth': '200Gbps',  # 更新带宽为200Gbps
                'nics_per_aswitch': 128,  # 更新每个ASW的NIC数量为128
            })
            parameters.update({
                'rail_optimized': False,  # 禁用Rail-Optimized结构
                'dual_ToR': True,  # 启用Dual ToR
                'dual_plane': False,  # 禁用Dual Plane
            })

    parameter_keys = [  # 定义需要处理的参数键列表
        'gpu', 'error_rate', 'gpu_per_server', 'gpu_type', 'nv_switch_per_server',
        'nvlink_bw', 'nv_latency', 'latency', 'bandwidth', 'asw_switch_num',
        'nics_per_aswitch', 'psw_switch_num', 'ap_bandwidth','asw_per_psw'
    ]
    for key in parameter_keys:  # 遍历参数键列表
        parameters[key] = getattr(args, key, None) if getattr(args, key, None) is not None else default_parameters[key]  # 如果参数未提供，则使用默认值
    # for key, value in parameters.items():  # 打印所有参数（注释掉）
    #     print(f'{key}: {value}')
    # print("==================================")  # 分隔线（注释掉）
    return parameters  # 返回最终参数字典


if __name__ =='__main__':  # 主程序入口
    main()  # 调用主函数
