#!/usr/bin/python
import sys
import struct 
import os

def read_results(csv_file):
    data = {}
    # read files
    with open(csv_file, 'r') as f:
        trace = f.readline()
        while trace:
            t = trace.split(',')
            ip = t[0]
            size = t[1]
            data[ip] = int(size)
            trace = f.readline()
    return data

def compare_results(result_file, ground_truth_file, threshold):
    measured = read_results(result_file)
    ground_truth = read_results(ground_truth_file)
    ARE = 0.0
    cnt = len(ground_truth.keys()) 
    for flow in ground_truth.keys():
        g = ground_truth[flow]
        m = measured.get(flow, 0.0)
        # print(g, m)
        if(m > 0):
            ARE += (abs(g-m) / g)
    ARE = ARE / cnt
    return ARE

if __name__ == "__main__":
    result_file       = sys.argv[1]
    ground_truth_file = sys.argv[2]
    threshold         = int(sys.argv[3])
    print("Process: %s, %s " % (result_file, ground_truth_file))
    ARE = compare_results(result_file, ground_truth_file， threshold)
    print("HDD ARE, %f" % ARE)
    # stat = collect_statistic_data(dat_file_folder + file)
    # save_statistic_data(csv_file_folder + file[:-4] + ".csv", stat)
    
    # stat = collect_statistic_data(dat_file_name)
    # save_statistic_data(csv_file_name, stat) 
    # print(stat) 
    # print(file_name)
    

