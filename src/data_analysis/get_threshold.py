#!/usr/bin/python
import sys
import struct 
import dat_trace
import os
import heapq

SIM_STEP = (128 * 128 * 64)
TCAM_SIZE = 1024
MEASURE_GOAL = 0.8

def process_traces(trace_file_name, csv_file_folder, trace_byte_size=13):
    packet_count = 0
    epoch = 0
    stat = {}
    with open(trace_file_name, 'rb') as f:
        bin_trace = f.read(trace_byte_size)
        while bin_trace:
            # create new trace 
            t = dat_trace.dat_trace()
            t.init_from_binary(bin_trace)
            # print(t)
            # load to stat
            if t.bin_src_ip() not in stat:
                stat[t.bin_src_ip()] = 1 
            else:    
                stat[t.bin_src_ip()] = stat[t.bin_src_ip()] + 1
            packet_count += 1
            
            # analysis stats
            if(packet_count == SIM_STEP): 
                top_stat, measure, min_size = get_top_traces(stat)
                print("%d, %d, %d, %f, %d" % (epoch, measure, SIM_STEP, (measure / SIM_STEP), min_size ))
                csv_file_name = "%s%d.csv" % (csv_file_folder, epoch)
                # print(csv_file_name)
                save_statistic_data(csv_file_name, top_stat)
                # next epoch
                epoch += 1
                stat = {}
                packet_count = 0
            # read next
            bin_trace = f.read(trace_byte_size)

def get_top_traces(stat):
    # k_keys_sorted_by_values = heapq.nlargest(k, dictionary, key=dictionary.get)
    # print(stat)
    top_stat_keys = heapq.nlargest(TCAM_SIZE, stat, key=stat.get)
    # print(top_stat_keys)
    measure = 0
    top_stat = {}
    min_size = sys.maxsize 
    for k in top_stat_keys:
      if(stat[k] < min_size):
        min_size = stat[k]
      measure += stat[k]
      top_stat[k] = stat[k]    
    # for v in top_stat.values():
    #     measure += v
    return top_stat, measure, min_size

def save_statistic_data(file_name, top_stat):
    with open(file_name, 'w') as f:
        for key in top_stat.keys():
            f.write("%s, %d\n" % (key, top_stat[key]))

if __name__ == "__main__":
    dat_file = sys.argv[1]
    csv_file_folder = sys.argv[2]
    process_traces(dat_file, csv_file_folder)
    # stat = process_trace(traces)
    # save_statistic_data(csv_file, stat)
    
    # stat = collect_statistic_data(dat_file_name)
    # save_statistic_data(csv_file_name, stat) 
    # print(stat) 
    # print(file_name)
    

