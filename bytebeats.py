#!/usr/bin/env python

# ./bytebeats.py | aplay

import sys

tunes = [
    # http://royal-paw.com/2012/01/bytebeats-in-c-and-python-generative-symphonies-from-extremely-small-programs/
    lambda t: t*((15&t>>11)%12)&55-(t>>5|t>>12)|t*(t>>10)*32,

    # https://www.noisebridge.net/wiki/Bytebeat

    # @wiretapped
    lambda t: (t^t>>(t>>11)%3^t>>(t>>12)%4),
    lambda t: t>>(t>>11)%4^(t>>10)*(t>>15),
    lambda t: t<<3+(t>>10)%3^t>>4+(t>>12)%4^t**(2+(t>>13)%8),
    lambda t: t^t>>4^(t*((t>>(11+(t>>16)%3))%16))^t*3,
    lambda t: t+(t>>(5+(t>>10)%4)^t),
    lambda t: t+(t>>(5+(t>>10)%8))^t|t>>12,
    lambda t: t|(((t>>1)%(8+(t>>14)%4))+(t>>6)),
    lambda t: t*(3+(t>>10)%(4+(t>>11)%8))|(t>>5),
    lambda t: t^(t+(t>>7))|t*((t>>(16-((t>>19)*4)))%8),

    # @isislovecruft
    lambda t: (~t>>2)*(2+(42&t*((7&t>>10)*2))<(24&t*((3&t>>14)+2))),
    lambda t: (t*5&t>>7|t*9&t>>4|t*18&t/1024)|((t|7)>>5|(t|4)>>9),
    lambda t: ((t*(t>>13|t>>8))|(t>>16)^t)-64
    ]

def play(f):
    for t in xrange(2**19):
        sys.stdout.write(chr(f(t) % 256))

try:
    n = int(sys.argv[1])
    tunes[n]
except:
    print "Usage: ./bytebeats.py song-nr | aplay"
    print
    print "There are %d songs." % len(tunes)
    sys.exit(0)

if sys.stdout.isatty():
        print "Stdout goes to terminal--you probably don't want to do that."
        print "Pipe stdout to `aplay` instead."
        sys.exit(0)

play(tunes[n])
