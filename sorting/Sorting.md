## [Sorting Algorithms in Short](https://leetcode.com/discuss/general-discussion/754949/sorting-algorithms-in-short)

### Bubble Sort

* Time Complexity : Best → `O(n)` , Worst & Average → `O(n*n)`
* Space Complexity: `O(1)`
* Stablitiy       : Stable
* Is-In-Place     : In-Place
* When to use     : `1.` If array is of small size `2.` If array is of large size but nearly sorted
* Remark          : Easiest to Implement

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
				 
				 
				 
