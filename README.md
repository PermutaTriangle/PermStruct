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

For instructions on how to run the algorithm, see the (soon-to-be written)
documentation.

## License
BSD-3: see the [LICENSE](https://github.com/PermutaTriangle/PermStruct/blob/master/LICENSE) file.
