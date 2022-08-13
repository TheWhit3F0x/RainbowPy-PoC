# About RainbowPy

Python3 required!

RainbowPy is a simple script written in Python that demonstrates the funcionality of Rainbow Tables in a really simplified way.
This script is not intended for real use in real scenarios.

This repository is not maintained.

PS: This won't evolve to a real-use tool in the future as I actually don't have enough knowledge and interest to do it.

# Usage

There are two scripts in this repository (which can be imported into another scripts, btw).

## Rainbowgenerator

Generates a hash chain from a seed (random if not provided) and returns the seed, a PoC hash obtained through the process and the final hash

```
usage: rainbowgenerator.py [-h] [--seed SEED] --chainlength CHAINLENGTH --pocindex POCINDEX

options:
  -h, --help            show the help message
  --seed SEED, -s SEED  The seed to initilize the chain [Default: Random]
  --chainlength CHAINLENGTH, -c CHAINLENGTH  The chain's length [Required]
  --pocindex POCINDEX, -p POCINDEX  The index from which to get the PoC hash [Required]
```

## Rainbowcheck

Checks if a PoC hash is in a chain of determined length and returns the original string if found. To define a chain, its seed, final hash and length must be provided

```
usage: rainbowcheck.py [-h] --seed SEED --endhash ENDHASH --pochash POCHASH --chainlength CHAINLENGTH

options:
  -h, --help            show the help message
  --seed SEED, -s SEED  The seed of the corresponding chain [Required]
  --endhash ENDHASH, -e ENDHASH The final hash of the chain [Required]
  --pochash POCHASH, -p POCHASH The PoC hash from which to get the original string [Required]
  --chainlength CHAINLENGTH, -c CHAINLENGTH The chain's length [Required]
```
