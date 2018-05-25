from time import mktime

def date2milis(d):
    return (mktime(d.timetuple()) + d.microsecond / 1000000.0) * 1000.0 if d else None