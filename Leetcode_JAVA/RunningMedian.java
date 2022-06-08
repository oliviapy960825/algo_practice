/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
*/
public class Solution{

	public int binarySearch(int[] arr, int num, int low, int high){
		while(low + 1 < high){
			int mid = low + (high - low) / 2;
			if(arr[mid] == num)
				return mid;
			else if(arr[mid] < num)
				low = mid;
			else
				high = mid;
		}
	}

	public void runningMedian(int[] arr, int n){
		int i, j, pos, num;
		int count = 1;
		for(int i = 1; i < n; i++){
			float median;
			j = i - 1;
			num = arr[i];
			pos = binarySearch(arr, num, 0, j);
			while(j >= pos){
				arr[j + 1] = arr[j];
				j--;
			}
			arr[j + 1] = num;
			count++;

			if(count % 2 != 0){
				median = arr[count / 2];
			}
			else{
				median = (arr[count / 2 - 1] + arr[count / 2]) / 2;
			}

			System.out.println("Running Median is " + median);
		}
	}
}