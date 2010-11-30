

def get_from_server():
    import httplib
    conn = httplib.HTTPConnection("www.studentenwerk-mannheim.de")
    conn.request("GET", "/mensa/wo_hs.normal.php")
    r1 = conn.getresponse()
    data = r1.read()
    return data
