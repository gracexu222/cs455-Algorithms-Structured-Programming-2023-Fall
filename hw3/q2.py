import random
import time
from collections import Counter

def most_frequent(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    # Find the number with the highest frequency
    return max(freq_dict, key=freq_dict.get)
# Generating synthetic data
n = 10**6
K = 10
data = [random.randint(0, K-1) for _ in range(n)]

# Ensuring one unique maximum frequency
data.extend([K] * (n//2))
data = random.sample(data, len(data))  # Shuffle the data

# Test and time our method
start_time = time.time()
result1 = most_frequent(data)
end_time = time.time()
print(f"Using dictionary approach: {result1}. Time taken: {end_time - start_time:.4f} seconds.")

# Test and time Counter method
start_time = time.time()
counter = Counter(data)
result2 = counter.most_common(1)[0][0]
end_time = time.time()
print(f"Using Counter approach: {result2}. Time taken: {end_time - start_time:.4f} seconds.")

# Assert both methods give the same result
assert result1 == result2, "The two methods gave different results!"
