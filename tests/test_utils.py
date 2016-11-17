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
                                      ['bla'], {"bli": "blo"}
                                  ]
                                  },
                                  {'Date': [
                                      ["2014-05-12T00:00:00Z"]
                                  ]
                                  }
                              ],
                              {"stuff": "me"}
                          ]
                          }
        self.namespace = "fr:gouv:culture:archivesdefrance:seda:v1.0"

    def test_xmlify(self):
        xml_element = XMLElement(namespace=self.namespace, **self.structure)()
        self.assertEqual(E.tostring(xml_element),
            '<ArchiveTransferRequest xmlns="fr:gouv:culture:archivesdefrance:seda:v1.0" stuff="me"><Comment bli="blo">bla</Comment><Date>2014-05-12T00:00:00Z</Date></ArchiveTransferRequest>'.encode('utf-8'))
        self.assertEqual(xml_element.attrib, {'stuff': "me"})
        self.assertEqual(xml_element.Comment.attrib, {'bli': "blo"})



if __name__ == '__main__':
    main()
