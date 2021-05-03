def CheckMethodTime():
    n = 1000
    count = 10000
    dummy = 0.0
    st = 0.0
    sst = 0.0

    for j in range(n):
        start = time.perf_counter_ns()
        for i in range(count):
            arr = [10, 22, 14, 4, 2, 50, 75, 49, 4]
            dummy += InsertionSort.sort(arr, i)
        stop = time.perf_counter_ns()
        ns = (stop - start) / count
        st += ns
        sst += ns * ns

    mean = st/n
    sdev = math.sqrt((sst - mean*mean*n)/((n-1)))
    print("{:.1f} ns +/- {:.1f} ns".format(mean, sdev))
    return dummy