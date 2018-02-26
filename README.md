Webruntime
----------

The webruntime module can be used to launch applications based on
HTML/JS/CSS. This can be a browser or a runtime that looks like a
desktop app, such as XUL (based on Firefox) or NW.js.


Installation
------------

Webrunbtime is pure Python and requires Python 3.4+.
It's only dependency is [dialite](https://github.com/flexxui/dialite).

* ``pip install webruntime``


Example
-------

```py
    >>> from flexx.webruntime import launch
    >>> rt = launch('http://xkcd.com', 'app')
    ...
    >>> rt.close()
```

License
-------

The code of Webruntime is distributed under the terms of
the liberal 2-clause BSD license. See LICENSE for details.
