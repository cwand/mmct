
# mmct
Provides functionality for performing multinomial tests using monte carlo simulation

## Background
This library contain python code that can be used to test whether a given set of observations are likely to be drawn from a multinomial distribution with a given set of parameters (probabilities for each case).
Specifically, let X = (x<sub>1</sub>,x<sub>2</sub>,...,x<sub>k</sub>), where x<sub>i</sub> is the number of times we observed outcome i. We want to test whether X is taken from a multinomial distribution with probabilities p<sub>1</sub>, p<sub>2</sub>,...,p<sub>k</sub>, where p<sub>1</sub>,+p<sub>2</sub>+...+p<sub>k</sub> = 1. As is standard we quantify the test with a p-value, i.e. the probability of, by pure randomness, to get a result that is as bad or worse than X. 

To measure what we mean by "as bad or worse" we use the log-likelihood ratio, LLR. This is explained in the contect of multinomial tests in an equivalent package for the R programming language [here](https://cran.r-project.org/web/packages/XNomial/vignettes/XNomial.html). Basically, a variable that *exactly* follows the hypothesised distribution will get a LLR of 0. Any other distribution will have an LLR smaller than 0, with more unlikely distributions getting smaller and smaller. E.g., rolling three times with a fair dice you could roll two ones and a six. That would get you an LLR of -3.47. Rolling three ones would score an LLR of -5.38.

In order to perform the test we generate a bunch of random samples from the null-hypothesis distribution, each with the same number of total observations as the item under test (N = x<sub>1</sub>+x<sub>2</sub>+...+x<sub>k</sub>). We order all of these random samples according to their log-likelihood ratio, LLR and compare with the LLR of the item under test. The p-value is simply the fraction of the random samples with an LLR smaller than that of the item under test.

The library is inspired [met](https://pypi.org/project/met/), which achieve the same objective as mmct, but does so by painstakingly enumerating every possible case for the given multinomial distribution and calculating the p-value exactly. While this is certainly preferable, it becomes very slow very quickly, so for performing many tests or tests with a large parameter space, a monte carlo approximation may be good enough. As already mentioned, mmct has also drawn inspiration from the [XNomial](https://cran.r-project.org/web/packages/XNomial/vignettes/XNomial.html) package, which performs an identical task in the R programming language.

## Usage

The package is most easlily installed via pip:

    pip install mmct

The source code is also available on GitHib and is free for use and modification: [mmct on GitHub](ttps://github.com/cwand/mmct/) 

When the package has been installed, a test can be performed following the example below, in which we test whether a set of dice rolls could have been generated from rolling two fair dice 20 times and adding the eyes:

    import mmct
    import numpy as np
    #     Eyes    2  3  4  5  6  7  8  9 10 11 12
    x = np.array([0, 0, 2, 4, 5, 2, 3, 1, 0, 1, 2])
    # Hypothsised probabilities:
    p = np.array([1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36])
    # Initialise tester:
    t = mmct.tester()
    # Set number of Monte Carlo iterations to perform
    t.n_trials = 100000
    pval = do_test(x,p)
   
   The result of the test will of course vary (unless the random simulator is seeded), but should in general result in a p-value around 0.31, i.e. we cannot reject the hypothesis that the numbers above are taken from a fair dice rolling (which they actually also are).


