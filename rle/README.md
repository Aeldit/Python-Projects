# RLE Python

This python program implements 2 functions, `compress()` and `decompress()` both using the RLE method. They work with the bases 8, 10 and 16

The compress function accepts any string, but the decompress functions requires a string in this form :

```python
# Here we use the base 16
my_string = "Fr4H9gAA"
decompress(my_string, 16) # -> This will return "rrrrrrrrrrrrrrrrHHHHgggggggggAAAAAAAAAA"
```

These functions have been tested with [cProfile](https://docs.python.org/3/library/profile.html) and both have an execution time inferior to 0.1 second with a long text like `Alice in wonderland`
