from uuid import uuid4
from json import dumps
import time

results = []

iterations = [100_000_00_0]
for iteration in iterations:
    items = []
    for i in range(iteration):
        if i % 10000000 == 0:
            print("counter = %s of %s, %s%%" % (i, iteration, (i / iteration) * 100))
        items.append(uuid4().hex)

    for counter in range(10):
        start_time = time.time()
        result = ""
        another_result = "".join(items)
        end_time = time.time()
        runtime_join = end_time - start_time
        print(
            "iteration count:%s, size:%s, join: %s seconds"
            % (counter, iteration, runtime_join)
        )

        start_time = time.time()
        result = ""
        for i in items:
            result += i
        end_time = time.time()
        runtime_plus = end_time - start_time
        print(
            "iteration count:%s, size:%s, plus: %s seconds"
            % (counter, iteration, runtime_plus)
        )

        results.append(
            {
                "iteration_count": counter,
                "iteration_size": iteration,
                "runtime_join": runtime_join,
                "runtime_plus": runtime_plus,
            }
        )

print(dumps(results))
