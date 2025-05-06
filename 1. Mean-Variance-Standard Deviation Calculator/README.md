# [Mean-Variance-Standard Deviation Calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

You will be [working on this project with our Gitpod starter code](https://gitpod.io/?autostart=true#https://github.com/freeCodeCamp/boilerplate-mean-variance-standard-deviation-calculator/).

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

* [Python for Everybody Video Course](https://www.freecodecamp.org/news/python-for-everybody/) (14 hours)
* [How to Analyze Data with Python Pandas](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/) (10 hours)

Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix. 

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

If a list containing less than 9 elements is passed into the function, it should raise a `ValueError` exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, `calculate([0,1,2,3,4,5,6,7,8])` should return:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Development
Write your code in `mean_var_std.py`. For development, you can use `main.py` to test your code. In order to run your code, type `python3 main.py` into the GitPod terminal and hit enter. This will cause the included CPython interpreter to run the `main.py` file.

## Testing
The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience.

## Submitting
Copy your project's URL and submit it to freeCodeCamp.

# Code
```python
import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(list).reshape((3, 3))
        calculations = {
            'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
            'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
            'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
            'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
            'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
            'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
            }
        return calculations
```

## Test Result Screenshot
![Test result screenshot](https://github.com/user-attachments/assets/c28d18c3-f962-4185-874c-ebe96b69ec59)
