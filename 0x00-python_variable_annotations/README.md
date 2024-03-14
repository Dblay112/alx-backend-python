What are Variable Annotations?

Variable annotations in Python allow developers to specify the types of variables explicitly. These annotations provide
additional information about the intended usage and expected data types of variables, improving code readability and
enabling static type checking tools to catch potential errors early in the development process.
Key Concepts

    Syntax: Variable annotations are typically added using the colon (:) syntax following the variable name. For
    example:

        python

            my_variable: int

                Type Hints: Annotations can specify primitive data types (e.g., int, str, float) as well as custom
                classes and generic types.

                    Optional Annotations: Annotations are optional and can be used selectively where clarity or type
                    checking is desired.

                        Static Type Checking: Tools like MyPy can perform static type checking by analyzing variable
                        annotations, helping identify type-related errors at compile-time.

                        
