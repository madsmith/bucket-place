#!/usr/bin/env python

gMaxBuckets = 3
gMaxNumbers = 13
gBuckets = {}

gDebug = False

def dprint(msg):
    global gDebug
    if gDebug:
        print msg

def initBuckets():
    global gBuckets
    global gMaxBuckets

    for b in range(1, gMaxBuckets+1):
        gBuckets[b] = {}

def canPlaceIn(b, n):
    global gBuckets
    dprint("? can place %d in %d" % (n, b))
    for v in gBuckets[b].keys():
        difference = n - v

        dprint("Checking difference %d is not in %s" % (difference,
            gBuckets[b]))
        if difference in gBuckets[b]:
            return False
    return True

def placeIn(b, n):
    global gBuckets

    if canPlaceIn(b, n):
        dprint("Putting %d in bucket %d" % (n, b))
        gBuckets[b][n] = n
        return True
    else:
        dprint("Can't place %d in bucket %d" % (n, b))
        return False

def removeFrom(b, n):
    global gBuckets

    if n in gBuckets[b]:
        dprint("Removing %d from bucket %d" % (n, b))
        del gBuckets[b][n]

def solve(numbers):
    global gMaxBuckets
    global gBuckets

    dprint("Solving...")
    dprint(gBuckets)
    # guard
    if len(numbers) == 0:
        print "!!! Solved"
        print gBuckets
        return

    # Note, not guarding len(numbers) == 1

    n, remaining = numbers[0], numbers[1:]

    # Try putting n in all three buckets
    for b in range(1, gMaxBuckets + 1):
        didPlace = placeIn(b, n)

        if didPlace:
            solve(remaining)
            removeFrom(b, n)


def main():
    global gMaxNumbers

    initBuckets()

    numbers = range(1, gMaxNumbers+1)

    solve(numbers)

if __name__ == "__main__":
    main()
