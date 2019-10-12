# 排序


```C++
vector<int> sortArray1(vector<int>& nums) {
    // 方法一：冒泡排序
    // 通过相邻元素的比较和交换，使得每一趟循环都能找到未有序数组的最大值或最小值
    // 最好：O(n)，只冒泡一次数组就有序的情况。
    // 最坏：O(n2)
    // 平均：O(n2)
    for (int i = nums.size()-1; i > 0; --i)
    {
        bool mark = true;

        for (int j = 0; j < i; ++j)
            if (nums[j] > nums[j+1])
            {
                swap(nums[j], nums[j+1]);
                mark = false;
            }
        
        if(mark)  
            break;
    }
    return nums;
}

vector<int> sortArray2(vector<int>& nums) {
    // 选择排序
    // 和冒泡排序相似，区别在于选择排序是将每一个元素和它后面的每一个元素进行比较和交换，从而找到最小值
    // 最好：O(n2)
    // 最坏：O(n2)
    // 平均：O(n2)
    for(int i = 0; i < nums.size(); ++i)
        for(int j = i + 1; j < nums.size(); ++j)
            if(nums[i] > nums[j])
                swap(nums[i], nums[j]);
    return nums;
}

vector<int> sortArray3(vector<int>& nums) {
    // 插入排序
    // 以第一个元素作为有序数组，其后的元素通过在这个已有序的数组中找到合适的位置并插入
    // 最好：O(n)，原数组已经是升序的  
    // 最坏：O(n2)， 原数组已经是降序的
    // 平均：O(n2)
    for(int i = 1; i < nums.size(); ++i) {
        int temp = nums[i];
        int j = i;

        while(j >= 0 && temp < nums[j-1]) {
            nums[j] = nums[j-1];
            --j;
        }
        nums[j] = temp;
     }
    return nums;
}

int partition(vector<int> &arr, int left, int right)
{
    int pivot_position = right;
    int pivot = arr[right];
    --right;

    while(true)
    {
        while (arr[left] < pivot)
            left++;
        while (arr[right] > pivot)
            right--;

        if (left < right)
            swap(arr[left], arr[right]);
        else
            break;
    }
    swap(arr[pivot_position], arr[left]);

    return left;
}

void quicksort(vector<int> & arr, int left, int right)
{
    // 基准情形：分出的子数组长度为0 或1
    if (right - left <= 0)
        return;

    // 将数组分成两部分，并返回分隔所用的轴的索引
    int pivot_position = partition(arr, left, right);

    // 对轴左侧的部分递归调用quicksort
    quicksort(arr, left, pivot_position - 1);

    // 对轴右侧的部分递归调用quicksort
    quicksort(arr, pivot_position + 1, right);
}

void quick_sort_recursive(vector<int> &arr, int start, int end) {
    if (start >= end)
        return;
    int mid = arr[end];
    int left = start, right = end - 1;

    while (left < right)
    {
        //在整个范围内搜寻比枢纽元值小或大的元素，然后将左侧元素与右侧元素交换

        while (arr[left] < mid && left < right) //试图在左侧找到一个比枢纽元更大的元素
            left++;
        while (arr[right] >= mid && left < right) //试图在右侧找到一个比枢纽元更小的元素
            right--;
        swap(arr[left], arr[right]); //交换元素
    }

    if (arr[left] >= arr[end])
        swap(arr[left], arr[end]);
    else
        left++;

    quick_sort_recursive(arr, start, left - 1);
    quick_sort_recursive(arr, left + 1, end);
}

vector<int> sortArray(vector<int>& nums) {
    quick_sort_recursive(nums, 0, nums.size()-1);

    return nums;
}

vector<int> sortArray5(vector<int>& nums) {
    // 堆排序
    // https://blog.csdn.net/u010452388/article/details/81283998
    return nums;
}

```
