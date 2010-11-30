
def get(query):
    import httplib
    conn = httplib.HTTPConnection("www.informatik.hs-mannheim.de")
    conn.request("GET", query)
    r1 = conn.getresponse()
    data = r1.read()
    return data

def get_studiengaenge_from_server():
    return get("/stundenplan/my_splan.php")

def get_query_from_server(query):
    return get("/stundenplan/my_splan.php?" + query)