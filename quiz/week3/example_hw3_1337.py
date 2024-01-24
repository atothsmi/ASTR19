def read_file(filename):

  #open a file

  f = open(filename,'r')

  #return the lines in the file as a list

  return f.readlines()

def main():

  #define a filename

  fname = 'data_hw3.txt'

  #read in the data

  line_list = read_file(fname)

  #print some info to the screen

  print(line_list[2].split()[1])

if __name__=="__main__":

  main()