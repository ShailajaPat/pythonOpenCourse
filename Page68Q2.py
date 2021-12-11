# Write a class that has the following attributes
#       classification
#       justification
#       selector
# Provide default values for each attribute (consider using None) 
# Make it so that when you print it, you can display all of the attirbutes and
# their values nicely
# Soemthing like this should work -
# query1 = Query("TS//SJ//REL TO USA, EVEY", "Primary email address of Zendian diaplomat", "ileona@stato.gov.zd") 
# print(query1)
## Change the Query class to accept a list of selectors rather than a single selector. Make sure you can still print everything ok.

class Query(object):
     selector = []
     def __init__(self, classi, justi, selecti):
          self.classification = classi
          self.justification = justi
          self.selector = self.selector + selecti
          
     def __str__(self):
          return "Classification: {0}\n Justification: {1}\n Selector: {2}\n".format(self.classification, self.justification, self.selector)

     def __repr__(self):
          return "Query('{0}','{1}','{2}')".format(self.classification,self.justification, self.selector)

# main
shailaja = Query("shailaja patil", "Mobile number", ["9850799803","9767962142"])
print(shailaja)

query1 = Query("TS//SJ//REL TO USA, EVEY", "Primary email address of Zendian diaplomat", ["ileona@stato.gov.zd"]) 

print(query1)
