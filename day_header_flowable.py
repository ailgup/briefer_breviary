from reportlab.platypus import BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate, Flowable, CondPageBreak, HRFlowable, Table

from reportlab.lib.units import mm
from reportlab.lib.colors import Color, black
from reportlab.pdfbase.pdfmetrics import stringWidth

MAGNIFICAT_RED = Color( 214/255 ,50/255, 84/255, alpha=1)

HEADER_WIDTH = 90*mm

POINT_TO_MM = 0.3527

##FORMATTING
DATE_FONT = "Minion"
DATE_FONT_SIZE = 13
DATE_FONT_COLOR = MAGNIFICAT_RED

LEVEL_FONT = "Minion"
LEVEL_FONT_SIZE = 8
LEVEL_FONT_COLOR = MAGNIFICAT_RED

TITLE_FONT = "MinionSub"
TITLE_FONT_SIZE = 8
TITLE_FONT_COLOR = black
class DayHeader(Flowable):
    """
    Draw a header thing for the day with option for (Solem, Feast, Mem, Opt. Mem)
    
    ----                                        ----
    |                MARCH 19 (Date)                |
    |               SOLEMNITY  (Level)              |
    ----            St. Joseph  (Title)          ----
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, date="", title="", level = ""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.date = date
        self.title = title
        self.level = level
        
        
        self.date_font_size = DATE_FONT_SIZE
        self.level_font_size = LEVEL_FONT_SIZE
        self.title_font_size = TITLE_FONT_SIZE
        if not height:
            self.height = self.calc_height()
        
    #----------------------------------------------------------------------
    
    def resize_date_to_fit(self, text, font, font_size, width = HEADER_WIDTH, percentage_margin = 0.75):

        while (stringWidth(text,font,font_size) > width * percentage_margin):
            font_size = font_size - 1
            
        return font_size
        
    
    def calc_height(self):
        POINT_TO_MM = 1
        MARGIN_PERCENTALE = 1.5
        
        total_height = (bool(self.date)*self.date_font_size + bool(self.title)*self.title_font_size + bool(self.level)*self.level_font_size) 
        total_height = POINT_TO_MM * total_height
        total_height = MARGIN_PERCENTALE * total_height
        return total_height
        
    
    def draw(self):
        """
        Draw the shape, text, etc
        """
        ## TODO resize font if too wide
        self.date_font_size = self.resize_date_to_fit(self.date,DATE_FONT,self.date_font_size)


        
        #resize date if it is too long for container
        
        
        bracket_width = 5*mm
        
        self.canv.setLineWidth(3)

        offset = 0.5 #needed to suqare up corners
        #verticle members
        self.canv.line(self.x, self.y-offset, self.x, self.y+self.height+offset)
        self.canv.line(self.x+self.width, self.y-offset, self.x+self.width, self.y+self.height+offset)
        
        self.canv.setLineWidth(1)
        #left horozontal
        self.canv.line(self.x, self.y, self.x+bracket_width, self.y)
        self.canv.line(self.x, self.y+self.height, self.x+bracket_width, self.y+self.height)
        
        #right horozontal
        self.canv.line(self.x+self.width, self.y, self.x+self.width-bracket_width, self.y)
        self.canv.line(self.x+self.width, self.y+self.height, self.x+self.width-bracket_width, self.y+self.height)
        
        #DATE STYLE
        self.canv.setFont(DATE_FONT,self.date_font_size)
        self.canv.setFillColor(DATE_FONT_COLOR)
        
        self.canv.drawCentredString( self.width/2, self.y+self.height-self.date_font_size, self.date.upper())
        
        #LEVEL STYLE
        self.canv.setFont(LEVEL_FONT, self.level_font_size)
        self.canv.setFillColor(LEVEL_FONT_COLOR)
        level_y_pos = self.y+(self.height/2) - LEVEL_FONT_SIZE * POINT_TO_MM
        if(self.level=="S"):
            self.canv.drawCentredString(self.width/2, level_y_pos, "SOLEMNITY")
        elif self.level == "F":
            self.canv.drawCentredString(self.width/2, level_y_pos, "FEAST")
        elif self.level == "M":
            self.canv.drawCentredString(self.width/2, level_y_pos, "MEMORIAL")
        elif self.level == "m":
            self.canv.drawCentredString(self.width/2, level_y_pos, "OPTIONAL MEMORIAL")
            
        #TITLE STYLE
        self.canv.setFont("MinionSub", 8)
        self.canv.setFillColor(black)
        self.canv.drawCentredString(self.width/2, self.y+self.title_font_size, self.title)
        
HOUR_FONT = "MinionSub_bold"
HOUR_FONT_SIZE = 10
HOUR_FONT_COLOR = MAGNIFICAT_RED
class HourHeader(Flowable):
    """
    Draw a header for the hour, center bolded, red text
    
                                            
    |                                               |
    |              Evening Prayer II                |
    
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, hour = ""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.hour = hour
        self.hour_font_size = self.resize_font_to_fit(self.hour,HOUR_FONT,HOUR_FONT_SIZE,self.width)
        
        if not height:
            self.height = self.calc_height()
        else:
            self.height = height
        
    #----------------------------------------------------------------------
    
    def resize_font_to_fit(self, text, font, font_size, width = HEADER_WIDTH, percentage_margin = 0.75):

        while (stringWidth(text,font,font_size) > width * percentage_margin):
            font_size = font_size - 1
            
        return font_size
        
    
    def calc_height(self):
        POINT_TO_MM = 1
        MARGIN_PERCENTALE = 2
        
        total_height = (bool(self.hour)*self.hour_font_size ) 
        total_height = POINT_TO_MM * total_height
        total_height = MARGIN_PERCENTALE * total_height
        return total_height
        
    
    def draw(self):
        """
        Draw the shape, text, etc
        """
     
        
        
        #DATE STYLE
        self.canv.setFont(HOUR_FONT,self.hour_font_size)
        self.canv.setFillColor(HOUR_FONT_COLOR)

        self.canv.drawCentredString( self.width/2, self.y+self.height-self.hour_font_size, self.hour)
        
