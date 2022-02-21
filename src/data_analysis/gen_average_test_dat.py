#!/usr/bin/python
import sys
import struct 
import dat_trace
import random

num_trace = 128 * 128 * 128

random.seed(0)

def gen_data_to_file(file_name, trace_byte_size=13):
    with open(file_name, 'wb') as f:
        for i in range(0, num_trace):
            addr1 = random.randint(0, 255)
            addr2 = random.randint(0, 255)
            t = dat_trace.dat_trace()
            ip = "1.2.%d.%d" % (addr1, addr2)
            t.init_from_string(src_ip=ip, src_port=12345, dst_ip="5.6.7.8", dst_port=54321, proto=6)
            f.write(t.to_binary())

def parse_data_from_file(file_name, trace_byte_size=13):
    with open(file_name, 'rb') as f:
        bin_trace = f.read(trace_byte_size)
        while bin_trace:
            t = dat_trace.dat_trace()
            t.init_from_binary(bin_trace)
            # print(t)
            bin_trace = f.read(trace_byte_size)

if __name__ == "__main__":
    file_name = sys.argv[1]
    gen_data_to_file(file_name)
    parse_data_from_file(file_name) 
    # print(file_name)


