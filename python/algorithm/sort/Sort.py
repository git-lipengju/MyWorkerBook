import time, copy, math
from make_data import get_data, get_range_data


# stable sort
def bubble(data, is_log=True):
    data_length = len(data)
    data1 = copy.deepcopy(data)
    # 传统sort 升序
    start = time.time()
    count1 = 0
    for i1 in range(data_length - 1):
        for i2 in range(1, data_length - i1):
            # count1 += 1
            if data1[i2] < data1[i2-1]:
                tmp = data1[i2]
                data1[i2] = data1[i2-1]
                data1[i2-1] = tmp
    end = time.time()
    if is_log:
        print("bubble time is : %s" % (end - start))
        # print("bubble count is : %s " % count1)
        # print("bubble result is : %s" % data1)
    # 优化sort，添加最后一次交换位置的标记点，下次排序只需遍历到此处即可
    data2 = copy.deepcopy(data)
    start = time.time()
    exchange_index = data_length
    count2 = 0
    for i1 in range(data_length - 1):
        is_exchange = False
        for i2 in range(1, exchange_index):
            # count2 += 1
            if data2[i2] < data2[i2 - 1]:
                tmp = data2[i2]
                data2[i2] = data2[i2 - 1]
                data2[i2 - 1] = tmp
                exchange_index = i2
                is_exchange = True
        if not is_exchange or exchange_index == data_length:
            break
    end = time.time()
    if is_log:
        print("upgrade bubble time is : %s" % (end - start))
        # print("upgrade bubble count is : %s " % count2)
        # print("upgrade bubble result is : %s" % data2)
    return data1


# unstable
def selection(data, is_log=True):
    data_length = len(data)
    data1 = copy.deepcopy(data)
    start = time.time()
    count1 = 0
    for i1 in range(data_length - 1):
        for i2 in range(i1, data_length):
            # count1 += 1
            if data1[i1] > data1[i2]:
                tmp = data1[i1]
                data1[i1] = data1[i2]
                data1[i2] = tmp
    end = time.time()
    if is_log:
        print("selection time is : %s " % (end - start))
        # print("selection count is : %s" % count1)
        # print("selection result is : %s " % data1)
    return data1


# stable
def insert(data, is_log=True):
    data_length = len(data)
    data1 = copy.deepcopy(data)
    start = time.time()
    count1 = 0
    for i1 in range(1, data_length):
        for i in range(i1):
            # count1 += 1
            if data1[i1 - i] >= data1[i1 - i - 1]:
                break
            tmp = data1[i1 - i - 1]
            data1[i1 - i - 1] = data1[i1 - i]
            data1[i1 - i] = tmp
    end = time.time()
    if is_log:
        print("insert time is : %s " % (end - start))
        # print("insert count is : %s" % count1)
        # print("insert result is : %s " % data1)
    return data1


# unstable
def shell(data, is_log=True):
    data_length = len(data)
    data1 = copy.deepcopy(data)
    start = time.time()
    gap = 1
    count1 = 0
    while gap < data_length/5:
        gap = gap * 5 + 1
    while gap:  # 不同间距下的遍历
        for i1 in range(math.floor(data_length/gap)):  # 每个间距下每个分组的遍历
            for i2 in range(i1 + gap, data_length, gap):  # 每个分组进行插入排序
                i3 = i2
                while i3 >= gap and data1[i3] < data1[i3 - gap]:  # 当前元素值小于前一个，交换，并继续向前比较
                    tmp = data1[i3 - gap]
                    data1[i3 - gap] = data1[i3]
                    data1[i3] = tmp
                    i3 -= gap
                # count1 += (i2 - i3)/gap + 1
        gap = math.floor(gap/5)
    end = time.time()
    if is_log:
        print("shell time is : %s " % (end - start))
        # print("shell count is : %s" % count1)
        # print("shell result is : %s " % data1)
    return data1


# stable
def merge(data, is_log=True):
    data1 = copy.deepcopy(data)
    start = time.time()
    def recusive(rcdata):
        rcdata_length = len(rcdata)
        if rcdata_length < 2:
            return rcdata
        left_data = rcdata[:int(rcdata_length/2)]
        right_data = rcdata[int(rcdata_length/2):]
        left_length = len(left_data)
        right_length = len(right_data)
        if left_length > 1:
            left_data = recusive(left_data)
        if right_length > 1:
            right_data = recusive(right_data)
        left_index = 0
        right_index = 0
        result = []
        while left_index < left_length and right_index < right_length:
            if left_data[left_index] <= right_data[right_index]:
                result.append(left_data[left_index])
                left_index += 1
            else:
                result.append(right_data[right_index])
                right_index += 1
        if left_index < left_length:
            for i in range(left_index, left_length):
                result.append(left_data[i])
        if right_index < right_length:
            for i in range(right_index, right_length):
                result.append(right_data[i])
        return result
    data1 = recusive(data1)
    end = time.time()
    if is_log:
        print("merge time is : %s " % (end - start))
        # print("merge count is : %s" % count1)
        # print("merge result is : %s " % data1)
    return data1


