#!/usr/bin/env python3
"""LSD Radix Sort — O(n*k) linear time."""
import random, time

def radix_sort(arr):
    if not arr: return arr
    neg = [x for x in arr if x < 0]
    pos = [x for x in arr if x >= 0]
    def _radix(a):
        if not a: return a
        max_val = max(a)
        exp = 1
        while max_val // exp > 0:
            buckets = [[] for _ in range(10)]
            for x in a: buckets[(x // exp) % 10].append(x)
            a = [x for b in buckets for x in b]
            exp *= 10
        return a
    return _radix([-x for x in neg])[::-1] + _radix(pos)

if __name__ == "__main__":
    N = 100000
    data = [random.randint(-N, N) for _ in range(N)]
    t0 = time.time(); r1 = radix_sort(data[:]); t1 = time.time()-t0
    t0 = time.time(); r2 = sorted(data); t2 = time.time()-t0
    print(f"Radix Sort (N={N:,})")
    print(f"  Radix: {t1:.3f}s | Builtin: {t2:.3f}s | Match: {r1==r2}")\n