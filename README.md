Wordle Solver
=============

About
-----
I finally looked at Wordle today.  I was never very good at anagrams (nor ever thought games based on 
them were particularly interesting), but thought a character frequency algorithm would probably do 
pretty well.

I didn't look at their source code beforehand.  Hence I used an ngram model I had lying around from a few years
back (to build the corpus of 5 letter words).  There are differences between it and the official one, which is
why `suggest(n=4)` returns multiple options.

Example Run
-----------

```python
$ python
Python 3.9.7 (default, Sep 10 2021, 14:59:43) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from wordle_solver import WordleSolver
>>> w = WordleSolver()
loaded 12915 words with char freqs: [('a', 7316), ('b', 1684), ('c', 1981), ('d', 2274), ('e', 6084), ('f', 937), ('g', 1613), ('h', 1983), ('i', 4399), ('j', 472), ('k', 1558), ('l', 3366), ('m', 2104), ('n', 3749), ('o', 4426), ('p', 1630), ('q', 147), ('r', 4300), ('s', 4996), ('t', 3064), ('u', 2522), ('v', 753), ('w', 766), ('x', 276), ('y', 1638), ('z', 537)]
>>> w.suggest()
[('arose', 27122), ('aeros', 27122), ('seria', 27095), ('riesa', 27095)]
>>> w.gray('arse')
>>> w.yellow('o',3)
>>> w.suggest()
[('tonic', 689), ('ntico', 689), ('nicot', 689), ('conti', 689)]
>>> w.gray('ic')
>>> w.yellow('t',1)
>>> w.green('o',2)
>>> w.yellow('n',3)
>>> w.suggest()
[('mount', 4), ('jotun', 4), ('fount', 4)]
>>> 
```

![image](https://user-images.githubusercontent.com/2049665/151464974-d0a8863d-1fdb-4771-8e76-129dfe036139.png)
