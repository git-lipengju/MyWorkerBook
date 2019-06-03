import time, copy, math
from make_data import get_data, get_range_data


# stable sort
def bubble(data):
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
    print("upgrade bubble time is : %s" % (end - start))
    # print("upgrade bubble count is : %s " % count2)
    # print("upgrade bubble result is : %s" % data2)
    return data1


# unstable
def selection(data):
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
    print("selection time is : %s " % (end - start))
    # print("selection count is : %s" % count1)
    # print("selection result is : %s " % data1)
    return data1


# stable
def insert(data):
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
    print("insert time is : %s " % (end - start))
    # print("insert count is : %s" % count1)
    # print("insert result is : %s " % data1)
    return data1


# unstable
def shell(data):
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
    print("shell time is : %s " % (end - start))
    # print("shell count is : %s" % count1)
    # print("shell result is : %s " % data1)
    return data1


def merge(data):
    data_length = len(data)
    data1 = copy.deepcopy(data)
    start = time.time()


    end = time.time()
    print("merge time is : %s " % (end - start))
    # print("merge count is : %s" % count1)
    # print("merge result is : %s " % data1)
    return data1


if __name__ == "__main__":
    data_list = get_data(1000)
    bubble_data = bubble(data_list)
    selection_data = selection(data_list)
    insert_data = insert(data_list)
    shell_data = shell(data_list)
    merge_data = merge(data_list)
    print(bubble_data == selection_data == insert_data == shell_data == merge_data)


