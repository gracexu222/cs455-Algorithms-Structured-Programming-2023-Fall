# cs455-Algorithms-Structured-Programming-2023-Fall
HW1:

As mentioned in class, "running times" from now on will mean "asymptotic running times" unless otherwise stated. Likewise for "memory usage".
Different homeworks may have differing number of points for convenience of grading. However every homework's points will be scaled to the same number, which is "30 divided by the total number of homeworks".
Consider this variant of linear search as done in class in which we are given an array A containing n 64-bit numbers and a 64-bit number x, and asked to find all in the indices in A such that A[i] equals x. (This paragraph applies to the first three questions below.

(3 pts) What are the worst-case and the best-case running times of this algorithm? Identify worst-case and best-case inputs (one for each)
(2 pts) What are the worst-case and the best-case memory usages of this algorithm? Identify worst-case and best-case inputs (one for each).
)(5 pts) Implement this algorithm in Python. Run it on worst-case and best-case inputs for each of running time and memory usage.
Question 4 (6 pts): Consider this problem. We are given an array Y which contains positive integers. For any two indices i, j such that i < j, define

A(i, j) = (j-i)*min(Y[i], Y[j]). The problem is to find a pair i, j where i < j for which A(i, j) is the maximum possible.

Here is an example. Y = [8, 4, 1]. A(0, 1) = (1-0)*min(8,4) = 4. A(0,2) = (2-0)*min(8.1) = 2. A(1,2) = (2-1)*min(4, 1) = 1. So the optimal answer is (i=0, j=1). 

Design a greedy algorithm to solve this problem, implement it in Python, and run it on the following two inputs. Some points will be deducted if your algorithm finds good but not optimal solutions.

Y = [10, 3, 8, 4, 19, 7, 12]

Y = [5, 9, 3, 10, 4, 7, 11]

Explain what makes this algorithm greedy. What is the worst-case running time of your algorithm as a function of n, the number of elements in Y?

HW2 Divide and Conquer and Dynamic Programming:

Consider an array A of distinct numbers in ascending order and a given threshhold T. Design a divide-and-conquer algorithm that is as asymptotically efficient as you can (in running time) to compute the number of pairs (i, j), i < j, such that (A[j] - A[i]) < T.
(3 pts) Describe the algorithm in a paragraph or two. Explain the key ideas in  it and why it finds a correct solution.
(3 pts) Analyze the running time of your algorithm on inputs in which the number of pairs in the solution is constant, i.e. does not grow with the number of elements n in A.
(3 pts) Implement it in Python and run it on A = [2, 7, 14, 22, 30, 37, 43, 50, 57, 63, 71, 78, 85, 91, 98, 105, 112, 118, 125, 133] and T = 8. 
Consider the problem of finding a longest increasing subsequence in a sequence of integers. (Remember as done in class when covering the LCS problem, a subsequence of a sequence is not necessarily a contiguous slice of the latter.)
(3 pts) Design a dynamic programming algorithm for this problem and explain it.
(3 pts) Implement it in Python and run it on the sequence [3, 2, 5, 1, 6, 3, 9,2] to output an increasing subsequence that is the longest.
Consider this slightly modified definition of edit distance. The edit distance between two strings S and T is the minimum number of insertion, deletion, substitution, or transposition operations needed to transform S to T (or vice versa). We've added a new operation which is to transpose adjacent characters. Consider CTAC and GCTCA. Their edit distance is 2 per the modified definition as AC can be transformed to CA with a single transposition operation.
(3 pts) Describe the modified dynamic programming algorithm.
(3 pts) Implement this (modified) algorithm in Python and run it on (CTAC, GCTCA) to output the edit distance as well as an actual sequence of operations that corresponds to it.

