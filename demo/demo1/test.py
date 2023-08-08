import plistlib


def findDuplicates(fileName):
    print('Finding duplicate tracks in %s...' % fileName)
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    trackNames = {}
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            if name in trackNames:
                if duration // 1000 == trackNames[name][0] // 1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
            else:
                trackNames[name] = (duration, 1)
        except:
            pass
