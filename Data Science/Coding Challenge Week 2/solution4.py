def evenly_distribute(packets, m, get_packets=False):
    # sort the packets
    packets.sort()
    # minimum difference = packets[i: i+m] for min(packets[i + m - 1] - packets[i])
    i = 0
    diff = packets[i + m - 1] - packets[i] # diff for first m packets.sort()
    start = i
    while i < len(packets) - m:
        i += 1
        if diff > packets[i + m - 1] - packets[i]:
            diff = packets[i + m - 1] - packets[i]
            start = i
    if get_packets:
        return diff, packets[start : start + m]
    else:
        return diff

print(evenly_distribute([7, 3, 2, 4, 9, 12, 56], 3))
print(evenly_distribute([3, 4, 1, 9, 56, 7, 9, 12], 5, True))