#H1 is the first header, should there be multiple antiphons for the psalm, eg. Easter, Christmas...
ANT_H1_FONT = "MinionSub_bold"
ANT_H1_FONT_SIZE = 8
ANT_H1_FONT_COLOR = MAGNIFICAT_RED
# this is the text of the antiphon itself
ANT_1_FONT = "MinionSub_bold"
ANT_1_FONT_SIZE = 8
ANT_1_FONT_COLOR = black

#H2 is the subsequent headers, should there be multiple antiphons for the psalm, eg. Easter, Christmas...
ANT_H2_FONT = "MinionSub_bold"
ANT_H2_FONT_SIZE = 7
ANT_H2_FONT_COLOR = MAGNIFICAT_RED
ANT_H2_INDENT = 4*mm
# this is the text of the antiphon itself
ANT_2_FONT = "MinionSub_bold"
ANT_2_FONT_SIZE = 7
ANT_2_FONT_COLOR = black
class Antiphon(Flowable):

    """
    antiphon(s) for the psalms, for multiple, pass a list of tuples
        eg. [("Easter","Alleluia, He is Risen"),("Lent","Let us take up our cross")...]
    
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, antiphon = "", number=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        
        self.multiple_antiphons = len(antiphon)>1

        self.antiphon = antiphon

        if not height:
            self.height = 0
        else:
            self.height = height
            
        self.paragraphs = self.build_paragraphs()
        
        
    def build_paragraphs(self):
        from MagnificatTextStyle import ANTIPHON_PARA_STYLE
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import ParagraphStyle

        paragraphs = []
        for a in self.antiphon:
            
            if self.antiphon.index(a) == 0:
                antiphon_string = "<font color='#D63254'>"+a[0]+'</font> '+a[1]
                P=Paragraph(antiphon_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=10,textColor = black, fontSize=8))
                ant_width = HEADER_WIDTH
            else:
                antiphon_string = "<para leading=7 size=6> <font color='#D63254'>"+a[0]+"</font> "+a[1]+"</para>"
                P=Paragraph(antiphon_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=10,textColor = black, fontSize=8))
                ant_width = HEADER_WIDTH - ANT_H2_INDENT
            w,h = P.wrap(HEADER_WIDTH, 99999)
            self.height = self.height+h
            paragraphs.append((w,h,P))
        return paragraphs
    def draw(self):
        """
        Draw the shape, text, etc
        """
        current_y = self.y+self.height
        for i in range(len(self.antiphon)):

            if i==0:
            
                #self.canv.setFont(ANT_H1_FONT,ANT_H1_FONT_SIZE)
                #self.canv.setFillColor(ANT_H1_FONT_COLOR)
                #self.canv.drawString( self.x, current_y, self.antiphon[i][0])
                
                
                self.paragraphs[i][2].drawOn(self.canv,self.x,current_y-self.paragraphs[i][1] +ANT_1_FONT_SIZE )
                current_y = current_y - self.paragraphs[i][1]
                
            else:
                #self.canv.setFont(ANT_H2_FONT,ANT_H2_FONT_SIZE)
                #self.canv.setFillColor(ANT_H2_FONT_COLOR)
                #self.canv.drawString( self.x + ANT_H2_INDENT, current_y, self.antiphon[i][0])
                ant_width = stringWidth(self.antiphon[i][0],ANT_H2_FONT,ANT_H2_FONT_SIZE)
                self.paragraphs[i][2].drawOn(self.canv,self.x+ANT_H2_INDENT,current_y-self.paragraphs[i][1] +ANT_2_FONT_SIZE )
                current_y = current_y - self.paragraphs[i][1]
                
               
                
                
class Psalm(Flowable):
    """
    psalm
    Psalm(verse = "Psalm 119:105-112", 
                                 titles = ["XIV (Nun)","A Meditation on God's Law"], 
                                 summary="This is my commandment: that you should love one another", 
                                 summary_verse = "(John 15:12)", 
                                 text
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, verse = "", titles=[], summary="",summary_verse="",text=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        
        self.verse = verse
        self.titles = titles
        self.summary = summary
        self.summary_verse = summary_verse
        self.text = text
        
        if not height:
            self.height = 0
        else:
            self.height = height
            
        self.paragraphs = self.build_paragraphs()
        
        
    def build_paragraphs(self):
        from MagnificatTextStyle import PSALM_PARA_STYLE
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import ParagraphStyle
        paragraphs = []

        #title
        psalm_string = "<para align='center'><b>"+self.verse+"</b></para>"
        P=Paragraph(psalm_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=10,textColor = MAGNIFICAT_RED, fontSize=9))
        P.keepWithNext = True
        psalm_width = HEADER_WIDTH
        w,h = P.wrap(HEADER_WIDTH, 99999)
        self.height = self.height+h
        paragraphs.append((w,h,P))
        
        psalm_string = "<para align='center'>"
        for t in self.titles:
            psalm_string += t+" -  "
        psalm_string = psalm_string[:-3] #remove trailing dash
        psalm_string+="</para>"
        P=Paragraph(psalm_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=10,textColor = MAGNIFICAT_RED, fontSize=8))
        P.keepWithNext = True
        psalm_width = HEADER_WIDTH
        w,h = P.wrap(HEADER_WIDTH, 99999)
        self.height = self.height+h
        paragraphs.append((w,h,P))
        
        #summary string
        psalm_string = "<para align=right fontsize=6><i>"+self.summary+"</i>"+"  "+self.summary_verse+"<br /></para>"
        P=Paragraph(psalm_string,PSALM_PARA_STYLE)
        
        P.keepWithNext = True #does not always keep together if near end of page
        psalm_width = HEADER_WIDTH
        w,h = P.wrap(HEADER_WIDTH, 99999)
        self.height = self.height+h
        paragraphs.append((w,h,P))

        #psalm itself
        psalm_stanzas = self.text.split("<br /><br />")
        paragraph_staging=[]
        for stanza in psalm_stanzas:
            psalm_string = "<para>"+stanza+"<br /><br /></para>"
            P=Paragraph(psalm_string,ParagraphStyle(name='Psalm',fontName = 'Minion_med',leading=7,textColor = black, fontSize=8))
            psalm_width = HEADER_WIDTH
            w,h = P.wrap(HEADER_WIDTH, 99999)
            self.height = self.height+h
            paragraph_staging.append((w,h,P))
        for p in paragraph_staging:
            
            stanza_height=0

            stanza_height = p[1]
            paragraphs.append((0,0,CondPageBreak(stanza_height)))
            paragraphs.append(p)
        
        
        return paragraphs
        
    def draw(self):
        """
        Draw the shape, text, etc
        """
        current_y = self.y+self.height

        for i in range(len(self.paragraphs)):
            
            self.paragraphs[i][2].drawOn(self.canv,self.x,current_y-self.paragraphs[i][1] +ANT_2_FONT_SIZE )
            current_y = current_y - self.paragraphs[i][1]
            
