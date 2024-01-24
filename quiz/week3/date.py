import datetime

def main():

  #define a date

  s = '2022-03-14T15:09:26Z'

  #format the date

  d = datetime.datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")

  #print the date and time

  print(d)

if __name__=="__main__":

  main()