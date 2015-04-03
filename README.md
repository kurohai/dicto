### dicto
Python module to allow dotted notation in a dict.

## Usage

Example
-------

.. code-block:: python

    # coding: utf-8
    from dicto.dicto import dicto

    mydict = {'a': 1}
    mydicto = dicto(mydict)

    mydicto.b = 2

    print mydicto.a
    print mydicto['a']
    print mydicto.b
    print mydicto['b']

    another_dict = mydicto.export()
