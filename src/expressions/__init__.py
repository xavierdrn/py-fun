try:
    # attempt to import class 'Expressions' from the implementation module
    # 'type: ignore' avoids VSCode marking if module is not present
    from .expressions_impl import Expressions # type: ignore

except ImportError:
    # no implementation module is present, import from the default module
    from .expressions import Expressions

# import 'main()' function from 'driver.py'
from .driver import main


# restrict exports including non-underscored names
__all__ = ["Expressions"]
