import urllib.request as ur


def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per)
if __name__ == '__main__':
    print("downloader")

    url = "http://mawi.nezu.wide.ad.jp/mawi/ditl/ditl2020-G/202004080800.pcap.gz"
    url1 = "http://mawi.nezu.wide.ad.jp/mawi/samplepoint-B/20060303/200603030000.dump.gz"

    wd = "../../Data/raw_data/"
    # wd = "./raw_data/"
    wn = wd + url1[-20:]

    ur.urlretrieve(url1,wn,cbk)

    # with open(wn, 'wb') as f:
    #     pass
