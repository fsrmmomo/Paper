import struct

import pyshark
from packet_struct import *
import os


def pkt_parse(rf, wf):
    # fpcap = open('../../Data/raw_data/MAWI/test.pcap', 'rb')

    # rf = '../../Data/raw_data/MAWI/test.pcap'
    # wf = '../../Data/raw_data/MAWI/test.dat'
    # wf = open('../../Data/raw_data/MAWI/test.dat','wb')
    wf = open(wf, 'wb')
    packet_num = 0
    trace_byte_size = 16
    pkt_list = []
    start = -1

    with open(rf, 'rb') as f:
        print("打开了pcap")
        tmp = f.read(24)

        bin_trace = f.read(trace_byte_size)
        # print(" ".join([hex(int(i)) for i in bin_trace]))
        x = 0

        while bin_trace:
            x += 1
            # print(x)
            hex_trace = struct.unpack("IIII", bin_trace)
            GMTtime = hex_trace[0]
            MicroTime = hex_trace[1]
            caplen = hex_trace[2]
            plen = hex_trace[3]

            # data = f.read(plen)
            data = f.read(caplen)
            bin_trace = f.read(trace_byte_size)
            # print(" ".join([hex(int(i)) for i in bin_trace]))

            # print(caplen)

            ipProto = data[12:14]
            if len(data) < 38:
                continue

            if ipProto != b'\x08\x00':
                # print("   不是ipv4")
                continue
            else:
                if int(data[23]) != 6 and int(data[23]) != 17:
                    # print("不是tcpudp")
                    # print(hex(data[23]))
                    continue
                # p = packet_struct()
                packet_num += 1
                time = 0
                if start != -1:
                    time = GMTtime + MicroTime / 1000000.0 - start
                else:
                    start = GMTtime + MicroTime / 1000000.0
                savep = b''
                src_ip = data[26:30]
                dst_ip = data[30:34]
                trans_proto = data[23]
                src_port = data[34:36]
                dst_port = data[36:38]
                t = struct.pack("BId", trans_proto, plen, time)

                # print(time)

                # print(" ".join([hex(int(i)) for i in savep]))
                # print(packet_num)

                savep = struct.pack("BBBBHBBBBHBId", int(src_ip[0]), int(src_ip[1]), int(src_ip[2]), int(src_ip[3]),
                                    int(src_port[0] * 256 + src_port[1]),
                                    int(dst_ip[0]), int(dst_ip[1]), int(dst_ip[2]), int(dst_ip[3]),
                                    int(dst_port[0] * 256 + dst_port[1]),
                                    trans_proto,
                                    plen,
                                    time
                                    )

                pkt_list.append(savep)
                if len(pkt_list) > 1000000:
                    print(packet_num)
                    for pkt in pkt_list:
                        wf.write(pkt)
                    pkt_list = []
    for pkt in pkt_list:
        pass
        wf.write(pkt)
    print(packet_num)
    wf.close()


def read_dat(rf):
    # rf = '../../Data/raw_data/MAWI/test.dat'
    rf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.dat'
    trace_byte_size = 32
    x = 0
    with open(rf, 'rb') as f:
        bin_trace = f.read(trace_byte_size)

        while bin_trace:
            x += 1
            print(str(x) + '  ', end='')
            p = packet_struct()

            p.init_from_binary(bin_trace)
            print(p)
            bin_trace = f.read(trace_byte_size)
            if x > 20000:
                break


if __name__ == '__main__':
    rdir = "../../Data/raw_data/MAWI/SB-F/"
    # rdir = "../../Data/raw_data/MAWI/SB-G/"
    wdir = "../../Data/raw_data/MAWI/dat/"
    wprefix = rdir[-5:-1] + "-"
    for file in os.listdir(rdir):
        if file[-6:] == "0.pcap":
        # if file[-4:] == "pcap":
            print("processing      :" + rdir + file)
            wname = wdir + wprefix + file[:-5] + '.dat'
            print("result write to :" + wname)
            pkt_parse(rdir + file, wname)
            # read_pcap(rdir + file, wname)

    # pkt_parse()
    # read_dat('')
