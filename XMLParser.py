# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, file_name):
        try:
            f = open(file_name, encoding='utf-8')

        except IOError:
            raise IOError('파일[]' + file_name + '] 이 존재하지 않습니다.')

        self._xml_tree = ET.parse(f)
        self._pretty_print(self._xml_tree.getroot())

        # ET.dump(self._xml_tree)
        f.close()

    def _pretty_print(self, current, parent=None, index=-1, depth=0):
        for i, node in enumerate(current):
            self._pretty_print(node, current, i, depth + 1)
        if parent is not None:
            if index == 0:
                parent.text = '\n' + ('\t' * depth)
            else:
                parent[index - 1].tail = '\n' + ('\t' * depth)
            if index == len(parent) - 1:
                current.tail = '\n' + ('\t' * (depth - 1))

    def parse_element(self, element):
        result = ""

        for notification in self._xml_tree.findall("Notification_INOUT"):
            referralDocumentUniqueId = notification.find(element).text
            result += referralDocumentUniqueId + ','

        return result


if __name__ == '__main__':
    parser = XMLParser('C://Users//jhkan//Desktop//연세대학교세브란스_221007_RECEIVE.xml')
    parser.parse_element()

