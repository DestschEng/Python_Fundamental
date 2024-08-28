from typing import List, Generator

def wrangle(numbs: List[int]) -> Generator[int, None, None]:
    for n in numbs:
        num_power = n ** 2
        yield num_power

result = wrangle(numbers := [1, 2, 3, 4])

for num in result:
    print(num)
