def most_frequent(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    # Find the number with the highest frequency
    return max(freq_dict, key=freq_dict.get)
