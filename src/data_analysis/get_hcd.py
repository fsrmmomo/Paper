#!/usr/bin/python
import sys
import struct 
import dat_trace
import os

def collect_statistic_data(file_name, trace_byte_size=13):
    stat = {}
    with open(file_name, 'rb') as f:
        bin_trace = f.read(trace_byte_size)
        while bin_trace:
            t = dat_trace.dat_trace()
            t.init_from_binary(bin_trace)
            # print(t)
            # load to stat
            if t.bin_src_ip() not in stat:
                stat[t.bin_src_ip()] = 1 
            else:    
                stat[t.bin_src_ip()] = stat[t.bin_src_ip()] + 1
            bin_trace = f.read(trace_byte_size)
    return stat

def save_statistic_data(file_name, stat):
    with open(file_name, 'w') as f:
        for key in stat.keys():
            f.write("%s, %s\n"%(key, stat[key]))

if __name__ == "__main__":
    dat_file_folder = sys.argv[1]
    csv_file_folder = sys.argv[2]
    for file in os.listdir(dat_file_folder):
        if file[-3:] == "dat":
            print("Process: ", dat_file_folder + file)
            stat = collect_statistic_data(dat_file_folder + file)
            save_statistic_data(csv_file_folder + file[:-4] + ".csv", stat)
    
    # stat = collect_statistic_data(dat_file_name)
    # save_statistic_data(csv_file_name, stat) 
    # print(stat) 
    # print(file_name)
    

