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

`tester.n_samples` : `int` -- The number of random samples to make during the monte carlo simulation. Default is 1000.

`tester.test_statistics` : `string` -- The test statistic to use when comparing the item under test with the monte carlo samples. Valid choices are `LLR` (log-likelihood ratio) (default) or `Prob` (probability).
When using `Prob` the test statistic is simply the probability of the given distribution occuring under the null-hypothesis. When using `LLR` the test statistic is the natural logarithm of a likelihood ratio. The ratio is taken between the probability of each event occuring under the null-hypothesis and the probability of the event occuring under the best alternative probability distribution, which is simply the observed frequency. Equations and detailed explanations for both of these can be found in the documentation of the [XNomial pacakge](https://cran.r-project.org/web/packages/XNomial/vignettes/XNomial.html) for the R programming language.

`tester.statistics` : `numpy.ndarray` -- An array of the statistics computed from the monte carlo simulation

---

#### Running the simulations and performing the test

To perform the monte carlo simulations and do the test, use the `do_test` function:

---

`tester.do_test(numpy.ndarray x, numpy.ndarray p)` : `float` -- Tests the hypothesis that the array of observations `x` originates from a multinomial distribution with probabilities given in `p`. This draws `n_samples` random samples from the hypothesised distribution and calculates the test statistic for each of the samples. The sample statistics are inserted into `statistics`. The function returns the p-value which is the fraction of random samples having a poorer test statistic than the item under test.

---

### Using multiple threads (`mt_tester`)

Since most computers have multiple processors, the monte carlo sampling
can typically be sped up by running the sampling process in multiple threads.
mmct supports this feature with the `mt_tester` class, which is a derived class
from the `tester` class, with the only difference being the parallilsation of
the sampling process.

#### Constructing the multithreaded tester

Just like its parent class, `mt_tester` has a single constructor with no
parameters:

---

`mt_tester()` -- Create a new instance of the multithreaded tester class

---

#### Member variables of the multithreaded tester class

The multithreaded tester class inherits the member variables of `tester`, and
additionally has one member variable:

---

`mt_tester.threads` : `int` -- The number of threads to use. Defaults to `None`,
in which case the system uses the default amount (usually the number of logical
processors)

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

`stat.multinomialLLR(numpy.ndarray x, numpy.ndarray ref)` : `float` -- Compute the log-likelihood ratio test statistic for a multinomial distribution `x` of observations given a null-hypothesis reference. The reference array must be a set of probabilities (adding to unity) in order for the function to compute a meaningful result.

mmct uses `scipy.stat.multinomial` to compute the multinomial probability function in case the user has set `tester.test_statistic = 'Prob'`.
