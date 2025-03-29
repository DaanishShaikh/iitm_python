import random  # Importing the built-in random module for generating random numbers

# Seeding the random number generator to ensure reproducibility
# The same seed value will produce the same sequence of random numbers
random.seed(42) 

# Generating a random floating-point number between 0.0 and 1.0
print("random.random():", random.random())  # Example output: 0.6394267984578837

# Generating a random floating-point number between 1 and 10 (inclusive of both ends)
print("random.uniform(1, 10):", random.uniform(1, 10))  # Example output: 1.0253449218110241

# Generating a random integer between 1 and 10 (both inclusive)
print("random.randint(1, 10):", random.randint(1, 10))  # Example output: 2

# Generating a random number from a range (start=1, stop=10, step=2)
# Will return only odd numbers in this case (e.g., 1, 3, 5, 7, 9)
print("random.randrange(1, 10, 2):", random.randrange(1, 10, 2))  # Example output: 1

# Generating a random number from an exponential distribution with lambda=1.5
print("random.expovariate(1.5):", random.expovariate(1.5))  # Example output: 0.05198124573220175

# Generating a random number from a Gaussian (normal) distribution with mean=0 and std deviation=1
print("random.gauss(0, 1):", random.gauss(0, 1))  # Example output: 0.2566636477931025

# Generating a random number from a Beta distribution with alpha=2 and beta=5
print("random.betavariate(2, 5):", random.betavariate(2, 5))  # Example output: 0.33297086599039466

# Generating a random number from a Gamma distribution with shape=2 and scale=5
print("random.gammavariate(2, 5):", random.gammavariate(2, 5))  # Example output: 14.166994472080957

# Generating a random number from a Log-normal distribution with mean=0 and standard deviation=1
print("random.lognormvariate(0, 1):", random.lognormvariate(0, 1))  # Example output: 0.5866293875597789

# Generating a random number from a Normal distribution with mean=0 and standard deviation=1
print("random.normalvariate(0, 1):", random.normalvariate(0, 1))  # Example output: -0.5227681427695596

# Generating a random number from a Triangular distribution with lower=1, upper=10, and mode=5
print("random.triangular(1, 10, 5):", random.triangular(1, 10, 5))  # Example output: 4.775467447414219

# Creating a sample list for random selection and shuffling
sample_list = [1, 2, 3, 4, 5]

# Selecting a random element from the list
print("random.choice(sample_list):", random.choice(sample_list))  # Example output: 4

# Selecting 3 random elements from the list (with replacement, meaning duplicates are possible)
print("random.choices(sample_list, k=3):", random.choices(sample_list, k=3))  # Example output: [2, 4, 3]

# Selecting 3 unique random elements from the list (without replacement)
print("random.sample(sample_list, k=3):", random.sample(sample_list, k=3))  # Example output: [1, 5, 3]

# Shuffling the list randomly (modifies the original list)
random.shuffle(sample_list)
print("random.shuffle(sample_list):", sample_list)  # Example output: [5, 1, 4, 3, 2]

# Generating an 8-bit random integer (a value between 0 and 255)
print("random.getrandbits(8):", random.getrandbits(8))  # Example output: 177

# Randomly selecting a boolean value (True or False)
print("random.choice([True, False]):", random.choice([True, False]))  # Example output: False

# Generating 5 random bytes
print("random.randbytes(5):", random.randbytes(5))  # Example output: b'\xa1\x1b\xe7\x94P'
