.. grill.names documentation master file, created by
   sphinx-quickstart on Sun Apr  9 21:39:36 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to grill.names's documentation!
=======================================

This package offers ``Name`` objects for digital content creation.

----

Overview
--------

Digital content encoded in machine-readable formats can be created, viewed and distributed on digital electronics devices without caring how the data is named.

However, for a project with a life cycle like: ``Idea → Encode → Distribution``, going through each stage requires human input, and for that, ease of data tracking and discoverability is a requirement.

At ``the grill``, every project's contribution can be uniquely identified via the :ref:`CGAsset` name.

Contributions will naturally go through multiple iterations, with the most important ones being "snapshot". These snapshots are saved on a filesystem, called ``versions`` of the asset and can be made up of multiple file resources, which can be identified via the :ref:`CGAssetFile` name.

Names
-----

.. toctree::
    :maxdepth: 4

    CGAsset
    CGAssetFile
    DateTimeFile
    DefaultName
    LifeTR

Indices and tables
==================

* :ref:`genindex`
