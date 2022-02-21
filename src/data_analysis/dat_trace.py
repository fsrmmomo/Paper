import sys
import struct 

class dat_trace:
    def init_from_string(self, src_ip, src_port, dst_ip, dst_port, proto):
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.proto = proto
    
    def init_from_binary(self, bin_trace):
        hex_trace = struct.unpack("BBBBHBBBBHB", bin_trace)
        self.src_ip = "%d.%d.%d.%d" % (hex_trace[0], hex_trace[1], hex_trace[2], hex_trace[3])
        self.src_port = "%d" % (hex_trace[4])
        self.dst_ip = "%d.%d.%d.%d" % (hex_trace[5], hex_trace[6], hex_trace[7], hex_trace[8])
        self.dst_port = "%d" % (hex_trace[9])
        self.proto = "%d" % (hex_trace[10])
    
    def __str__(self):
        return "%s %s %s %s %s" % (self.src_ip, self.src_port, self.dst_ip, self.dst_port, self.proto)

    def to_binary(self):
        src_ip = self.src_ip.split(".")
        dst_ip = self.dst_ip.split(".")
        # print(src_ip)
        # print(dst_ip)
        # print(int(self.src_port))
        # print(int(self.dst_port))
        # print(int(self.proto))
        bin_trace = struct.pack("BBBBHBBBBHB", int(src_ip[0]), int(src_ip[1]), int(src_ip[2]), int(src_ip[3]), int(self.src_port), 
                                               int(dst_ip[0]), int(dst_ip[1]), int(dst_ip[2]), int(dst_ip[3]), int(self.dst_port), int(self.proto))
        return bin_trace

    def parse_data(self, bin_trace):
        hex_trace = struct.unpack("BBBBHBBBBHB", bin_trace)
        self.init_from_binary(hex_trace)

    def bin_src_ip(self):
        src_ip = self.src_ip.split(".")
        bin_src_ip = format(int(src_ip[3]), '02x') + format(int(src_ip[2]), '02x') + format(int(src_ip[1]), '02x') + format(int(src_ip[0]), '02x')
        return bin_src_ip
