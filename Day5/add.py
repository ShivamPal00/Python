def debug_decorator(cls):
    class DebugClass(cls):
        def _init_(self, *args, **kwargs):
            print(f"Creating instance of {cls._name_}")
            super()._init_(*args, **kwargs)

        def _call_(self, *args, **kwargs):
            print(f"Calling {cls._name_} instance")
            return super()._call_(*args, **kwargs)

    return DebugClass

@debug_decorator
class Calculator:
    def add(self, a, b):
        return a + b

calculator = Calculator()  # Output: Creating instance of Calculator
print(calculator.add(2, 3))  # Output: Calling Calculator instance
