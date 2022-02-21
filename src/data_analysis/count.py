#!/usr/bin/python
import sys
import struct
import dat_trace
import os



def collect_statistic_data(file_name, trace_byte_size=13):
    stat = {}
    count_array = []
    with open(file_name, 'rb') as f:
        bin_trace = f.read(trace_byte_size)
        x = 0
        while bin_trace:
            x+=1
            t = dat_trace.dat_trace()
            t.init_from_binary(bin_trace)
            # print(t)
            # load to stat
            if t.bin_src_ip() not in stat:
                stat[t.bin_src_ip()] = 1
            else:
                stat[t.bin_src_ip()] = stat[t.bin_src_ip()] + 1

            if(x%1000==0):
                count_array.append(len(stat))
                stat.clear()

            bin_trace = f.read(trace_byte_size)
            if bin_trace == None:
                count_array.append(len(stat))
                stat.clear()
    print(count_array)
    # count_array.sort()
    # print(count_array)
    print(len(count_array))

    return count_array

def save_statistic_data(file_name, count_array):
    with open(file_name, 'w') as f:
        for num in count_array:
            f.write("%d\t"%(num))



if __name__ == "__main__":
    # dat_file_folder = sys.argv[1]
    dat_file_folder = "../../Data/dat/"

    cnt_file_folder = "../../Data/cnt/"
    # csv_file_folder = sys.argv[2]
    for file in os.listdir(dat_file_folder):
        # if file[-3:] == "dat":
        if file == "1.dat":
            print("Process: ", dat_file_folder + file)
            count_array = collect_statistic_data(dat_file_folder + file)

            # save_statistic_data(cnt_file_folder + file[:-4] + ".cnt", count_array)