# unstable
def quick(data, is_log=True):
    data1 = copy.deepcopy(data)
    start = time.time()
    def recusive(rcdata):
        data_length = len(rcdata)
        if data_length < 2:
            return rcdata
        division_point = rcdata[0]
        left_data = []
        right_data = []
        for i in range(1, data_length):
            if rcdata[i] < division_point:
                left_data.append(rcdata[i])
            else:
                right_data.append(rcdata[i])
        left_data.append(division_point)
        return recusive(left_data) + recusive(right_data)

    data1 = recusive(data1)
    end = time.time()
    if is_log:
        print("quick time is : %s " % (end - start))
        # print("quick count is : %s" % count1)
        # print("quick result is : %s " % data1)
    return data1


# stable
def counting(data, is_log=True):
    data1 = copy.deepcopy(data)
    data_length = len(data1)
    start = time.time()
    min_data = data1[0]
    max_data = data1[0]
    for i in range(1, data_length):
        if data1[i] < min_data:
            min_data = data1[i]
        if data1[i] > max_data:
            max_data = data1[i]
    tmp_list = [0] * (max_data - min_data + 1)
    for i in range(data_length):
        tmp_list[data1[i] - min_data] += 1
    result = []
    for i in range(max_data - min_data + 1):
        while tmp_list[i]:
            result.append(i + min_data)
            tmp_list[i] -= 1
    end = time.time()
    data1 = result
    if is_log:
        print("counting time is : %s " % (end - start))
        # print("counting count is : %s" % count1)
        # print("counting result is : %s " % data1)
    return data1


# stable
def bucket(data, is_log=True):
    data1 = copy.deepcopy(data)
    data_length = len(data1)
    start = time.time()
    bucket_size = 20  # 定义每个桶的大小
    min_data = data1[0]
    max_data = data1[0]
    for i in range(1, data_length):
        if data1[i] < min_data:
            min_data = data1[i]
        if data1[i] > max_data:
            max_data = data1[i]
    bucket_count = math.floor((max_data - min_data) / bucket_size) + 1  # 根据桶的大小计算桶的个数
    buckets = [[] for i in range(bucket_count)]  # 生成所有的桶
    for i in range(data_length):  # 将数据放到每个桶中
        buckets[math.floor((data1[i] - min_data) / bucket_size)].append(data1[i])
    result = []
    for i in range(bucket_count):  # 对每个桶进行排序
        if len(buckets[i]) < 1:
            continue
        buckets[i] = selection(buckets[i], is_log=False)  # 调用选择排序
        result = result + buckets[i]
    end = time.time()
    data1 = result
    if is_log:
        print("bucket time is : %s " % (end - start))
        # print("bucket count is : %s" % count1)
        # print("bucket result is : %s " % data1)
    return data1


# stable
def radix(data, is_log=True):
    data1 = copy.deepcopy(data)
    data_length = len(data1)
    start = time.time()
    max_data = max(data1)
    digits = int(math.log(max_data, 10)) + 1
    buckets = [[] for i in range(10)]
    for i in range(digits):  # 遍历每一位数
        for j in range(data_length):  #
            buckets[int(data1[j]/(10 ** i)) % 10].append(data1[j])
        data1 = []
        for k in buckets:
            data1 += k
        buckets = [[] for i in range(10)]
    end = time.time()
    if is_log:
        print("radix time is : %s " % (end - start))
        # print("radix count is : %s" % count1)
        # print("radix result is : %s " % data1)
    return data1


if __name__ == "__main__":
    data_list = get_data(10000)  # 10000
    # bubble_data = bubble(data_list)  # 13.85 14.66
    # selection_data = selection(data_list)  # 9.84
    # insert_data = insert(data_list)  # 15.69
    # shell_data = shell(data_list)  # 13.73
    # print(bubble_data == selection_data == insert_data == shell_data)
    merge_data = merge(data_list)  # 0.065 extra space
    quick_data = quick(data_list)  # 0.047
    counting_data = counting(data_list)  # 0.0135
    bucket_data = bucket(data_list)  #bubble: 0.2, selection: 0.171, insert: 0.172, shell: 0.195, merge: 0.187, quick: 0.184, counting: 0.199
    radix_data = radix(data_list)  # 0.045
    print(merge_data == quick_data == counting_data == bucket_data == radix_data)



















