def minDeletions(X, i, j):

	# base condition
	if i >= j:
		return 0

	
	if X[i] == X[j]:
		return minDeletions(X, i + 1, j - 1)

	return 1 + min(minDeletions(X, i, j - 1), minDeletions(X, i + 1, j))


if __name__ == '__main__':

	X = "abcabc"
	n = len(X)

	print("The minimum number of deletions required is", minDeletions(X, 0, n - 1))
