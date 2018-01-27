from datetime import datetime
s1 = 'Sun 10 May 2015 13:54:36'
s2 = 'Sun 10 May 2015 13:54:36' # for example
#Day dd Mon yyyy hh:mm:ss +xxxx
FMT = '%a %d %b %Y %H:%M:%S'
tdelta = datetime.strptime(s1, FMT) #- datetime.strptime(s1, FMT)
print (tdelta)