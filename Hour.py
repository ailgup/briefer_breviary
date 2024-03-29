import json
# Hour class, is loaded with all the needed data, used as a go-between the db and the pdf
class Breviary:
    OFFICE_OF_READINGS = "Office of Readings"
    MORNING_PRAYER = "Morning Prayer"
    DAYTIME_PRAYER = "Daytime Prayer"
    EVENING_PRAYER = "Evening Prayer"
    NIGHT_PRAYER = "Night Prayer"
    HOURS = [OFFICE_OF_READINGS, MORNING_PRAYER, DAYTIME_PRAYER, EVENING_PRAYER, NIGHT_PRAYER]
    HOUR_ABBREVIATIONS = ["or","mp","dp","ep","np"]

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    DAYS = [SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]


    Antiphon = {"title": "", "ant": ""}
    Psalm = {"titles": [], "verse": "", "summary": "", "summary_verse": "", "text": ""}
    Reading = {"verse": "", "text": ""}
    Response = {"verse": "", "response": ""}
    Intercessions = {"first": "", "response": "", "intercessions": []}  # intercessions is list of Responses
    Hymn = {"name": "", "number": "", "saint_michaels_num": "", "in_ibrev": ""}

class Antiphon:
    
    def __init__(self):
        self.title = None
        self.ant = None
    def __init__(self, title, ant):
        self.title = title
        self.ant = ant
    def __str__(self):
        return f"Antiphon({self.title}, {self.ant})"
class Psalm:
    
    def __init__(self):
        self.titles = []
        self.verse = None
        self.summary=None
        self.summary_verse=None
        self.text = None
    def __init__(self, titles,verse,summary,summary_verse ,text):
        self.titles = titles
        self.verse = verse
        self.summary=summary
        self.summary_verse=summary_verse
        self.text = text
    def __init__(self, psalm_obj):
        self.titles = psalm_obj["psalm_number"]
        self.verse = psalm_obj["descriptor"]
        self.summary=psalm_obj["scripture_verse"]
        self.summary_verse=psalm_obj["scripture_verse_author"]
        self.text = psalm_obj["psalm_text"]
    def toJSON(self):
        return {"titles": titles, "verse": self.verse, "summary": self.summary, "summary_verse": self.summary_verse, "text": self.text}
    def __str__(self):
        return f"Psalm({self.titles}, {self.verse},{self.summary},{self.summary_verse},{self.text})"   
    
class Hour:
    def __init__(self):
        # this is the canonical variable_names should be used everythere!
        self.week = 0
        self.week_roman = ""
        self.day = ""
        self.hour = ""
        self.invitatory = [] #List of Antiphon type
        self.hymn = []  # List of Hymn type
        self.ant_1 = []  # List of Antiphon type
        self.ant_2 = []
        self.ant_3 = []
        self.ps_1 = Breviary.Psalm
        self.ps_2 = Breviary.Psalm
        self.ps_3 = Breviary.Psalm
        self.reading = Breviary.Reading
        self.response = []  # List of Response type
        self.canticle_ant = []  # List of Antiphon type
        self.intercessions = Breviary.Intercessions
        self.prayer = []  # List of Strings

    def process_row(self, row):
        pass
        
#stolen from https://bobbyhadz.com/blog/python-typeerror-object-of-type-bytes-is-not-json-serializable
class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        return json.JSONEncoder.default(self, obj)
        


def fetch_rows_mysql(table="four_week"):
    import mysql.connector
    import json
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="briefer"
    )
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM "+table)

    myresult = mycursor.fetchall()
    print (myresult)

    #js = json.dumps(myresult, cls=BytesEncoder)
    #js = json.loads(js)
    js = [ json.loads( row["json_stuff"] ) for row in myresult ]
    
    print(js)
    return js
      
def fetch_rows(table="four_week"):
    import psycopg2
    import psycopg2.extras
    rows = []
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Pa88w0rd")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM " + table +" ORDER BY \"id\"")
        for row in cur:
            rows.append(row)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return rows


def process_row(row):
    h = Hour()
    print("\n\nH:\n",row,type(row))
    
    h.week = row["week"]
    if row["week"] == 1:
        h.week_roman = "I"
    elif row["week"] == 2:
        h.week_roman = "II"
    elif row["week"] == 5:
        h.week_roman = "III"
    elif row["week"] == 4:
        h.week_roman = "IV"

    h.day = row["day"]
    h.hour = row["hour"]

    h.invitatory = row["invitatory"]
    h.hymn = row["hymn"]
    
    print (h.hymn)
    
    h.ant_1 = row["ant_1"]
    h.ant_2 = row["ant_2"]
    h.ant_3 = row["ant_3"]
    h.ps_1 = row["ps_1"]
    h.ps_2 = row["ps_2"]
    h.ps_3 = row["ps_3"]

    h.reading = row["reading"]

    h.response = row["response"]
    h.canticle_ant = row["canticle_ant"]

    h.intercessions = row["intercessions"]
    h.prayer = row["prayer"]

    return h
