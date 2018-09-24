"""
Topic -- String alignment using minimum edit distance 
Video -- https://www.youtube.com/watch?v=DiAtV7SneRE
Source_github -- https://github.com/llSourcell/dynamic_programming

Summary
-------
This script will calculate the minimum edit distance between any two given strings. This would mean, the minimum number of operations
- edit, delete or add - one would require to convert a string A to string B. 
Example: Converting string A = "abcd" to string B ="befd" would require 3 operations: delete 'a', add 'e' and edit 'c' to 'f'. 
This problem can very be solved dynamically because it has an optimal substructure and overlaping subproblems.

Consider C to be a matrix onto which the cost of performing the operations - edit, delete or add - are mapped on. The columns of the 
matrix is named with letters in string A, and the row of the matrix is named with letter in string B.
The optimal substructure is then given by:
		   __		
		  |	C[i-1,j-1]				if A[j] = B[i]
		  |		  __
A[i,j] =  |		 |C[i-1,j] + 1
		  |	min -|C[i,j-1] + 1		if A[j] != B[i]
		  |		 |C[i-1,j-1] + 1
		   ____	  --
"""
import numpy as np

def main(string_A, string_B):

	A = string_A
	B = string_B
	C = np.zeros((len(B),len(A)))

	for i in range(len(B)):
		for j in range(len(A)):

			if A[j] == B[i]: C[i,j] = C[i-1, j-1]
			elif A[j] != B[i]: C[i,j] = min(C[i-1, j],C[i, j-1],C[i-1, j-1]) + 1

	print("The minimum edit distance is %2.1f" % (C[-1,-1]))


if __name__ == '__main__':

	string_A = "abcdef"
	string_B = "acfz"
	main(string_A, string_B)





