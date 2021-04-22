## Documentation

On this page you can find detailed information about the tester class and useful functions.

### The tester class (`tester`)

The tester class is the main class in the mmct package. It performs the monte carlo simulations and does the actual testing.

#### Constructing the tester class

The tester class has a single constructor method, taking no input parameters:

---

`tester()` -- Create a new instance of the tester class

---

#### Member variables of the tester class

The following member variables of the tester class can be useful to access or modify.

---

`tester.n_samples` : `int` -- The number of random samples to make during the monte carlo simulation

`tester.statistics` : `numpy.ndarray` -- An array of the statistics computed from the monte carlo simulation

---

#### Running the simulations and performing the test

To perform the monte carlo simulations and do the test, use the `do_test` function:

---

`tester.do_test(numpy.ndarray x, numpy.ndarray p)` : `float` -- Tests the hypothesis that the array of observations `x` originates from a multinomial distribution with probabilities given in `p`. This draws `n_samples` random samples from the hypothesised distribution and calculates the test statistic for each of the samples. The sample statistics are inserted into `statistics`. The function returns the p-value which is the fraction of random samples having a poorer test statistic than the item under test.

---

## Other functions

The following functions are not directly related to the act of testing a multinomial distribution, but are still availble from the `mmct` package

---

`get_multinom(numpy.ndarray c_prob, numpy.ndarray rs)` : `numpy.ndarray` -- Generate multinomially distributed variables. `rs` should be an array with random numbers in `[0,1)`. `c_prob` is the array determining the probabilites, however it should be the cumulative sum of probabilities for each bin in the multinomial.

**Example**:
Generate a multinomial distribution with 5 observations where the probabilites for each bin are `[0.2, 0.5, 0.1, 0.2]`:
```
import mmct
import numpy as np
import random
rs = np.zeros(5)
for i in range(0,5):
  rs[i] = random.random()
c_prob = np.array([0.2, 0.7, 0.8, 1.0]) # Probabilities added cumulatively
multinom = mmct.get_multinom(c_prob, rs)
```

---

The following function computes the log-likelihood ratio test statistic that is used for comparing the item under test with the random monte carlo samples.

`stat.multinomialLLR(numpy.ndarray x, numpy.ndarray ref)` : `float` -- Compute the log-likelihood ratio test statistic for a multinomial distribution `x` of observations given a null-hypothesis reference. The reference array will be converted to a set of probabilities and scaled to the same number of observations as there are in `x` automatically.
