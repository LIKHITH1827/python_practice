d={'a':
    {'li':
        {'height':6,'weight':64},
    'jai':
        {'height':7,'weight':70}},
   'b':
       {'ob':
           {'height':5,'weight':80},
       'kittu':
           {'height':8,'weight':56}}}



for sections,people_data in d.items():
    for people,qualities in people_data.items():
        for quality in qualities:
            print(quality)
            if qualities[quality]>7:
                print("very height")
            else:
                print("shorter")
        print(qualities)
    print("loop done")