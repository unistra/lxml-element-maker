lxml-element-maker
==================

.. image:: https://api.travis-ci.org/unistra/lxml-element-maker.svg?branch=master
    :target: https://travis-ci.org/unistra/lxml-element-maker
    :alt: Build

.. image:: http://coveralls.io/repos/unistra/lxml-element-maker/badge.png?branch=master
    :target: http://coveralls.io/r/unistra/lxml-element-maker?branch=master
    :alt: Coverage

.. image:: https://img.shields.io/pypi/v/lxml-element-maker.svg
    :target: https://pypi.python.org/pypi/lxml-element-maker
    :alt: Version

.. image:: https://img.shields.io/pypi/pyversions/lxml-element-maker.svg
    :target: https://pypi.python.org/pypi/lxml-element-maker
    :alt: Python Version

.. image:: https://img.shields.io/pypi/status/lxml-element-maker.svg
    :target: https://pypi.python.org/pypi/lxml-element-maker
    :alt: Python Version

.. image:: https://img.shields.io/pypi/l/lxml-element-maker.svg
    :target: https://docs.python.org/3/license.html
    :alt: Licence

Requirements
------------

* python 3.4
* lxml 3.4.4

Install
-------

.. code:: bash

    pip install lxml-element-maker

Usage
-----

Transforms a python structure to an xml element with lxml :

.. code:: python

    from element_maker.utils import XMLElement

    structure = {'ArchiveTransferRequest':
                          [
                              [
                                  {'Comment': [
                                      ['baz'], {"foo": "bar"}
                                  ]
                                  },
                                  {'Date': [
                                      ["2014-05-12T00:00:00Z"]
                                  ]
                                  }
                              ],
                              {"cars": "pizza"}
                          ]
                          }
    namespace = "fr:gouv:culture:archivesdefrance:seda:v1.0"
    xml_element = XMLElement(namespace=self.namespace, **self.structure)()
    # Test the element with an xsd schema
    result = xml_element.pass_xsd("./tests/data/test.xsd")
    # Or test the element with an rng schema
    result2 = xml_element.pass_rng("./tests/data/test.rng")

The result is an xml :

.. code:: xml

    <ArchiveTransferRequest xmlns="fr:gouv:culture:archivesdefrance:seda:v1.0" cars="pizza">
        <Comment foo="bar">baz</Comment>
        <Date>2014-05-12T00:00:00Z</Date>
    </ArchiveTransferRequest>


Authors
-------

* Geoffroy : https://github.com/orgs/unistra/people/geoffroybeck
* Morgan : https://github.com/orgs/unistra/people/dotmobo
