Overview
--------

Digital content encoded in machine-readable formats can be created, viewed and distributed on digital electronics devices without concern for the nomenclature of such data.
However, for a project with a life cycle going through ``Idea → Encoding → Distribution``, human input remains crucial, and with it, ease of data tracking and discoverability.

This package provides foundational name objects for digital creation processes at `👨‍🍳 The Grill <https://grill.readthedocs.io/en/latest/>`_, where all project contributions can be uniquely identified via the :ref:`CGAsset` name.

These contributions go through multiple iterations, with the most important ones captured as ``asset snapshots``, versioned independently and stored for persistency.
Each ``version`` of an ``asset`` and can be made up of multiple file resources, which can be identified via the :ref:`CGAssetFile` name.
