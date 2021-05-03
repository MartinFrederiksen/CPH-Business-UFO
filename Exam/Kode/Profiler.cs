public static double CheckMethodTime() {
    int n = 1000;
    int count = 10000;
    double dummy = 0.0;
    double st = 0.0, sst= 0.0;

    Stopwatch stopWatch = new Stopwatch();
    for(int j = 0; j < n; j++) {
        stopWatch.Restart();
        for(int i = 0; i < count; i++) {
            int[] arr = new int[] {10, 22, 14, 4, 2, 50, 75, 4};
            dummy += InsertionSort.sort(arr, i);
        }
        stopWatch.Stop();
        double ns = (stopWatch.Elapsed.TotalMilliseconds * 1000000) / count;
        st += ns;
        sst += ns * ns;
    }
    double mean = st/n, sdev = Math.Sqrt((sst - mean*mean*n)/(n-1));
    Console.WriteLine($"{mean.ToString("F1")} ns +/- {sdev.ToString("F1")} ns");
    return dummy;
}