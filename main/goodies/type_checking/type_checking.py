""" Type hints are completely ignored at runtime, exactly like TypeScript types are erased 
when compiling to JavaScript. 

In VS Code, the TypeScript-like type checker is Pyright, 
and it is already built into the default Python extension via Pylance.
At the top of a file add pyright comment (#pyrigh: strict)

Running the Python file will not enforce type hints.
Just like TypeScript, type checking happens before running the code.
"""

""" # pyright: strict
"""

def add(a: int, b: int) -> int:
    return a + b

print(add("Hello ", "World"))