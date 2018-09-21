# JobberQuestions
These are the solutions to the provided questions in docs from the file "Engineer Coding Challenges - 1.pdf"

# Usage
## Tests
[![Build Status](https://travis-ci.org/dhaberst/JobberQuestions.svg?branch=master)](https://travis-ci.org/dhaberst/JobberQuestions)

If tests need to be run manually the following commands can be run:
```bash
python nextVersion.spec.py
python createSpiral.spec.py
```
Otherwise sit back and enjoy CI :smiley:
## Problems
### nextVersion.py
This function takes in a version number i.e 1.2.3 and increments it. As a note, all numbers except the first one must not be greater than 10.
```
nextVersion("1.2.3") == "1.2.4"
```

### createSpiral
This function creates  a matrix (2D array) where numbers 1 to N are represented as a clockwise spiral.
```
createSpiral(3) == [[1,2,3],
                    [8,9,4],
                    [7,6,5]]
```
# How I Solved?
### nextVersion.py
This one was pretty straight-forward since all it is is an incrementing number with a slight twist that the first number can increase beyond 9. All that means for me is that when the length of the number increases i.e from 9 - 10 (length 1 to 2) or 99 - 100 (length 2 to 3), then we know that it needs to go from 9.9 to 10.0. The shortcut that you can take is you remove the first occurrence  of a period from 1.0.0 to make 10.0.
### createSpiral
This one is slightly more complex but stems from the idea that you need to generate a spiral sequence. For example a spiral sequence for N = 3 would be 3,2,2,1,1. That means we go 3 right, 2 down, 2 left, 1 up, 1 right. Using this idea we can create a sequence generator which is the base of our algorithm. Now that we know we go from right, down, left, up, we can cycle through those states and insert incrementing numbers according to the sequence generator. 
# Resources
## Python Docs
- [Unit Testing](https://docs.python.org/3.6/library/unittest.html)
- [Regex](https://docs.python.org/3/library/re.html)
## Stack Overflow
- [Replace first occurance of string](https://stackoverflow.com/questions/4628618/replace-first-occurrence-of-string-in-python)

