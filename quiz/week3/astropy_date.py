 

from astropy.time import Time

def print_modified_julian_date():

  #define a date

  s = '2022-03-14T15:09:26.53589793Z'

  #create an astropy time object

  t = Time(s)

  #print the modified Julian date

  print(t.mjd)

def main():

  #print a modified julian date

  print_modified_julian_date()

#run the program

if __name__=="__main__":

  main()