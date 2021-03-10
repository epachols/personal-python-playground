# Python note

## Python language structure

Python is really 'written' in cpython. when one writes py code, it is read by an interpreter that converts it to bytecode, and then that bytecode is fed into the cpython virtual machine -> THAT code runs.

python created in 1991 (monty python)
py2 in 2008 ->> py3

## python datatypes

### Fundamental data types

##### int - integer

##### float - floating point number

##### bool - boolean

True or False (note capital use)

##### str - string

single or double quotes

multiline strings -> long_string = '''
asdflakjdfs alskdfjasf lots
lots
and lots fo stuff
alrightie
'''

can convert numbers into strings by just using the str(), likewise inverted with int();

formatted strings (press f to pay respects)
name= 'timTom'
adjective = 'moppet'

f'hi {name}. nice weather we're having, {adjective}'

strings accept bracket notation for index reference [start:stop:stepOver]
'hi tommy'[3] = 't'
'hi tommy'[0:6:2] = 'htm'
'hi tommy'[::1] = 'h tmy'
'hi tommy'[-1] = 'y'
'hi tommy'[::-1] = 'ymmot ih' (walk the thing backward)

can include or omit as seen above

strings are immutable, so they don't support a direct assignment

len() is the length calculator built in method for strings.

##### list -

most similar to an array.
[1,2,3,4,5]
mutable
list slicing myList[1:3] - doesn't modify the original list, creates a copy without modifying.
new_thing = thing[:] - makes an exact copy with a new reference.

matrix:
2d lists

.append(object) -> modifies in place (because you're calling it on the function)
.insert(index, object) -> modifies in place (MIP)
.pop(index) -> MIP, .pop(0) will pop the single item at the 0 index RETURNS the removed item.
.remove(value) -> MIP remove(0) will remove the value 0
.clear() -> empties the list. MIP
.index(value, start, stop) -> value we are looking for, where do we start looking, where do we stop looking.
'in' ('x' in basket) -> looks for x in the basket list. can also use this on strings
.count(value) -> how many times value occurs in the list
.sort() -> MIP (sorts strings like javascript by ascending char code)
sorted(list) -> produces a new one rather than modifying the existed list
.reverse(iterable) -> MIP
.join(iterable) -> creates a new item, str item to join on comes first, then iterable is passed to method.
" ".join([array, of, words]) === array of words

common list patterns -
see the list[::-1] pattern (like calling reverse, but why bother lol!)
list(range(1,100)) -> this will instantiate a new list counting from 1-100 (powerful stuff!)

list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9] --> unpacking and assigning, *other takes the place of an assignment in between that took everything after 3 and before 9.

##### tuple -

like a list, but an immutable list
mytuple = (1,2,3,4,5)
we can check if things are in there, but we can't CHANGE anything in it. good for saying "don't touch"
faster than lists, slightly.
a tuple with a single item will look like this (2,) --> will have a silly funny comma
.count()

##### set - set

unordered collection of unique values. myset = {1,2,3,4,5}
print(1 in myset) = true
len(myset) = 5
myset.copy() => returns a copy. can set to variable

myset = {1,2,3,4,5}
yourset = {4,5,6,7,8,9,10}

methods--
.difference(yourset) --> give the difference of before the '.' and what is passed
.discard(value) --> MIP removes a value from the set
.difference_update(yourset) --> MIP removes the differences.
.intersection(yourset) --> returns the common things to both sets.
isdisjoint(yourset) --> do their sets NOT overlap?
issubset(yourset) --> is mine a subset of yours? T/F
issuperset(yourset) --> does mine encompass yours? T/F
.union(yourset) --> returns a new set, union of the two removes duplicates, bitwise or operator is the union so (myset | yourset)

##### dict - dictionary

unordered, assigned by key, keys must be unique, immutable (num, bool, string)
dictionary {
'key': value,
'key': value
}
dictionary[key] = value;

methods--
using .get(key, defaultValue) --> will return none rather than error, better than assignment checking.
can also instantiate a dictionary with dict(name="stuff")
print('basket' in user) --> T/F
thing.keys(), things.values(),
.item() --> grabs the entire key value pair
.items() --> returns a tuple[(key, value), (key, value), ...]
.clear() --> empties the dictionary
.popitem() --> pops off an item from the dictionary, the last one, but unordered.
.update({key: value}) --> can call to change an item

### classes -> custom types

### specialized data types

