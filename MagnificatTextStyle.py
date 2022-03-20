from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import Color
from reportlab.lib.units import mm

styles = getSampleStyleSheet()
ANTIPHON_PARA_STYLE = ParagraphStyle(name='Psalm',
                                parent=styles['Normal'],
                                fontName = 'Minion',
                                alignment = 0,
                                allowOrphans = 0,
                                allowWidows = 1,
                                backColor = None,
                                borderColor = None,
                                borderPadding = 0,
                                borderRadius = None,
                                borderWidth = 0,
                                bulletAnchor = None,
                                bulletFontName = None,
                                bulletFontSize = 10,
                                bulletIndent = 0,
                                embeddedHyphenation = 0,
                                endDots = None,
                                firstLineIndent = 0,
                                fontSize = 8,
                                hyphenationLang = None,
                                justifyBreaks = 0,
                                justifyLastLine = 0,
                                leading = 10, # how tight the text is
                                leftIndent = 0,
                                linkUnderline = 0,
                                rightIndent = 0,
                                spaceAfter = 0,
                                spaceBefore = 0,
                                spaceShrinkage = 0.05,
                                splitLongWords = 1,
                                strikeGap = 1,
                                strikeOffset = 0.25*mm,
                                strikeWidth =None,
                                textColor = Color(0,0,0,1),
                                textTransform = None,
                                underlineGap = 1,
                                underlineOffset = -0.125*mm,
                                underlineWidth =None,
                                uriWasteReduce = 0,
                                wordWrap = None
                                )
PSALM_PARA_STYLE = ParagraphStyle(name='Psalm',
                                parent=styles['Normal'],
                                fontName = 'Minion',
                                alignment = 0,
                                allowOrphans = 0,
                                allowWidows = 1,
                                backColor = None,
                                borderColor = None,
                                borderPadding = 0,
                                borderRadius = None,
                                borderWidth = 0,
                                bulletAnchor = None,
                                bulletFontName = None,
                                bulletFontSize = 10,
                                bulletIndent = 0,
                                embeddedHyphenation = 0,
                                endDots = None,
                                firstLineIndent = 0,
                                fontSize = 8,
                                hyphenationLang = None,
                                justifyBreaks = 0,
                                justifyLastLine = 0,
                                leading = 7, # how tight the text is
                                leftIndent = 0,
                                linkUnderline = 0,
                                rightIndent = 0,
                                spaceAfter = 0,
                                spaceBefore = 0,
                                spaceShrinkage = 0.05,
                                splitLongWords = 1,
                                strikeGap = 1,
                                strikeOffset = 0.25*mm,
                                strikeWidth =None,
                                textColor = Color(0,0,0,1),
                                textTransform = None,
                                underlineGap = 1,
                                underlineOffset = -0.125*mm,
                                underlineWidth =None,
                                uriWasteReduce = 0,
                                wordWrap = None
                                )