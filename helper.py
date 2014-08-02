__author__ = 'Agile Developers'

# this is just a workaround -- fix problems with encoding
def replaceUmlaute(content):
    fixedContent = content.replace('ü', 'ue')
    fixedContent = fixedContent.replace('Ü', 'Ue')

    fixedContent = fixedContent.replace('ö', 'oe')
    fixedContent = fixedContent.replace('Ö', 'Oe')

    fixedContent = fixedContent.replace('ä', 'ae')
    fixedContent = fixedContent.replace('Ä', 'ae')

    fixedContent = fixedContent.replace('ß', 'ss')

    return fixedContent