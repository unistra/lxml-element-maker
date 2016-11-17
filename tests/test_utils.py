from unittest import TestCase, main
from element_maker.utils import XMLElement
from lxml import etree as E


class UtilsTest(TestCase):
    """ Test utils """

    def setUp(self):
        self.structure = {'ArchiveTransferRequest':
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
        self.namespace = "fr:gouv:culture:archivesdefrance:seda:v1.0"

    def test_xmlify(self):
        xml_element = XMLElement(namespace=self.namespace, **self.structure)()
        self.assertEqual(E.tostring(xml_element),
            '<ArchiveTransferRequest xmlns="fr:gouv:culture:archivesdefrance:seda:v1.0" cars="pizza"><Comment foo="bar">baz</Comment><Date>2014-05-12T00:00:00Z</Date></ArchiveTransferRequest>'.encode('utf-8'))
        self.assertEqual(xml_element.attrib, {'cars': "pizza"})
        self.assertEqual(xml_element.Comment.attrib, {'foo': "bar"})



if __name__ == '__main__':
    main()
