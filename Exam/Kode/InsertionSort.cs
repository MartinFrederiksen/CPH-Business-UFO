public static double sort(int[] arr, int t) {
    for (int i = 1; i < arr.Length; ++i) {
        int tempVal = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > tempVal) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = tempVal;
    }
    return t;
}