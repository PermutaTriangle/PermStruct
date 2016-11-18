# The PermStruct Algorithm

[![Build Status](https://travis-ci.org/PermutaTriangle/PermStruct.svg?branch=master)](https://travis-ci.org/PermutaTriangle/PermStruct)

PermStruct is an algorithm for discovering descriptions of permutation sets in
terms of so-called generating rules. These descriptions can then be used to
derive generating functions for the permutation sets.

## Installing
To install PermStruct on your system, start by installing the
[Permuta](https://github.com/PermutaTriangle/Permuta) library. Then run
the following commands:
```
$ sudo ./setup.py install
```
If you have [Gurobi](http://www.gurobi.com) installed then you are done. If you
do not have it run:
```
$ make -C exact_cover
$ sudo make -C exact_cover install
```

It is also possible to install PermStruct in development mode, in which case you
run the following instead:
```
$ sudo ./setup.py develop
```

To run the unit tests, you can run the following command:
```
$ ./setup.py test
```

## Usage
Once you've installed PermStruct, it can be imported into a Python script just
like any other Python library:
```
import permstruct
```

As an example we run the algorithm on permutations avoiding the pattern 231.
We start by defining the basis `patts` and then run the algorithm.
```
patts = [Permutation([2,3,1])]
struct(patts)
```
When the input is just the basis the algorithm will infer other settings from
the longest pattern in the basis, `k = 3` here:

* `size = k + 1` (the maximum size of the rules to try)
* `perm_bound = k + 2` (the longest permutations to use from Av(patts))
* `verify_bound = perm_bound + 2` (the longest permutations from Av(patts) to use to verify the cover found)
* `subpatts_len = None` (the longest subpattern to use from the basis; `None` implies we use all subpatterns)
* `subpatts_num = None` (the maximum number of subpatterns to use from the basis)
* `subpatts_type = SubPatternType.EVERY` (the type of subpattern to use from the basis)
* `ask_verify_higher = True` (whether to ask about verifying with longer permutations)

If the algorithm is too slow it good to try to decrease the size of the rules
(`size`). If the algorithm does not find a cover it is often good to try
increasing the rule size. If the algorithm finds a cover that is not verified it
is good to increas the `perm_bound`.

## PyPy
If you have PyPy installed you can do all of the above in PyPy.

## License
BSD-3: see the [LICENSE](https://github.com/PermutaTriangle/PermStruct/blob/master/LICENSE) file.
