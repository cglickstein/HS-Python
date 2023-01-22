# Radioactive decay
cobalt = 10

for year in range(0,5):
    m = cobalt* .12
    cobalt = cobalt - m #why not 10-m?
print (cobalt)
#add up all things printed

remain = round (cobalt, 2)
print ("The amount of cobalt remaining after 5 years is", remain, "grams")



