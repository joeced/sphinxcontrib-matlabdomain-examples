See all linking 0.19.1
----------------------

Given this MATLAB code

.. code-block:: RST

    BaseClass.m
    baseFunction.m
    ClassExample.m

.. literalinclude:: ../matlab-files/BaseClass.m
    :language: MATLAB
    :caption: ``BaseClass.m``

.. literalinclude:: ../matlab-files/baseFunction.m
    :language: MATLAB
    :caption: ``baseFunction.m``

.. literalinclude:: ../matlab-files/src/ClassExample.m
    :language: MATLAB
    :caption: ``ClassExample.m``

and this RST

.. code-block:: RST

    .. currentmodule:: .

    .. autoclass:: BaseClass
        :show-inheritance:
        :members:

    .. autofunction:: baseFunction

    .. autoclass:: src.ClassExample
        :show-inheritance:
        :members:

renders into this

.. currentmodule:: .

.. autoclass:: BaseClass
    :show-inheritance:
    :members:

.. autofunction:: baseFunction

.. autoclass:: src.ClassExample
    :show-inheritance:
    :members: