"""HW7 Question 2

For this question, you will write tests for a function that already exists in Numpy: 
`numpy.random.normal`
Its documentation: https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html

This function generates random numbers, given a client-specified mean and standard deviation.
Since it's random, we can't test for exact numbers, so your tests should check that the mean 
and variance of the generated data are approximately equal to the specified mean and variance. 
You only need to write tests for the case where the mean (`loc`) and standard deviation (`scale`) 
are each a single number. (I.e., you'll notice that the documentation says that `loc` and `scale` 
can also be "array-like", but you only need to test the single number case.)

Your tests should use statistical analysis to verify this:

- The mean is approximately equal to the specified mean if it lies within four standard errors 
of the specified mean. Here, "standard error" refers to the standard deviation of the "sampling 
distribution of the mean": it's what we would expect to be the standard deviation of a list of 
numbers, where each number in the list is the mean of a list of randomly generated numbers.
To calculate the standard error, we take the population standard deviation (which the client 
passed as an argument), and divide it by the square root of the sample size (the number of 
elements that the client asked to generate). For example, if the client asked for 100 numbers, 
with a standard deviation of 5, the standard error would be 5 / sqrt(100), which is 0.5. So, if 
the mean of the generated numbers is within 4 times 0.5 (2.0) of the specified mean, we'll 
consider it approximately equal, and pass the test for whether the function is generating numbers
with the specified mean.

- Similarly, we'll consider the standard deviation of the generated numbers to be approximately 
equal to the specified standard deviation if it lies within four standard errors of the 
client-specified standard deviation. For standard deviation, the standard error is: the 
client-specified standard deviation, divided by the square root of 2 * (n-1), where n is the 
sample size (the number of elements that the client asked us to generate). For example, if the 
client asked for 100 numbers with a standard deviation of 5, the standard error would be 
5 / sqrt(2 * (100 - 1)), which is 0.355. So, if the standard deviation of the generated numbers 
is within 4 times 0.355 (1.42) of the specified standard deviation, we'll consider it 
approximately equal, and pass the test for whether the function is generating numbers with the 
specified standard deviation.

- You should also test that the correct number of elements were generated.

For more information on these statistical concepts, you can read:
- https://en.wikipedia.org/wiki/Standard_error
- https://statisticsfundamentals.com/sampling-distributions/standard-error/
- https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/
what-is-the-standard-error-of-a-sample/
- The output of a reliable AI when prompted with "How can I use standard error to determine 
whether a sample came from a Normal distribution with a specified mean and variance? Please 
explain it without relying on conceptual background on statistical distributions or tests"
- Tl;dr: If we were to randomly generate n number of elements over and over, and store only the
mean of each generated sample, we would get a bunch of numbers that are very close to the 
specified mean, but not exactly the mean. To determine whether the generated sample's mean could
possibly belong in this list of means, we check whether it is within four standard errors of the 
specified mean.

There is no code in the `src` directory for this question; you only need to write tests.
"""
