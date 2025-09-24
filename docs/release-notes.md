# Changelog

All notable changes to this project are documented in this file.

---

## v0.0.2 - 2025-09-23

* Added support for `Column(..., default=...)` in models  
  - By default, all fields now have a **default value of `None`**.  
  - Developers can still **specify a custom default** if needed.  
  - Example:  
    ```python
    class Hero(Model):
        name = Column(str)               # default is None
        age = Column(int, default=20)    # custom default value
    ```

---

## v0.0.1 - 2025-09-23

* Initial version  
* Added documentation  
* Added history