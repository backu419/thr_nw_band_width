import time, psutil, pandas as pd, seaborn as sns, matplotlib.pyplot as plt

import pandas as pd

la_rcd_bytes = psutil.net_io_counters().bytes_recv
la_snt_bytes = psutil.net_io_counters().bytes_sent
total_bytes=la_rcd_bytes+la_snt_bytes
print(la_rcd_bytes)
print(la_snt_bytes)
print(total_bytes)
print(f"{la_snt_bytes/1024/1024:.2f}MB and {la_rcd_bytes/1024/1024:.2f}MB then {total_bytes/1024/1024:.2f}MB")
io_bytes=psutil.net_io_counters(pernic=True)
io_bytes1=psutil.net_io_counters()
print(io_bytes)
print(type(io_bytes))
print((io_bytes1))
print(type(io_bytes1))
df=pd.DataFrame(io_bytes)
print(df)
# for i in io_bytes:
#     print(i)
# data=[]
#
# data.append({'Bytes_sent':io_bytes.bytes_sent,
#                 'Bytes_recv':io_bytes.bytes_recv,
#                  'Pkt_sent':io_bytes.bytes_sent,
#                  'Pkt_rcvd':io_bytes.packets_recv,
#                  'Pkt_drop_in':io_bytes.
#             )