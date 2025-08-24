#!/usr/bin/python
# Get Lap Averages for Centennial Lap Social on Strava
import logging
#import inspect
#print(inspect.getsource(logging))
import sys
import string
from stravalib import model, attributes, exc, unithelper as uh
import datetime 
from operator import itemgetter
from datetime import datetime, timedelta

def get_name(id):
    o = client.get_athlete(id)
    n =  o.firstname+" "+o.lastname
    return n

def lap_to_sec(laptime):
    seconds = (3600 * int(laptime.split(":")[0]))+(60 * int(laptime.split(":")[1]))+int(laptime.split(":")[2])
    return seconds

def sec_to_hms(sec):
    s = timedelta(seconds=int(sec))
    d = datetime(1,1,1) + s
    #print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
    return str(d.hour)+":"+str(d.minute)+":"+str(d.second)

if (len(sys.argv)==2):
    STORED_ACCESS_TOKEN=sys.argv[1]
else:
    sys.exit(sys.argv[0],"missing access token as only parameter")


from stravalib import Client
client = Client(access_token=STORED_ACCESS_TOKEN)
athlete = client.get_athlete() # Get current athlete details
print("Hello, {} {}, {} ".format(athlete.firstname, athlete.lastname, athlete.id))

rides_dict = []
activity_id = set()

CP_social = client.get_segment_efforts(2524690, athlete_id=athlete.id)
for lap in CP_social:
    #print "Activity for grouping ->",lap.activity.id
    #print "Lap start ->", lap.start_date
    #print "Lap time -> ", str(lap.start_date).split(" ")[1].split("+")[0]
    #print "Lap moving time ->", lap.moving_time
    epoch = lap.start_date.strftime('%s')
    #activity_id.add(lap.activity.id) #maybe not necessary set()
    rides_dict.append([epoch,lap.activity.id,str(lap.moving_time)])


rides_dict.sort(key=itemgetter(0))

last_activity_id=0
fastest_lap_all_time = []
fastest_lap_per_activity = []
average_laps=0
lap_count=0
average_laps_all_time = []

for f in rides_dict:
    if int(f[1]) == int(last_activity_id):
        #this is all the laps except first of laps in an activity
        #print "epoch",f[0],"activity id",f[1],"lap time",f[2]
        lap_in_seconds = lap_to_sec(f[2])
        if lap_in_seconds < fastest_lap_per_activity[0]:
            fastest_lap_per_activity[0] = lap_in_seconds
            fastest_lap_per_activity[1] = f[2]
        average_laps += lap_in_seconds
        print "    lap time",f[2]

    else:
        # first run on a new activity laps, so wrap up last summary and set all new variables
        if len(fastest_lap_per_activity) > 0:
            #just a way to see if we are on first loop
            print "Fastest Lap:", fastest_lap_per_activity[1]        
            print "Average Lap:", sec_to_hms(average_laps/lap_count)
            fastest_lap_all_time.append([fastest_lap_per_activity[1],activity.name,other_athletes])
            average_laps_all_time.append([(average_laps/lap_count),activity.name,other_athletes])
        print "==========================="

        activity = client.get_activity(f[1])
        print "Name:", activity.name

        #relations = client.get_related_activities(f[1])
        #print relations
        print "Other Athletes:",
        other_athletes = ""
        #for h in relations:
        #    print h.athlete.id, "Ride name:", h.name
        #    other_athletes += get_name(h.athlete.id)+","
        print other_athletes
        count = 0
        for g in rides_dict:
            if g[1] == f[1]:
                count += 1
        lap_count = count
        print "Laps:", count        

        #lap analysis
        #print "epoch",f[0],"activity id",f[1],"lap time",f[2], lap_to_sec(f[2])
        lap_in_seconds = lap_to_sec(f[2])
        fastest_lap_per_activity = []
        fastest_lap_per_activity.append(lap_in_seconds)
        fastest_lap_per_activity.append(f[2])
        average_laps=lap_in_seconds
        print "    lap time",f[2]
        last_activity_id = f[1]

if len(fastest_lap_per_activity) > 0:
    print "Fastest Lap:", fastest_lap_per_activity[1]
    print "Average Lap:", sec_to_hms(average_laps/lap_count)
    fastest_lap_all_time.append([fastest_lap_per_activity[1],activity.name,other_athletes])
    average_laps_all_time.append([(average_laps/lap_count),activity.name,other_athletes])


print ""
print "#####################"
print "Average Laps:"
for j,x,q in average_laps_all_time:
    print sec_to_hms(j),x,q
print "#####################"
print "Fastest Ever Laps:" 
for k,y,u in fastest_lap_all_time:
    print k,y,u
print ""
print ""

