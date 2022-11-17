import psutil

network_stats = psutil.net_io_counters(pernic = True)
byte_sent = getattr(network_stats,'bytes_sent')
byte_recv = getattr(network_stats,'bytes_recv')

print("Bytes Sent = {0} | Bytes Received = {1}".format(bytes_sent,bytes_recv))
