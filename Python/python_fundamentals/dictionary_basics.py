about_me = {}
about_me["name"] = "Sandy"
about_me["pet's name"] = "Beeker"
about_me["age"] = 36
about_me["hobby"] = "knitting"

def making_dicts():
    for key, val in about_me.items():
        print "My", key, "is", val

making_dicts()
