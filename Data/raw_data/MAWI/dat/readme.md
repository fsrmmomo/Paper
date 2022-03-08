
存储内容  32字节
```python
savep = struct.pack("BBBBHBBBBHBId", int(src_ip[0]), int(src_ip[1]), int(src_ip[2]), int(src_ip[3]),
                    int(src_port[0] * 256 + src_port[1]),
                    int(dst_ip[0]), int(dst_ip[1]), int(dst_ip[2]), int(dst_ip[3]),
                    int(dst_port[0] * 256 + dst_port[1]),
                    trans_proto,
                    plen,
                    time
                    )
```
