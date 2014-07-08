__author__ = 'Agile Developers'

# this is just a workaround -- fix problems with encoding
def replaceUmlaute(content):
    fixedContent = content.replace('ü', 'ue')
    fixedContent = fixedContent.replace('ö', 'oe')
    fixedContent = fixedContent.replace('ä', 'ae')
    fixedContent = fixedContent.replace('ß', 'ss')

    return fixedContent