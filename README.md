# Quine-McCluskey

Quine-McCluskey is an algorithm used for circuit compression. It takes a Boolean expression and combines them where a bit differs by one, until there are no more differences. It then matches those combined terms to their original "ancestors", finding the minimal amount of terms, and therefore minimizing the circuit.

## Input Format

The program reads a text file given on the command line. The file lists one term per line, for example:

```         
wxy-z
w-xyz
w-xy-z
-wxyz
-wx-yz
-w-xyz
-w-x-yz
```

-   Where `w` and `-w` indicate a boolean variable, and its negation. So the file listed above represents the expression:

$$
wxy\overline{z} + w\overline{x}yz + w\overline{x}y\overline{z} + \overline{w}xyz + \overline{w}x\overline{y}z + \overline{w}\,\overline{x}yz + \overline{w}\,\overline{x}\,\overline{y}z
$$

## How to Run

Pass the input file as a command-line argument to `main.py`:

``` bash
python main.py in.txt
```

## Citations

1.  GeeksforGeeks. [*Python – Combinations of elements till size N in list*](https://www.geeksforgeeks.org/python/python-combinations-of-elements-till-size-n-in-list/). Used: whole article.
2.  poke. Answer to [*How to compare each item in a list with the rest, only once?*](https://stackoverflow.com/questions/16603282/how-to-compare-each-item-in-a-list-with-the-rest-only-once) Stack Overflow. [Answer link](https://stackoverflow.com/a/16603357). Modified by community. License: CC BY-SA 3.0. Retrieved 2026-09-29.
3.  Donut. Answer to [*Remove all the elements that occur in one list from another*](https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another). Stack Overflow. [Answer link](https://stackoverflow.com/a/4211228). Modified by community. License: CC BY-SA 4.0. Retrieved 2026-09-29.
4.  Sven Marnach. Answer to [*Take the content of a list and append it to another list*](https://stackoverflow.com/questions/8177079/take-the-content-of-a-list-and-append-it-to-another-list). Stack Overflow. [Answer link](https://stackoverflow.com/a/8177090). Modified by community. License: CC BY-SA 4.0. Retrieved 2026-09-29.
5.  SilentGhost. Answer to [*How do I access command line arguments?*](https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments) Stack Overflow. [Answer link](https://stackoverflow.com/a/4033743). Modified by community. License: CC BY-SA 3.0. Retrieved 2026-09-29.
6.  W3Schools. [*Python File Open*](https://www.w3schools.com/python/python_file_open.asp). Used: whole page.
7.  user225312. Answer to [*How do I split a string into a list of characters?*](https://stackoverflow.com/questions/4978787/how-do-i-split-a-string-into-a-list-of-characters) Stack Overflow. [Answer link](https://stackoverflow.com/a/4978792). Modified by community. License: CC BY-SA 4.0. Retrieved 2026-09-29.
8.  user1006198. [*Python: How to check if a line is an empty line*](https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line). Stack Overflow question ([question link](https://stackoverflow.com/q/7896495)). Modified by community. License: CC BY-SA 4.0. Retrieved 2026-09-29.
9.  jamylak. Answer to [*How do I remove duplicates from a list, while preserving order?*](https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order) Stack Overflow. [Answer link](https://stackoverflow.com/a/17016257). Modified by community. License: CC BY-SA 4.0. Retrieved 2026-09-29.
10.  GeeksforGeeks. [*Python – Remove spaces from a string*](https://www.geeksforgeeks.org/python/python-remove-spaces-from-a-string/).

## **AI Disclosure**

I wrote the pseudocode and source code for this project. AI was used as a resource for debugging, explaining concepts, generating test cases, documentation formatting, and code auto-fill assistance. For the minimum-combination portion, AI helped me develop the approach and provided examples of using `itertools.combinations` and controlling the nested loops, which I incorporated into my implementation.
