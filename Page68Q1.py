# Make RangedQuery class that inherits from Query and has additional attributes
#       begin date
#       end date
# For now, just make dates of format 'YYYY-MM-DD'
# Provide defaults for these attributes. Make sure you incorporate the Query
# class's initializer into RangedQuery initializer 
# Ensure that new class should print nicely
# query2 = RangedQuery("TS//SJ//REL TO USA, EVEY", "Primary email address of Zendian diaplomat", "ileona@stato.gov.zd","2016-12-01","2016-12-31") 
# print(query2)
#                
class Query(object):
     def __init__(self, classi, justi, selecti):
          self.classification = classi
          self.justification = justi
          self.selector = selecti
          
     def __str__(self):
          return "Classification: {0}\n Justification: {1}\n Selector: {2}\n".format(self.classification, self.justification, self.selector)

     def __repr__(self):
          return "Query('{0}','{1}','{2}')".format(self.classification,self.justification, self.selector)

class RangedQuery(Query):
     def __init__(self, classi, justi, selecti, sdate, edate):
          super(RangedQuery, self).__init__(classi, justi, selecti)
          self.begin_date = sdate
          self.end_date = edate

     def __str__(self):
          query_str = super(RangedQuery, self).__str__()
          return query_str + "State Date: {0}, End Date: {1}\n".format(self.begin_date, self.end_date)

     def __repr__(self):
          query_str = super(RangedQuery, self).__str__()
          return query_str + "RangedQuery('{0}','{1}')".format(self.start_date, self.end_date)
          
# main
shailaja = RangedQuery("shailaja patil", "Mobile number", "9850799803", "2019-01-01", "2019-01-31")
print(shailaja)

query1 = RangedQuery("TS//SJ//REL TO USA, EVEY", "Primary email address of Zendian diaplomat", "ileona@stato.gov.zd", "2019-03-01", "2019-03-31") 

print(query1)
