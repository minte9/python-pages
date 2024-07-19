def batch_generator(data, batch_size=10):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Usage example
data = list(range(30))
for batch in batch_generator(data):
    print(batch)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]