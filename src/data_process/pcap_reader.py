import struct

import pyshark
from packet_struct import *

def pkt_parse():
    fpcap = open('../../Data/raw_data/MAWI/test.pcap','rb')

    rf = '../../Data/raw_data/MAWI/test.pcap'
    ftxt = open('../../Data/raw_data/MAWI/result.txt','w',encoding='utf-8' )

    string_data = fpcap.read()

    print(  type(string_data))

    pcap_header = {}
    pcap_header['magic_number'] = string_data[0:4]
    pcap_header['version_major'] = string_data[4:6]
    pcap_header['version_minor'] = string_data[6:8]
    pcap_header['thiszone'] = string_data[8:12]
    pcap_header['sigfigs'] = string_data[12:16]
    pcap_header['snaplen'] = string_data[16:20]
    pcap_header['linktype'] = string_data[20:24]
    #把pacp文件头信息写入result.txt
    ftxt.write("Pcap文件的包头内容如下： \n")
    for key in ['magic_number','version_major','version_minor','thiszone',
                'sigfigs','snaplen','linktype']:
        ftxt.write(key+ " : " + repr(pcap_header[key])+'\n')





    # pcap文件的数据包解析
    step = 0
    packet_num = 0
    packet_data = []
    ph = []
    # pcap_packet_header = {}
    i = 24

    trace_byte_size = 16

    with open(rf,'rb') as f:
        bin_trace = f.read(trace_byte_size)

        while bin_trace:

            hex_trace = struct.unpack("IIII", bin_trace)




    while (i < len(string_data)):
        # 数据包头各个字段
        pcap_packet_header = {}
        pcap_packet_header['GMTtime'] = string_data[i:i + 4]
        pcap_packet_header['MicroTime'] = string_data[i + 4:i + 8]
        pcap_packet_header['caplen'] = string_data[i + 8:i + 12]
        pcap_packet_header['len'] = string_data[i + 12:i + 16]
        # 求出此包的包长len
        packet_len = struct.unpack('I', pcap_packet_header['len'])[0]
        # 写入此包数据
        packet_data.append(string_data[i + 16:i + 16 + packet_len])
        i = i + packet_len + 16
        packet_num += 1
        ph.append(pcap_packet_header)
        # print(i)

    # 把pacp文件里的数据包信息写入result.txt
    for i in range(packet_num):
        # 先写每一包的包头
        ftxt.write("这是第" + str(i) + "包数据的包头和数据：" + '\n')
        for key in ['GMTtime', 'MicroTime', 'caplen', 'len']:
            # value = struct.unpack('I', pcap_packet_header[key])
            value = struct.unpack('I', ph[i][key])
            # print(value)
            # ftxt.write(key + ' : ' + repr(pcap_packet_header[key]) + '\n')
            ftxt.write(key + ' : ' + str(value[0]) + '\n')
        # 再写数据部分
        ftxt.write('此包的数据内容' + repr(packet_data[i]) + '\n')
    ftxt.write('一共有' + str(packet_num) + "包数据" + '\n')

    ftxt.close()
    fpcap.close()

def read_pcap():
    rf = '../../Data/raw_data/MAWI/test.pcap'
    wf = '../../Data/raw_data/MAWI/result.txt'

    # cap = pyshark.FileCapture(rf, only_summaries=True)
    cap = pyshark.FileCapture(rf, keep_packets=False)
    # print(cap[0])
    flag = 0
    start = -1
    x = 0
    for pkt in cap:
        # continue

        if pkt.transport_layer== 'TCP' or pkt.transport_layer== "UDP":
            x+=1
            # print(pkt)
            # print(pkt.transport_layer)
            # print(pkt.sniff_timestamp)
            # print(type(pkt.sniff_timestamp))
            #
            # print(pkt.ip.src)
            # print(str(pkt.ip.src))
            # print(pkt.ip.dst)
            # # pkt.ip.
            # print(pkt[pkt.transport_layer].srcport)
            # print(int(pkt[pkt.transport_layer].srcport))
            # print(pkt[pkt.transport_layer].dstport)
            # print(pkt.length)
            # print(pkt.captured_length)
            src_ip = str(pkt.ip.src)
            dst_ip = str(pkt.ip.dst)
            # print(pkt.sniff_time)

            src_port = int(pkt[pkt.transport_layer].srcport)
            dst_port = int(pkt[pkt.transport_layer].dstport)
            proto = 6 if pkt.transport_layer== 'TCP' else 17
            p = packet_struct()
            second , microSecond = pkt.sniff_timestamp.split(".")
            second = int(second)
            microSecond = int(microSecond)//1000

            now_t = float(pkt.sniff_timestamp)
            time = 0
            if start != -1:
                time = now_t - start
            else:
                start = now_t

            p.init_from_pacp(src_ip, src_port, dst_ip, dst_port, proto, second, microSecond, time)
            print(p)

    print(x)

if __name__ == '__main__':
    read_pcap()