class Reading(Flowable):
    """
    Reading                   Gen 1:1
    ---------------------------------
        In the begining....
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, book="",verse = "",text=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        
        self.verse = verse
        self.book = book
        self.text = text
        
        if not height:
            self.height = 0
        else:
            self.height = height
            
        self.paragraphs = self.build_paragraphs()
        
        
    def build_paragraphs(self):
        from MagnificatTextStyle import PSALM_PARA_STYLE
        from reportlab.platypus import Paragraph, TableStyle

        from reportlab.lib.styles import ParagraphStyle
        
        paragraphs = []

        #title
        title_1 = "<para><b>READING</b></para>"
        title_2 = "<para align=right>"+self.book+" "+self.verse+"</para>"
        
        P1=Paragraph(title_1,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=10,textColor = MAGNIFICAT_RED, fontSize=10))
        P2=Paragraph(title_2,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=8,textColor = MAGNIFICAT_RED, fontSize=8))
        
        psalm_width = HEADER_WIDTH
        w,h = P1.wrap(HEADER_WIDTH, 99999)
        w,h = P2.wrap(HEADER_WIDTH, 99999)
        
        T = Table([[P1,P2]])
        T.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
        
        w,h = T.wrap(HEADER_WIDTH,999999)
        self.height = self.height + h
        print("h1:",self.height)
        paragraphs.append((w,h,T))
        
        #horozontal line

        line = HRFlowable(
            color=MAGNIFICAT_RED,
            thickness=1,
            width=HEADER_WIDTH,
            spaceBefore=1,
            spaceAfter=0
        )
        w,h = line.wrap(HEADER_WIDTH,999999)
        self.height = self.height + h
        print("h2:",self.height)
        paragraphs.append((self.width,3,line))
        #summary string
        
        #dropcap
        reading_string = "<para align=right >"+self.text[0]+"</para>"
        P=Paragraph(reading_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=20,textColor = MAGNIFICAT_RED, fontSize=20))
        w,h = P.wrap(HEADER_WIDTH, 99999)
        
        # first two lines
        table_width = HEADER_WIDTH /2 - 1
        FONT_SIZE=8
        para_lines=999
        P2 = None
        # create two line paragraph
        substring = self.text[1:-1]
        while para_lines >  (FONT_SIZE) *2 :
            substring = substring.rsplit(' ', 1)[0]
            reading_string = "<para align=left >"+substring+"</para>"
            P2=Paragraph(reading_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=8,textColor =black, fontSize=FONT_SIZE))
            w,h = P2.wrap(table_width, 99999)
            para_lines = h
            
        
        #remainder
        reading_string = "<para align=left >"+self.text[len(substring)+1:-1]+"<br /></para>"
        P3=Paragraph(reading_string,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=8,textColor =black, fontSize=FONT_SIZE))
        w,h = P3.wrap(HEADER_WIDTH, 99999)
        
        
        T2=Table([[P,P2],[P3,0]])
        #T=Table([["1","2"],["3","4"]])
        T2.setStyle(TableStyle([('SPAN', (0, 1), (1, 1)),
        #('GRID', (0, 0), (-1, -1), 0.25, black),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (0,0), 3),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,1), (1,1), 5)]))
        
        w,h = T2.wrap(HEADER_WIDTH,999999)
        self.height+=h
        print("h3:",self.height)
        paragraphs.append((w,h,T2))

       
        return paragraphs
        
    def draw(self):
        """
        Draw the shape, text, etc
        """
        current_y = self.y+self.height

        for i in range(len(self.paragraphs)):
            
            self.paragraphs[i][2].drawOn(self.canv,self.x,current_y-self.paragraphs[i][1] +ANT_2_FONT_SIZE )
            current_y = current_y - self.paragraphs[i][1]
            
class Intercessions(Flowable):
    """
    Reading                   Gen 1:1
    ---------------------------------
        In the begining....
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, first="",response="",intercessions = []):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        
        self.first=first
        self.intercessions = intercessions
        self.response = response
        
        if not height:
            self.height = 0
        else:
            self.height = height
            
        self.paragraphs = self.build_paragraphs()
        
        
    def build_paragraphs(self):
    
        from reportlab.platypus import Paragraph, TableStyle

        from reportlab.lib.styles import ParagraphStyle
        
        paragraphs = []

        #title
        title_1 = "<para><b><i>Intercessions</i></b></para>" 
        P1=Paragraph(title_1,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=10,textColor = MAGNIFICAT_RED, fontSize=10))
        w,h = P1.wrap(HEADER_WIDTH, 99999)        
        self.height = self.height + h
        paragraphs.append((w,h,P1))
        
        #first
        title_1 = "<para>"+self.first+"</para>" 
        P1=Paragraph(title_1,ParagraphStyle(name='Psalm',fontName = 'Minion_med',leading=8,textColor = black, fontSize=8))
        w,h = P1.wrap(HEADER_WIDTH, 99999)        
        self.height = self.height + h
        paragraphs.append((w,h,P1))
            
        #resp
        title_1 = "<para><i>"+self.response+"</i></para>" 
        P1=Paragraph(title_1,ParagraphStyle(name='Psalm',fontName = 'Minion',leading=8,textColor = black, fontSize=8))
        w,h = P1.wrap(HEADER_WIDTH, 99999)        
        self.height = self.height + h
        paragraphs.append((w,h,P1))
        
        for i in self.intercessions:
            title_1 = "<para>"+i[0]+"<br /> - "+i[1]+"</para>" 
            P1=Paragraph(title_1,ParagraphStyle(name='Psalm',fontName = 'Minion_med',leading=8,textColor = black, fontSize=8))
            w,h = P1.wrap(HEADER_WIDTH, 99999)        
            self.height = self.height + h
            paragraphs.append((w,h,P1))
        


       
        return paragraphs
        
    def draw(self):
        """
        Draw the shape, text, etc
        """
        current_y = self.y+self.height

        for i in range(len(self.paragraphs)):
            
            self.paragraphs[i][2].drawOn(self.canv,self.x,current_y-self.paragraphs[i][1] +ANT_2_FONT_SIZE )
            current_y = current_y - self.paragraphs[i][1]
                                    