#!/usr/bin/python
import sys
import struct
from packet_struct import *
import os
import numpy as np


def collect_statistic_data(file_name, wf, trace_byte_size=32):
    # slot = 10000
    stat = {}
    volume = {}
    count_array = []
    with open(file_name, 'rb') as f:
        bin_trace = f.read(trace_byte_size)
        x = 0
        while bin_trace:
            x += 1
            t = packet_struct()
            t.init_from_binary(bin_trace)
            key = t.src_ip + t.src_port + t.dst_ip + t.dst_port + t.proto
            if key not in stat:
                stat[key] = 1
                volume[key] = t.length
            else:
                stat[key] = stat[key] + 1
                volume[key] += t.length
            bin_trace = f.read(trace_byte_size)
            if x % 1000000 == 0:
                print(x)

    print(len(stat))
    wf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.cnt1'
    wf = '../../Data/raw_data/MAWI/dat/SB-G-202004080800.cnt1'
    wf = '../../Data/raw_data/MAWI/dat/SB-F-202201021400.cnt1'
    s = []
    for k, v in stat.items():
        s.append(v)
    s.sort(reverse=True)
    with open(wf, 'w') as f:
        for v in s:
            f.write("%d\t" % v)

    wf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.cnt2'
    wf = '../../Data/raw_data/MAWI/dat/SB-G-202004080800.cnt2'
    wf = '../../Data/raw_data/MAWI/dat/SB-F-202201021400.cnt2'
    s = []
    for k, v in volume.items():
        s.append(v)
    s.sort(reverse=True)
    with open(wf, 'w') as f:
        for v in s:
            f.write("%d\t" % v)
    # print(count_array)
    # print(len(count_array))

    return 0


def save_statistic_data(file_name, count_array):
    with open(file_name, 'w') as f:
        for num in count_array:
            f.write("%d\t" % (num))


def sort_cnt(rf):
    # rf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.cnt2'
    rf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.cnt1'
    c_list = []
    with open(rf, 'r') as f:
        lines = f.readlines()
        for line in lines:
            c_list = [int(x) for x in line.split()]
    c_list.sort(reverse=True)
    print(c_list[:100])
    with open(rf, 'w') as f:
        for c in c_list:
            f.write("%d\t" % (c))


if __name__ == "__main__":
    # dat_file_folder = sys.argv[1]
    dat_file_folder = "../../Data/dat/"
    rf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.dat'
    rf = '../../Data/raw_data/MAWI/dat/SB-G-202004080800.dat'
    rf = '../../Data/raw_data/MAWI/dat/SB-F-202201021400.dat'

    wf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.cnt'
    wf = '../../Data/raw_data/MAWI/dat/SB-G-202004080800.cnt'

    cnt_file_folder = "../../Data/cnt/"
    collect_statistic_data(rf, wf)
    # sort_cnt('')

    # csv_file_folder = sys.argv[2]
    # slotList = [200, 500, 1000, 2000, 5000, 10000, 20000]
    # for slot in slotList:
    #     countList = []
    #     for file in os.listdir(dat_file_folder):
    #         if file[-3:] == "dat":
    #         # if file == "1.dat":
    #             print("Process: ", dat_file_folder + file)
    #             count = collect_statistic_data(dat_file_folder + file, slot)
    #             countList.append(count)
    #
    #     with open("../../Data/cnt/"+str(slot)+".res", 'w') as f:
    #         for num in countList:
    #             f.write("%d\t" % (num))

    # save_statistic_data(cnt_file_folder + file[:-4] + ".cnt", count_array)
