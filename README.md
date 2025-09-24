<p align="center">
  <a href="https://finesql.mohir.cloud"></a>
</p>
<p align="center">
    <em>FineSQL, async and await, focused on developer experience.</em>
</p>
<p align="center">
<a href="https://pypi.org/project/finesql" target="_blank">
    <img src="https://img.shields.io/pypi/v/finesql?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://finesql.mohir.cloud" target="_blank">https://finesql.mohir.cloud</a>

**Source Code**: <a href="https://github.com/goldendevuz/finesql" target="_blank">https://github.com/goldendevuz/finesql</a>

---

**FineSQL** is a small library built on top of <a href="https://fineio.readthedocs.io/en/stable/" class="external-link" target="_blank">FineIO</a>.

**FineSQL** has a small number of utility functions that allow working with `async`, `await`, and concurrent code in a more convenient way under my (<a href="https://twitter.com/goldendevuz" class="external-link" target="_blank">@goldendevuz - Abdulmajid Yunus</a>) very opinionated and subjective point of view.

The main goal of **FineSQL** is to improve **developer experience** by providing better support for **autocompletion** and **inline errors** in the editor, and **more certainty** that the code is **bug-free** by providing better support for type checking tools like **mypy**.

**FineSQL** also tries to improve **convenience** and simplicity when working with **async** code **mixed** with regular <abbr title="synchronous code, code that is not async">**blocking code**</abbr>, allowing to use them together in a simpler way... again, under my very **subjective** point of view.

## 🚨 Warning

This small library only exists to be able to use these **utility functions** until (and if) they are integrated into **FineIO**.

It will probably take some time for that to happen (or to be decided if it will be included or not).

So I made this to be able to use these ideas right now. 🤓

## Can I Use It?

Yes 🎉 (but continue reading).

You can use this and evaluate the **library API design** I'm proposing. It will probably be useful to know if it works and is useful for you (I hope so).

But still, consider this lab material, expect it to change a bit. 🧪

If you use it, **pin the exact FineSQL version** for your project, to make sure it all works.

Have **tests** for your project (as you should, anyway). And **upgrade the version** once you know that the new version continues to work correctly.

Still, it's **just 4 functions**, so there's not much to change, if you had to refactor your code to update something it would not be much.

And if you don't want to add `finesql` as a dependency to your project, you can also just copy the main file and try out those functions, it's quite small (but in that case you won't get updates easily).

## Requirements

As **FineSQL** is based on **FineIO** it will be also installed automatically when you install **FineSQL**.

## Installation

<div class="termy">

```console
$ pip install finesql
---> 100%
Successfully installed finesql fineio
```

</div>

## How to Use

You can read more about each of the use cases and utility functions in **FineSQL** in the <a href="https://finesql.mohir.cloud/tutorial/" class="external-link" target="_blank">tutorial</a>.

As a sneak preview of one of the utilities, you can **call sync code from async code** using `sqlify()`:

```Python
import time

import fineio
from finesql import sqlify


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def main():
    message = await sqlify(do_sync_work)(name="World")
    print(message)


fineio.run(main)
```

**FineSQL**'s `sqlify()` will use FineIO underneath to do *the smart thing*, avoid blocking the main **async** event loop, and run the **sync**/blocking function in a **worker thread**.

### Editor Support

Everything in **FineSQL** is designed to get the best **developer experience** possible, with the best editor support.

* **Autocompletion** for function arguments:

* **Autocompletion** for return values:

* **Inline errors** in editor:

* Support for tools like **mypy**, that can help you verify that your **code is correct**, and prevent many bugs.

## License

This project is licensed under the terms of the [MIT license](https://github.com/goldendevuz/finesql/blob/main/LICENSE).
