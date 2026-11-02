# Import table: expected answers

## Function shape

```python
def build_import_table(src_code: bytes) -> tuple[dict[str, str], list[str]]:
```

Returns two things:

- **Dict:** names the file can use, mapped to what they refer to.
- **List:** modules the file star-imported.

## Expected results

| Fixture | Code | Dict | Star list |
|---|---|---|---|
| `import_alias.py` | `import numpy as np` | `{"np": "numpy"}` | `[]` |
| `import_plain.py` | `import numpy` | `{"numpy": "numpy"}` | `[]` |
| `from_import.py` | `from numpy import float_` | `{"float_": "numpy.float_"}` | `[]` |
| `from_import_alias.py` | `from numpy import float_ as f` | `{"f": "numpy.float_"}` | `[]` |
| `import_submodule_alias.py` | `import numpy.linalg as la` | `{"la": "numpy.linalg"}` | `[]` |
| `import_submodule.py` | `import numpy.linalg` | `{"numpy": "numpy"}` | `[]` |
| `from_import_star.py` | `from numpy import *` | `{}` | `["numpy"]` |
| `comment_and_string.py` | `import numpy as np`, plus the symbol in a comment and a string | `{"np": "numpy"}` | `[]` |

## Why

- **Star imports stay out of the dict.** They don't create a name for the module, and a special key like `"*"` would get overwritten if a file star-imports two modules.
- **`import numpy.linalg` only creates `numpy`.** The `.linalg` comes from the code that uses it, so the path stays `numpy`. With `as la`, the name refers to the submodule, so the path is `numpy.linalg`.
- **Comments and strings add nothing.** Only real import statements count.