HW3 Sorting and Search :
(7 pts) Consider a generalization of a MAX-Heap in which the tree is a nearly-balanced k-ary tree. (k=2 is the (binary) MAX-Heap done in class. Now k can be 2, 3, 4, ...) As with binary max-heaps the term "nearly-balanced" means that the tree is filled except possibly in the last level, in which the leftmost values may be filled. Suppose the MAX-Heap is "linearized" into an array, just as for k=2 (see class slides).
(2 pts) Write out the formulae to compute--for a given node represented by index i in the array--its parent, and its jth child, j=1, ..., k.
(3 pts) What is the worst-case running time of MAX-Heapify(A, 1)? For this analysis, interpret k as a possibly increasing function of n, the number of elements in the heap. Explain your answer. 
(2 pts) Based on your analysis, is there any value of k, possibly a function of n, for which the worst-case time for MAX-Heapify(A, 1) is asymptotically better than the worst-case time for MAX-Heapify(A,1) when k is 2? Explain which value and why if so, and why not if not.
(8 pts) Imagine nonnegative integers arriving one by one in an input stream forever. When the next integer arrives, you need to output the number of times this integer has been seen in the stream till and including then. So when a number arrives for the first time, you should output 1, for the second time output 2 and so on. 
(3) Describe a good approach for this problem.
(2) Explain what is good about this approach. 
(3) Consider a batch version of this problem in which the numbers don't arrive in a stream but are stored in an array containing n elements. The goal in this batch version is to be able to process this array in such a way that subsequently, any number can be input and the approach outputs its frequency in the array sufficiently fast. Can you exploit the fact that now you know all the numbers upfront (even though n may be very large) to improve your approach. If so, explain in what ways your approach is an improvement.
(13 pts) Consider an array of n nonnegative integers. n can be arbitrarily large but assume that the number of distinct integers in the array cannot exceed a fixed constant K. (This does not constrain the integer values, they can be any.) We are interested in finding the number which has the highest frequency in this array.
(3 pts) Describe an approach that is good for this problem. It must work correctly.
(2 pts) Explain what is good about your approach.
(3 pts) Implement this approach in Python. You can use any packages that Python supports for the type of data structures that we have done in class. 
(5 pts) Test your implementation on a simulated array of n nonnegative integers, for sufficiently large n. Ensure that the number with the highest-frequency in your data set is unique. 
(2) Explain how you generated the synthetic data of the type we want in the array.
(3) Create one array, run your method on it to find the most frequent element, and run a much simpler method, e.g. based on Python dictionaries to find the same. Assert that both give the same results. Also time the running times of the two methods and report them.

HW4 Graph Algorithms:
(8 pts) Implement the disjoint-set-collection data structure from scratch as a class in Python.  Your implementation is not required to be the most efficient in time or in space complexity, though it should not be grossly inefficient in either. (Implementing the implementation described in class is just fine.)
The constructor method should take one argument, n, and initialize the DSC data structure to contain singleton sets, {{0}, {1}, {2}, ..., {n-1}}. 
Support the method find(i) which returns the id of the set containing the element i.
Support the method union(x, y) which assumes that x and y are in different sets and merges those two sets. 
Test this class to find the connected components of the graph on 7 nodes specified by the set of edges below: {{0, 1}, {2, 3}, {3, 5}, {4,6}}. Output the set of nodes in each connected component. (You don't need to output the edges in each connected component.)
(8 pts) Use your data structure to find the connected components in a given graph.
Implement using your DSC data structure an algorithm to find the connected components in a given graph. (In fact you can implement it in such a way that 1.4 reuses it for the basic testing.)
Implement a method that generates graphs that are suited to testing your implementation in 2.1. It takes a list of positive integers [n1, n2, ..., nk] as an argument and generates a graph with k connected components containing n1, n2, ..., nk nodes respectively. Within each connected component, make its graph fully connected, i.e. connect every pair of nodes within a component by an edge.
Use your generator in 2.2 to test your implementation in 2.1 on one graph generated from each of the configurations below: [10]*10, [100,500], [250,5, 10]. In each case automate the functional testing of your implementation in 2.1 by comparing the sets of nodes in each connected component that the generator produces (it can return this information) with the sets of nodes in each connected component that your implementation of 2.1 finds. 

