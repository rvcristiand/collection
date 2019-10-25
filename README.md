<!--- [comments in markdown](https://www.jamestharpe.com/code-comments-markdown/) -->
<!--- [standard-readme](https://github.com/RichardLitt/standard-readme) -->
# collection

<!--- [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) -->

<!--- Standard Readme Style -->

<!--- Your README file is normally the first entry point to your code. It should tell people why they should use your module, how they can install it, and how they can use it. Standardizing how you write your README makes creating and maintaining your READMEs easier. Great documentation takes work! -->
A metaclass to avoid instances with the same attributes.

<!--- This repository contains:

1. [The specification](spec.md) for how a standard README should look.
2. A link to a linter you can use to keep your README maintained ([work in progress](https://github.com/RichardLitt/standard-readme/issues/5)).
3. A link to [a generator](https://github.com/RichardLitt/generator-standard-readme) you can use to create standard READMEs.
4. [A badge](#badge) to point to this spec.
5. [Examples of standard READMEs](example-readmes/) - such as this file you are reading. -->

<!--- Standard Readme is designed for open source libraries. Although it’s [historically](#background) made for Node and npm projects, it also applies to libraries in other languages and package managers. -->


## Table of Contents

<!-- - [Background](#background) -->
<!-- - [Install](#install) -->
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<!-- ## Background -->

<!--- Standard Readme started with the issue originally posed by [@maxogden](https://github.com/maxogden) over at [feross/standard](https://github.com/feross/standard) in [this issue](https://github.com/feross/standard/issues/141), about whether or not a tool to standardize readmes would be useful. A lot of that discussion ended up in [zcei's standard-readme](https://github.com/zcei/standard-readme/issues/1) repository. While working on maintaining the [IPFS](https://github.com/ipfs) repositories, I needed a way to standardize Readmes across that organization. This specification started as a result of that. -->
<!-- Implementación del problema del método de elementos finitos en [python](python.org). -->


<!--- > Your documentation is complete when someone can use your module without ever
having to look at its code. This is very important. This makes it possible for
you to separate your module's documented interface from its internal
implementation (guts). This is good because it means that you are free to
change the module's internals as long as the interface remains the same. -->

<!--- > Remember: the documentation, not the code, defines what a module does.

~ [Ken Williams, Perl Hackers](http://mathforum.org/ken/perl_modules.html#document) -->

<!--- Writing READMEs is way too hard, and keeping them maintained is difficult. By offloading this process - making writing easier, making editing easier, making it clear whether or not an edit is up to spec or not - you can spend less time worry about whether or not your initial documentation is good, and spend more time writing and using code. -->

<!--- As well, standardizing can help elsewhere. By having a standard, users can spend less time searching for the information they want. They can also build tools to gather search terms from descriptions, to automatically run example code, to check licensing, and so on. -->

<!--- The goals for this repository are:

1. A well defined **specification**. This can be found in the [Spec document](spec.md). It is a constant work in progress; please open issues to discuss changes.
2. **An example README**. This Readme is fully standard-readme compliant, and there are more examples in the `example-readmes` folder.
3. A **linter** that can be used to look at errors in a given Readme. Please refer to the [tracking issue](https://github.com/RichardLitt/standard-readme/issues/5).
4. A **generator** that can be used to quickly scaffold out new READMEs. See [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme).
5. A **compliant badge** for users. See [the badge](#badge). -->

<!-- ## Install -->

<!-- Este proyecto usa [python](http://nodejs.org) y varias librerias científicas. La recomendación es instalar [Ananconda](https://www.anaconda.com/distribution/). -->

<!--- ```sh
$ npm install --global standard-readme-spec
``` -->

## Usage

You can create classes with the `UniqueInstances`
```python
class Coordinate(metaclass=UniqueInstances):
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        super(Coordinate, self).__init__(x, y, z)
```
and all instances will have differents attributes values.

<!-- ### Generator

To use the generator, look at [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme). There is a global executable to run the generator in that package, aliased as `standard-readme`. -->

<!--- ## Badge

If your README is compliant with Standard-Readme and you're on GitHub, it would be great if you could add the badge. This allows people to link back to this Spec, and helps adoption of the README. The badge is **not required**.

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

To add in Markdown format, use this code:

```
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
``` -->

<!--- ## Example Readmes

To see how the specification has been applied, see the [example-readmes](example-readmes/). -->

<!--- ## Related Efforts

- [Art of Readme](https://github.com/noffle/art-of-readme) - 💌 Learn the art of writing quality READMEs.
- [open-source-template](https://github.com/davidbgk/open-source-template/) - A README template to encourage open-source contributions. -->

<!--- ## Maintainers

[@RichardLitt](https://github.com/RichardLitt). -->

## Contributing

Feel free to dive in! [Open an issue](https://github.com/rvcristiand/pyFEM/issues/new) or submit PRs (pull requests).

collection follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

<!--- ### Contributors

This project exists thanks to all the people who contribute.
<a href="graphs/contributors"><img src="https://opencollective.com/standard-readme/contributors.svg?width=890&button=false" /></a> -->


## License

[MIT](LICENSE)