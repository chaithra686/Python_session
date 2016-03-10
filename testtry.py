



#!/usr/bin/env python

import MySQLdb
import csv
import collections

def main():
        connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
        mysql_cursor=connection.cursor()
        mysql_cursor.execute("select p.id,p.fullname,up.unresolved_party_type_name,m.id from party as p inner join party_unresolved_party_type_map as m on p.id=m.party_id inner join unresolved_party_type as up on m.unresolved_party_type_id=up.id order by p.id")
        result_set = mysql_cursor.fetchall()
#       print result_set
#        for row in result_set:
 #               print row



        counter = collections.defaultdict(int)

        i=0
        for i in result_set:
                i += 1

        f= open("try2.csv","wb")
        fwriter = csv.writer(f,quoting=csv.QUOTE_ALL)
        fwriter.writerow(['ID','Full name','party type','map id'])



        for i in result_set:
                if i <= 1000:
        #               f= open("try.csv","wb")
        #               fwriter = csv.writer(f,quoting=csv.QUOTE_ALL)
        #               fwriter.writerow(['ID','Full name','party type','map id'])

                        fwriter.writerow(result[i])
        f.close()
        return 0


if __name__ == '__main__':
         main()

