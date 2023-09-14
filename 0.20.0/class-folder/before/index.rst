Folders classes in 0.19.1
-------------------------

Given this MATLAB code

.. code-block:: RST

    @First/First.m
    @First/method_in_folder.m

.. literalinclude:: ../matlab-files/@First/First.m
    :language: MATLAB
    :caption: ``@First/First.m``

.. literalinclude:: ../matlab-files/@First/method_in_folder.m
    :language: MATLAB
    :caption: ``@First/method_in_folder.m``

and this RST

.. code-block:: RST

    .. currentmodule:: .

    .. autoclass:: @First.First
        :show-inheritance:
        :members:

renders into

.. currentmodule:: .

.. autoclass:: @First.First
    :show-inheritance:
    :members:
