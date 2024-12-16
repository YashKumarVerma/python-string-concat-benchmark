# python-string-concat-benchmark
benchmarking python concat benchmarking

## Outcome
- Using python's `.join()` is atleast two times faster than `+` operator.


## Raw Data
- Check `./processed.json` for raw data that was gathered during benchmarks


```py
words = ["apple", "banana", "cherry"]
result = ", ".join(words)
print(result)  # Output: "apple, banana, cherry"
```


When used with a dictionary:
```py
data = {"name": "John", "age": "30", "city": "New York"}
keys = ", ".join(data.keys())
values = " | ".join(data.values())
print(keys)   # Output: "name, age, city"
print(values) # Output: "John | 30 | New York"
```


A custom function can also be passed to process each element through a filter.
```py
words = ["apple", "banana", "cherry", "date"]
filtered = [word for word in words if len(word) > 5]
result = ", ".join(filtered)
print(result)  # Output: "banana, cherry"
```


A more practical usecase can be when generating query strings
```py
params = {"search": "python", "page": "2", "sort": "asc"}
query_string = "&".join(f"{key}={value}" for key, value in params.items())
print(query_string)  # Output: "search=python&page=2&sort=asc"
```


A slightly complex implementation can be used to perform operations on nested lists as well.
```py
nested_list = [["John", "Doe"], ["Jane", "Smith"]]
result = "; ".join(" ".join(pair) for pair in nested_list)
print(result)  # Output: "John Doe; Jane Smith"

```


## Result
![benchmark results](./images/python%20benchmark.png)
