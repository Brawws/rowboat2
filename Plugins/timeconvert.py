import datetime
import dateutil
from dateutil import parser
from dateutil import tz

def convert(time):
    local = dateutil.tz.gettz()
    utc = dateutil.tz.gettz('UTC')
    formatteddate = parser.parse(time)
    formatteddate = formatteddate.replace(tzinfo=utc)
    localtime = formatteddate.astimezone(local)
    localend = localtime.isoformat()
    localend = datetime.datetime.fromisoformat(localend)
    truelocal = localend.strftime('%b %d, %Y %I:%M:%S AM')
    return truelocal
