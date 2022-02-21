#!/usr/bin/python
import sys
import struct 
import dat_trace

def gen_data_to_file(file_name, trace_byte_size=13):
    with open(file_name, 'wb') as f:
        t = dat_trace.dat_trace()
        # t = dat_trace.dat_trace();
        t.init_from_string(src_ip="1.2.3.4", src_port=12345, dst_ip="5.6.7.8", dst_port=54321, proto=6)
        # print(t.to_binary())
        f.write(t.to_binary())

def parse_data_from_file(file_name, trace_byte_size=13):
    with open(file_name, 'rb') as f:
        bin_trace = f.read(trace_byte_size)
        while bin_trace:
            t = dat_trace.dat_trace()
            t.init_from_binary(bin_trace)
            print(t)
            bin_trace = f.read(trace_byte_size)

if __name__ == "__main__":
    file_name = sys.argv[1]
    gen_data_to_file(file_name)
    parse_data_from_file(file_name) 
    # print(file_name)


