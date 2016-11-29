from stravalib import Client
from stravalib import unithelper

client = Client(access_token='YourAccessToken')

athlete = client.get_athlete()
activities = client.get_activities(limit=9000)

print athlete.firstname
print athlete.lastname
print athlete.state
print athlete.email

atype = []
run = []
rundis = []
runelev = []
walk = []
walkdis = []
walkelev = []
ride = []
ridedis = []
rideelev = []
hike = []
hikedis = []
hikeelev = []
snowshoe = []
snowdis = []
snowelev = []

for a in activities:
    atype.append(a.type)

types = set(atype)
print types

for a in activities:
    if a.type == 'Run':
        run.append(a)
        rundis.append(float(unithelper.miles(a.distance)))
        runelev.append(float(unithelper.feet(a.total_elevation_gain)))
    elif a.type == 'Walk':
        walk.append(a)
        walkdis.append(float(unithelper.miles(a.distance)))
        walkelev.append(float(unithelper.feet(a.total_elevation_gain)))
    elif a.type == 'Ride':
        ride.append(a)
        ridedis.append(float(unithelper.miles(a.distance)))
        rideelev.append(float(unithelper.feet(a.total_elevation_gain)))
    elif a.type == 'Hike':
        hike.append(a)
        hikedis.append(float(unithelper.miles(a.distance)))
        hikeelev.append(float(unithelper.feet(a.total_elevation_gain)))
    elif a.type == 'Snowshoe':
        snowshoe.append(a)
        snowdis.append(float(unithelper.miles(a.distance)))
        snowelev.append(float(unithelper.feet(a.total_elevation_gain)))
    else:
        pass
print "Since May 6, 2014:\n"

def print_run():
    print str(len(run)) + " runs for a distance of " + str(
        round(sum(rundis), 2)) + " total miles and an average of " + str(round(sum(rundis) / (len(run)), 2)) + " miles per run"
    print "and a total elevation gain of " + str(
        round(sum(runelev), 2)) + " feet and an average elevation gain of " + str(round(
        sum(runelev) / (len(run)), 2)) + " per run. \n"

def print_walk():
    print str(len(walk)) + " walks for a distance of " + str(
        round(sum(walkdis), 2)) + " total miles and an average of " + str(round(
        (sum(walkdis)) / (len(walk)), 2)) + " miles per walk."
    print "and a total elevation gain of " + str(
        round(sum(walkelev), 2)) + " feet and an average elevation gain of " + str(round(
        sum(walkelev) / (len(walk)), 2)) + " per walk.\n"

def print_ride():
    print str(len(ride)) + " rides for a distance of " + str(
        round(sum(ridedis), 2)) + " total miles and an average of " + str(round(
        (sum(ridedis)) / (len(ride)), 2)) + " miles per ride."
    print "and a total elevation gain of " + str(
        round(sum(rideelev), 2)) + " feet and an average elevation gain of " + str(round(
        sum(rideelev) / (len(ride)), 2)) + " per ride.\n"

def print_hike():
    print str(len(hike)) + " hikes for a distance of " + str(
        round(sum(hikedis), 2)) + " total miles and an average of " + str(round(
        (sum(hikedis)) / (len(hike)), 2)) + " miles per hike."
    print "and a total elevation gain of " + str(
        round(sum(hikeelev), 2)) + " feet and an average elevation gain of " + str(round(
        sum(hikeelev) / (len(hike)), 2)) + " per hike.\n"
def print_snow():
    print str(len(snowshoe)) + " snowshoe for a distance of " + str(
        round(sum(snowdis), 2)) + " total miles and an average of " + str(round(
        (sum(snowdis)) / (len(snowshoe)), 2)) + " miles per snowshoe."
    print "and a total elevation gain of " + str(
        round(sum(snowelev), 2)) + " feet and an average elevation gain of " + str(round(
        sum(snowelev) / (len(snowshoe)), 2)) + " per snowshoe.\n"

if len(run) > 0:
    print_run()
if len(walk) > 0:
    print_walk()
if len(ride) > 0:
    print_ride()
if len(hike) > 0:
    print_hike()
if len(snowshoe) > 0:
    print_snow()

totalMiles = []
totalElev = []

for d in activities:
    totalMiles.append(float(unithelper.miles(d.distance)))
    totalElev.append(float(unithelper.feet(d.total_elevation_gain)))

print "Total miles = " + str(round(sum(totalMiles), 2))
print "Total elevation gain = " + str(round(sum(totalElev), 2))
