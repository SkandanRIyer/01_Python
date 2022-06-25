def solve(arr, queries):
    min_array = []
    dup_arr = []
    for slice_size in queries:
        if len(arr) == slice_size:
            min_array.append(min(arr))
        else:
            dup_arr = arr.copy()
            final_query_array = []
            while len(dup_arr) > slice_size:
                final_query_array.append(dup_arr[:slice_size])
                del dup_arr[0]
            if len(dup_arr) > 0:
                final_query_array.append(dup_arr)
            max_array = []
            for item in final_query_array:
                max_array.append(max(item))
            min_array.append(min(max_array))

    return min_array


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)
    print(result)
