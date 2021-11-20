# Sphinx Xref Example

Basic example of integrating xref's into your own directives and roles.

This generates a Sphinx site with more details!

## Requirements

* pipenv

## Setup

```
pipenv install
```

## Building

```
pipenv run sphinx-build source docs
```

## Contributing

Get dev tools with:

```
pipenv install -d
```

Before committing Python code, run black and mypy!

NOTE: mypy could take a while first run to generate a type cache.

I've found for iteration that you want to rebuild everything:

```
pipenv run sphinx-build source docs -a -E
```

## See Also

* https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html
* https://docutils.sourceforge.io/docs/howto/rst-roles.html
* https://docutils.sourceforge.io/docs/howto/rst-directives.html
* https://docutils.sourceforge.io/docs/ref/doctree.html
