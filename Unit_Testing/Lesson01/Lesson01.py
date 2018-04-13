"""
LESSON 1 - Unit Tests Using DOCSTRINGS and DOCTESTS

-- 1.1 DOCSTRING --
"A DOCSTRING is a string literal that’s specified in the source code of a module. It
is used to document a specific segment of the code. Code comments are also used
for documenting the source code. However, there is a major difference between a
docstring and a comment. When the source code is parsed, the comments are not
included in the parsing tree as part of the code, whereas docstrings are included in the
parsed code tree.

The major advantage of this is that the docstrings are available for use at runtime.
Using the functionalities specific to the programming language, you can retrieve the
docstring specific to a module. Docstrings are always retained through the entire runtime
of the module instance." (p.20)

In order to run the docstring, simply open the interactive python command line
and import the module (Ex.: test_module.py), then use the help() function, or print
its documentation (Ex.: print (test_module.Test_Class.__doc__)).

-- 1.2 DOCTEST --
"doctest is the lightweight unit testing framework in Python that uses docstrings to test
automation. The doctest is packaged with the Python interpreter, so you do not have to
install anything separately to use it. It is part of Python's standard library." (p.24)

In order to see the doctest in action, run the following command on the command prompt:
    python -m doctest -v test_module.py
    python -m doctest -v test_module.txt (if importing test_module of another .py file)

Let's take a look at how the doctest works. By comparing the code—specifically
the commands for execution and output—you can figure out quite a few things. doctest
works by parsing docstrings. Whenever doctest finds an interactive Python prompt in
the doctest documentation of a module, it treats its output as the expected output. Then
it runs the module and its members by referring to the docstrings. It compares the actual
output against the output specified in the docstrings. Then it marks the test pass or fail.
You have to use -m doctest while executing the module to let the interpreter know that
you need to use the doctest module to execute the code.

The command-line argument -v stands for verbose mode. You must use it because,
without it, the test will not produce any output unless it fails. Using verbose produces an
execution log irrespective of whether the test passes or fails." (p.25)


See the following files for implementation:
- test_module01.py (docstring)
- test_module02.py (doctest)
- test_module03.txt (doctest from separate file)
"""