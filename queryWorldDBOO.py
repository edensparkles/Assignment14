'''
Eden Lawson
elawson1@binghamton.edu
C60
Assignment 14
Vlad Malcevic
'''

'''
This program finds the population of a city via database query
Output:
  query result (str)
  
Input:
  city (str)
  min_pop(int)
  max_pop(int)
Classes Used:
  BadArgument
  QueryWorldBDPopRange
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Missing Argument'
    self.__message = 'City is blank or contains invalid characters'

#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def get_title(self):
    return self.__title
  
##  
##  def is_valid_range(self, min_pop, max_pop):
##    if self.min_pop.isdigit() and self.max_pop.isdigit():
##      min_pop_int = int(self.min_pop
##      max_pop_int = int(self.max_pop)
##      return min_pop_int <= max_pop_int
    
  def get_answer(self):
    return self.__answer
    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDBPopRange:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, db_name):
    conn = sqlite3.connect(db_name)
    self.__cursor = conn.cursor()
    # Must make city instance variable so that it is accessible to all methods
##    self.__current_city = ""
    self.__min_pop = ''
    self.__max_pop = ''
    self.__answer = None
    
  def is_valid_range(self, min_pop, max_pop):
    return int(min_pop) <= int(max_pop)


# -- Mutators ----------------------------------------------------------------

  # 
  # param city_name (str)
##  def set_city(self, city_name):
##    self.__current_city = city_name
  
  def set_answer(self):
    self.__answer = self.__cursor.fetchall()
    
  def set_min_pop(self,min_pop):
    self.__min_pop = min_pop

  def set_max_pop(self, max_pop):
    self.__max_pop = max_pop


  # raises BadArgumenyt Exception if city is blank or contains invalid chars
  def pop_query(self):
##    if self.__current_city.replace('_','A').isalpha():
    if self.is_valid_range(self.__min_pop, self.__max_pop):
      self.__cursor.execute('select city FROM cities where \
population > ? and population < ? and population from city')
      answer = self.__set_answer(self.cursor)
        
    else:
      raise BadArgument()


  # Close connection to db
  def close_connection(self):
    self.__cursor.close()


# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    answer = self.__set_answer()
    
    finished_list = ""
    for atuple in answer:
      finished_list += "(", atuple[0], ",", atuple[1],")"
    return "%s" % (finished_list)
    # Note that if city isn't in database, then answer will be None
    # If city is in database, answer will be a tuple object
    # Will have to get element[0] of tuple in order to use it
    

    # Note that 4th format specifier denotes a string rather than an int in 
    # order to accommodate possibility that answer is None
##    return '%s %s %s %s\n' % (
##      ('The population of' if answer else 'There is no city named'),
##      self.__current_city,
##      ('is' if answer else 'in the database'),
##      ('' if answer == None else str(answer[0])) )
##  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
  
# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
def main():
  # set up connection and create cursor
  query = QueryWorldDBPopRange('worldDB')
  #query = QueryWorldDB('world.db')

  # get input from user (priming read)
  min_pop = input("Find cities by population\nEnter the min population, " + \
               "(Press <Enter> to quit):  ")
  
  # let user get as many results as desired
  while min_pop:
    max_pop = input("Enter the max population:  ")
    try:
      # set up and issue query
##      query.set_city(city.strip())
      query.set_min_pop(min_pop.strip())
      query.set_max_pop(max_pop.strip())
      query.pop_query()
      self.__set_answer()
      # show results
      print(self.__str__)
    except BadArgument as err:
      # city input empty or malformed
      print('\n%s: %s\n' % (err.get_title(), str(err) ))
       
    # let user enter another city (continuation read)
    min_pop = input("Find cities by population\nEnter the min population, " + \
               "(Press <Enter> to quit):  ")
    
  # close connection to db
  query.close_connection()

main()
                            
                            
                    
