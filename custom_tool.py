def copy_list(arr,idx_start,idx_end):
    result = []
    arr_len = len(arr)
    idx_start = idx_start % arr_len
    idx_end = idx_end % arr_len
    if(idx_start < idx_end):
        for i in range(idx_start,idx_end):
            result.append(arr[i])
        return result
    else:
        for i in range(idx_start,arr_len):
            result.append(arr[i])
        for i in range(0,idx_end):
            result.append(arr[i])
        return result

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    b = copy_list(a,4,4)
    print(b)