complex data type = real num imaginary quotient.
bin() returns the binary representation 0b'binarynumberhere'
print(bin(`0b110', 2)) yields 5.

#### none

the absence of value

### basic operators

+, -, /, \*, \*\*, %
// -> round down divide. neat!

### functions

input() - note that the input this receives is converted to a string automatically
round() - .....
googleable - python3 math functions.

### variables in python

\_ signifies a private
standard in snake case
case sensitive
no overwriting key words (see reference)
good convention is CAPS REFERENCE IS constant
\_\_ is dunder -> dunder variable - left alone, and not assigned.

### logic notes

```
if thing_i_care_about and other_thing:
  indented code to nest
elif some_other_condition:
  different code
else:
  do the last thing
```

interpreter finds meaning in the spaces, hence importance of indentation

falsy and truthy follow javascript rules for the most part it seems. TODO: verify/edit this line

ternary logic: do_if_true if condition_here else do_if_false

short circtuiting:
if is_friend or is_user: print('best friends forever') put the condition that narrows it the most first, speeds up return time. interpreter doesn't care after the first truthy value.

logical operators: and, or, >, <, =, and not,

#### Looping:

for item in (tuple, list, dictionary)

dictionary looping methods
for item in user.items():
print(item) -> key-value pairs
for item in user.values():
print(item)
for item in user.keys():
print(item)
CAN ALSO: unpack
for key, value in user.items():
print(key, value) -> key-value pairs

RANGE:

```
range(start, stop, stepOver)

for number in range(0, 100, 25):
 print(number) --> 0, 25, 50, 100.
```

ENUMERATE:
takes in an iterable, and gives you an index

```
for index, char in enumerate(iterable):
  print(index, char)
```

WHILE LOOPS:

```
while condition_is_happening:
  do something()

while i < 50:
  do something()
  i++
else:
  print('done')

while True:
  response = input('hello!')
  if (response == 'bye'):
    break
```

note: the else attached to the while loop creates a resolve condition.

other notes:
break --> can use in for loop or while loop
continue --> go to the next move in the loop
pass --> does nothing, but a good way to placehold while coding to check a loop.

### Functions

def -> defining a function coming up. snake_case() variable names

```
def say_hello():
  print('hellooooo')

say_hello()
```

parameters and arguments -->
arguments are used as the actual values provided to a function
parameters are what the functions expect

positional arguments (order matters)
keyword arguments (defining out of order with using the parameter as a keyword, sort of bad practice)

default parameters - set at function def just like js.

implicit return of all functions is 'None'

```
Should do one thing really well
and should return something

Use Descriptive names
```

##### Docstrings

python supports docstrings, where you can give descriptive information about the function to the head of the function using three single quotes '''

Dunder doc

print(test.\_\_doc\_\_) gives the full description of a function with the \_\_main\_\_ method as well.

#### clean code notes

```
huge if/else chains vs clean returns.
```

#### \*args and \*\*kwargs

```
def super_func(\*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))
```

rule of order of including things:
super_funky(params, \*args, default parameters, \*\*kwargs):

#### := the walrus operator

assignment of variable value mid line

```
a = 'hellllllooooooooo howard'

while ((n := len(a)) > 10):
  print(f'too long {n} elements')
  a= a[:-1]
```

#### scope

python looks for variables first in...

- local
- parent local
- global
- python built-in fuctions

using the global keyword in front of a scoped reference to a variable shortcuts using the one in global if it exists.

dependency injection by wrapped function calls removes the global keyword necessity.

#### everything in python is an object (like js)

#### Classes

```
class CamelCaseVar:
  pass
```

#### HELP

calling help() on pretty much everything will print you out a list of built-in-methods and other informatino.

classmethod vs staticmethod
classmethod has access to the cls parameter, able to instantiate the class.
staticmethod does not, has no access.

#### 4 pillars of oop

##### encapsulation

separate code out by purpose

##### abstraction

hiding information that's unnecessary ()

Public vs private variables (without this one can dot-notation modify a method of an object.)

underscore means don't modify this thing.

no true abstraction protection.

##### inheritance

```
class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'attacking for 12 damage, {self.num_of_arrows} arrows remaining')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.attack()
archer1.attack()
```

isinstance(instance, class)
wizard 1 is an instance of user, and of wizard.

#### dunder methods

\_\_im_special\_\_
Dunder methods are inherited from parent objects, some of them are sort of like backdoor keys

take \_\delete\_\_
which gives one access to the del keyword.

or \_\call\_\_
which lets you use the instantiated class object by calling it

or \_\getitem\_\_
which allows you to reference the object with [] references, you set what method it should return (i.e., go into my dictionary and look at "dates" list)

Multiple inheritance

```
class Hybrid(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wiziard.__init__(self, name, power)
```

##### polymorphism

can be multiple things, multiple classes due to inheritance.

#### MRO method resolution order

What's first in line? so it goes up a level and checks all the items in that generation.

you can check the resolution order by calling print(object.mro())

MRO rules changed to depth-first search. important to note.

### functional programming in PY

pure functions in python

1. same thing in, always same thing out.
2. shouldn't produce side effects.
   print has side effects

map(func, \*iterables) --> function first. have to convert to a list. (makes a new one)

filter(func, \*iterables) --> also brings a return object. have to run list() on it to turn it into a list. (good, like, return a set, etc)

zip(my_list, your_list, this_list etc....) --> puts two iterables together into tuple sets

reduce(function, sequence) --> from functools import reduce (module import). reduce reduces iterables down to a certain data type. by an accumulator.

```
def accumuluator(acc, item):
  return acc + item

# reduce allows us to say
print(reduce(accumulator, my_list, 0))
# passes in the accumulator function, the iterable, and a start value for the accumulator.
```

#### Lambda expressions

one-time anonymous functions that you don't need more than once.

```
lambda param: action(param)

# so, for example
print(list(map(lambda item:item*2, my_list)))

# sorting by the second item of a tuple set
a.sort(key=lambda x: x[1])
```

#### List Comprehensions

exactly as it says
it comprehends an expression that says "make a list outta this stuff"

```
my_list = [param for param in iterable]
new_thing = [x for x in my_list ] (for example)
new_thing = [x for x in my_list if item % 2 == 0] (for example)
```

#### Set and Dictionary Comprehension

likewise for dictionaries and sets.

```
simple_dict={
  'a':1,
  'b':2
}

my_dict = { key:value**2 for key,value in simple_dict.items()}

# we can even do a dict comprehension out of a list!
my_dict = { num:num*2 for num in [1,2,3]}
```

### Decorators

have the @ sign followed by some sort of name
functions in python are first-class citizens(sweet). they can be passed just like variables.

```
def hello():
  print('helloooooo')

greet = hello
del hello
hello()  # this brings up nothing

print(greet())  # this still brings up hello even after calling del
```

All that was deleted was the named reference hello to the place in memory where the function that was defined lives. by giving it another place in memory garbage collection leaves it behind.

'decorators supercharge functions and give them extra features'

Higher Order Functions (HOC)

Any function that accepts a function as a param, or returns a function. (think wrappers, onions, ogres, map(), reduce(), filter())

decorator multi-use

```
def my_decorator(func):
  def wrap_func(*args, **kwargs):
    func(*args, **kwargs)
  return wrap_func
```

### errors in python

syntax errors (highlighting)
quite a few built-in exceptions

how to avoid?
Type checking:
return checking:
input checking:

```
while True:
  try:
    do something
    do something
    do something
  except ValueError:   # you can specify what kind of error to care about.
    what to do if we failed
    do something else
    print error(?)
  except ZeroDivisionError:
    please don't divide by zero
  else:
    break
  finally:
    print('ok i am finally done')
```

can also raise TypeOfError('error message goes here')

### Generators

range() is a generator - specifically doesn't create a space in memory. so..

print(list(range(10000000))) will literally sit on top of memory until it's done. easier to do this with a generator, singular assignments.

any iterable has the \_\_iter\_\_ dunder method. generators are iterable. generator is a special kind of iterable, a subset.

```
def generator_function(num)
  for i in range(num)
    yield i*2

g = generator_function(100)
print(g)
print(next(g))

```

note how instead of returning the list, we yield.

the moral of the story is

if you performance test looping over a range takes half the time that looping over a range AND converting it to a list. exceptionally useful for long loops, large data sets, and not wanting to occupy huge amounts of data.

Switch the return of the loop function you are making to yield to create a generator, many python libraries use generators rather than lists under the hood.

```

# this is how for loops work under the hood in python.

def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      print(next(iterator)*2)
    except StopIteration:
      break

```

### Modules in PY

naming convention: snake case

pycache is created every time we run a file with import statements. it caches the contents of the imports into pycache.

### package = parent folder for a module

import statement works

each package created adds an \_\_init\_\_.py in the package. can be empty. (pycharm will do this for you)

### \_\_name\_\_

the default file that is run (head honcho of imports) gets dunder main.

```
if __name__ = '__main__':
```

is a common line, which means "only run the following code if this is the main file", common practice as projects get bigger and bigger.

### python has tons of built-in-modules

has a package system.

PMI - python module index. check it for possible built in modules.

print(dir(module_name))

```
# the random module
random.int(1,100)
random.choice(["apple", "banana","kiwi"])
random.shuffle(my_list) # modifies in place
```

import thing as thang.
import thing as thang from thing_parent

#### sys module

sys is super useful - allows the use of argv

```
import sys
sys.argv[filename, index1, index2]
```

```
# example of a guessing game using sys argv, running the file and passing two int values gives us (note, basic error handling only)


import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

print(f'let\'s play a game! pick a number between {start} and {end}! Ready?...')

random_num = random.randint(start, end)

while True:
    try:
        response = int(input(f"what's your guess? (number between {start} and {end}):  "))
        if response == random_num:
            print(f'congratulations, you guessed {random_num} correctly!')
            break
        else:
            print(f"i'm sorry, {response} was not correct, guess again.")
    except:
            print(f"ouch, that wasn't even valid input")
else:
    print('all done, play again?')

```

### the power of Pypi!

Python package index, or (pypy)["https://pypi.org"] for short is the cool kids' shopping mall. (tensorflow, all that good stuff).
csv parser.

standard practice

1. does it already exist( in python built-in lib )
2. does it already exist (in pypi? have people been working on it? npm style)
3. go to the home page of the project.

### Virtual Environments

setting up different package version environments for different projects.

can create a venv using pycharm in any directory you want to have a py project. then any package installed there will become venv registered separately.

#### some useful modules

Collections:

```
from collections import Counter, defaultdict, OrderedDict

li= [1,2,3,4,5,6,7]

print(Counter(li))  # makes a dictionary with each value in the list as a key, and a counter as of the value within the list as the value

dictionary = defaultdict(callable_obj_or_lambda_fx, {'a':1, 'b':2})

# callable (like int) to feed a value if there isn't a value already at a referenced key.
# so dictionary['c'] would return a new default value at that key, rather than a reference error.
# useful for tons of stuff!

# an ordered dictionary retains the order of insertion (has a hidden key?)
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['b'] = 2
d['a'] = 1


print(d2 == d) # false, due to improper order. ordered dict gives you an order.

PYTHON DICTIONARIES ARE ORDERED BY DEFAULT NOW.
```

Other useful ones

```
import datetime

print(datetime.date.today())
# timezones, different time data, etc

from time import time
# various methods for use

from array import array
# arrays take up less memory, because it sets how much memory you can use at instantiation
array(typecode, my_list)
# typecode comes from the docs, can access it like you would a list. optimization that's non-generator.
```

### debugging in py

1. definitely setup linting (have it in pycharm or vscode aitty)
2. use an editor (duh)
3. read errors (of course!)
4. PDB - a built in module for python , the python debugger

```
import pdb

def thing(first, second):
  # ~somewhere in yer function
  pdb.set_trace()   # opens pdb

  # code pauses where you set trace, you can check what things are
  # help -- brings you a list of commands that get you stuff in python debugger.
  # list - lists the source code for the current file
  # step - goes to next line, to step through the code
  # continue - run normally
  # a - gives you all the arguments of the function you're in
  # w - shows context of current line

  # can change variables and code to test things inside pdb easily, useful for testing output.
```

### file I/O

input - output (writing to pdfs, images, etc)

OPEN: 'open('test.test')' in python.... opens a file for write.

```
myfile = open('test.test')

print(myfile.read()) #for example
myfile.seek(0)
```

file reads are done by a cursor, so after the first call one would need to use seek(0) to start over if wanted to read again

```
myfile.readline() #reads one line at a time, moving cursor
myfile.readlines() # get a list of all the lines read

myfile.close()
```

##### BETTER SYNTAX: with open

```
with open('test.txt', mode='r') as my_file  # mode setting here in params of open. can use 'w' for write. or 'r+' for readwrite. write opens resets the cursor to 0

# mode='a' is the append mode, adds whatever you're writing to the end of the file.

print(my_file.readlines())
```

##### create a file that doesn't exist - write mode without a file preexisting.

#### File paths

starts in relpath of main file being run unless otherwise set.

pathlib - an O.O.F.S. path - can take care of filepath for you depending on the machine you are running (python cares \ vs /)

#### File I/O errors

put it in a try: - except: raise err - block.

### Regex in Python

```
import re
string = 'search inside of this text please!'

print('search' in string) #true

a = re.search('this', string) #returns a match object or none output, includes span of where it occurs in the string

print(a.span) # tells where it occurs as a tuple
print(a.start) # when it starts
print(a.group(1))  # print the things that belong to the first capture group
```

```
import re

pattern = re.compile('this')
string = 'search inside of this text please!'
a = pattern.search(string)

# methods include but not limited to:
# findall(string) finds all instances in a list
# fullmatch(string) has to be an exact match, returns none otherwise
# match(string) doesn't care what comes afterwards
```

#### advanced patterns

see w3 schools for differences in regex.

##### (regex101)[https://www.regex101.com]

```
import re
pattern = re.compile(r"your_regex_here")  # r stands for raw string (keeps escapable chars)
```

example challenge: write a regex pattern for password check

```
# at least 8 chars long
# contain any sort of letters, numbers, $%#@
# has to end with a number

[A-Za-z0-9$%#@]{8,}\d
```

### unit testing additional notes in testing folder.

```
# running tests in unison

python3 -m unittest
```
