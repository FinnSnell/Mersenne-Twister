# Algorithm MT19937
w, n, m, r = 32, 624, 397, 31
a = 0x9908B0DF
u, d = 11, 0xFFFFFFFF
s, b = 7, 0x9D2C5680
t, c = 15, 0xEFC60000
l = 18
f = 1812433253
upper_mask = 0x80000000  # Most significant (w-r) bits (i.e., the highest bit in a 32-bit word)
lower_mask = 0x7FFFFFFF  # Least significant r bits (i.e., the lower 31 bits in a 32-bit word)

class MT19937:
    def __init__(self, seed):
        # initialize generator from a seed
        self.MT = [0] * n
        self.index = n
        self.MT[0] = seed
        for i in range(1, n):
            self.MT[i] = f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (w - 2)) + i)

    def twist(self):
        # update state array with twisting and shit
        for i in range(n):
            x = (self.MT[i] & upper_mask) + (self.MT[(i + 1) % n] & lower_mask)  # combine both state array values
            xA = x >> 1
            if x % 2 != 0:  # If x is odd
                xA ^= a
            self.MT[i] = (self.MT[(i + m) % n] ^ xA) & 0xFFFFFFFF  # update the state and apply mask

    # view read me for explanation
    def temper(self, y):
        y ^= (y >> u) & d
        y ^= (y << s) & b
        y ^= (y << t) & c
        y ^= y >> l
        return y

    def extract_number(self):
        # extract a tempered value base on MT using twist
        if self.index >= n:
            self.twist()
            self.index = 0

        y = self.MT[self.index]
        self.index += 1

        return self.temper(y)

# run the generator
mt = MT19937(seed=5489) 

# print numbers
print([mt.extract_number() for _ in range(10)])