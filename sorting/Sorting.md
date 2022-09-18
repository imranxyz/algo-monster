![Sorting](https://assets.leetcode.com/users/images/d77e0a7c-ebcd-465a-b0e5-0c9c60f8f2ed_1627063716.2876947.png)

## [Sorting Algorithms in Short](https://leetcode.com/discuss/general-discussion/754949/sorting-algorithms-in-short)

### Bubble Sort

* Time Complexity : Best → `O(n)` , Worst & Average → `O(n*n)`
* Space Complexity: `O(1)`
* Stablitiy       : Stable
* Is-In-Place     : In-Place
* When to use     : `1.` If array is of small size `2.` If array is of large size but nearly sorted
* Remark          : Easiest to Implement

![](https://assets.leetcode.com/users/images/d9e92ea5-1374-47ea-a18b-3056c14f3670_1627064875.6981823.gif)

#### Algo

**First Iteration (Compare and Swap)**

* Starting from the first index, compare the first and the second elements.
* If the first element is greater than the second element, they are swapped.
* Now, compare the second and the third elements. Swap them if they are not in order.
* The above process goes on until the last element.

**For Remaining Iteration**

* The same process goes on for the remaining iterations.
* After each iteration, the largest element among the unsorted elements is placed at the end.

**Key Point**

* After the `nth` pass, the `nth` largest element will be at `nth` last position in the array, where `n` is the size of the array.
* This sorting algo can be used to check if an array is sorted or not efficiently in `O(N)` time

```py
....
```

### Selection Sort

* Time Complexity : Best & Worst & Average → `O(n*n)`
* Space Complexity: `O(1)` 
* Stablitiy       : Not-Stable
* Is-In-Place     : In-Place
* When to use     : `1.` If array is of small size `2.` To minimise the number of swaps
* Remarks         : *Bubble sort* has more number of swaps as compare to *selection Sort* but *bubble sort* has better best time complexity. It can also be implemented as **stabaly**. Selection sort makes `O(n)` swaps which is minimum among all sorting algorithms mentioned above.	

### Insertion Sort

* Time Complexity : Best → `O(n)` , Worst & Average → `O(n*n)`
* Space Complexity: `O(1)` 
* Stablitiy       : Stable
* Is-In-Place     : In-Place
* When to use     : `1.` If array is of small size and nearly sorted
* Remark          : Standard Libraray of `C` uses this algo when `n` becomes smaller than a threshold and for small size it is better than merge and quick sort becasue of low constant values and non recusive in nature.
				 
				 
				 
