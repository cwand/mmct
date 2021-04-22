# Welcome to the mmct documentation site

On this site you can find detailed information about using mmct and code documentation.

## Installing mmct

mmct is easily installed using pip

```text
pip install mmct
```

You can also download the source code from GitHub [here](https://github.com/cwand/mmct/).

## Quick start example

The following example shows how to use mmct. We imagine throwing two fair dice and taking the sum of the eyes. We roll the two dice twenty times and get some distribution of the number of eyes rolled. The exercise is to test whether the distribution is in accordance with a multinomial distribution as we would expect from two fair dice.

```text
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
pval = t.do_test(x,p)
```

See the [documentation]() for more information.

## Contact

If you run into problems or find a bug, you can report it using the bug-tracker in the GitHub repository or [contact the author](mailto:cvvand@gmail.com)

