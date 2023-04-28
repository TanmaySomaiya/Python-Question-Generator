#for generating semester exam paper
#initial criteria
#to generate Q4 main question having 4 questions in them

 
import mysql.connector #import inbuit module mysql.connector
import random #import inbuilt module random


#class connection maker to establish connection
class connection_maker:

    #types of exam 
    # internal and end semester
    internal="Internal Exam"
    ESE="End Semester Exam"

    #to store host name
    host=""

    #to store user name
    user=""

    #to store password for the user 
    password=""
    
    #stores name of database to access 
    database=""

    result=[]
    questions_per_question=4
    
    #table name for each unit
    unit_1_table_name=""    #table name for unit 1
    unit_2_table_name=""    #table name for unit 2
    unit_3_table_name=""    #table name for unit 3
    unit_4_table_name=""    #table name for unit 4

#function to establish connection 
#host user password and database to access
    def connection_establisher(cls):

        #stores values in class variables 
        cls.host=input("Enter Host: ") 
        cls.user=input("Enter user: ")
        cls.password= input("Enter your password: ")
        cls.database=input("Enter database to access: ")
       
#functions to take input from user for name of unit tables  

#unit 1
    def table_to_access_unit_1(cls):
        cls.unit_1_table_name=input("UNIT_1 Table name: ")

#unit 2 
    def table_to_access_unit_2(cls):
        cls.unit_2_table_name=input("UNIT_2 Table name: ")

#unit 3   
    def table_to_access_unit_3(cls):
        cls.unit_3_table_name=input("UNIT_3 Table name: ")

#unit 4
    def table_to_access_unit_4(cls):
          cls.unit_4_table_name=input("UNIT_4 Table name: ")

#function to genetate questions for unit 1
    def unit1_generator(cls): #ttakes all the value which are stored in class variables
        #msql.connector.connect establishes connection with the credintials
        mydb=mysql.connector.connect(
              host=cls.host, 
              user=cls.user,
              password=cls.password,
              database=cls.database
            )
        
        #cursor to execute sql statements 
        mycursor = mydb.cursor()

        #.execute to execute the given query
        mycursor.execute("SELECT questions FROM {0}".format(cls.unit_1_table_name))
       
        #store in the form of list using fetchall()
        cls.result = mycursor.fetchall()
        
        #for loop which will run from 1 to defined value of questions per question + 1
        for i in range(1,cls.questions_per_question+1):
            random_row = random.choice(cls.result) #storing a choice in tuple from questions stored in variable result(list)
            cls.result.remove(random_row) #remove the selected choice from the list
            
            for i in random_row:
                print("Q. "+i) #print questions
        print("\n")
            #print(random_row)
            #random_cell = random_row[0]
           
    
    def unit2_generator(cls):
        mydb=mysql.connector.connect(
              host=cls.host,
              user=cls.user,
              password=cls.password,
              database=cls.database
            )
        #print("Connection Established \n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT question FROM {0}".format(cls.unit_2_table_name))
        cls.result = mycursor.fetchall()
        
        for i in range(1,cls.questions_per_question+1):
            random_row = random.choice(cls.result)
            cls.result.remove(random_row)
            for i in random_row:
                print("Q. "+i)
        print("\n")

    def unit3_generator(cls):
        mydb=mysql.connector.connect(
              host=cls.host,
              user=cls.user,
              password=cls.password,
              database=cls.database
            )
       # print("Connection Established \n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT question FROM {0}".format(cls.unit_3_table_name))
        cls.result = mycursor.fetchall()
        for i in range(1,cls.questions_per_question+1):
            random_row = random.choice(cls.result)
            cls.result.remove(random_row)
            for i in random_row:
                print("Q. "+i)
        print("\n")

    def unit4_generator(cls):
        mydb=mysql.connector.connect(
              host=cls.host,
              user=cls.user,
              password=cls.password,
              database=cls.database
            )
       #2 print("Connection Established \n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT question FROM {0}".format(cls.unit_4_table_name))
        cls.result = mycursor.fetchall()
        
        for i in range(1,cls.questions_per_question+1):
            random_row = random.choice(cls.result)
            cls.result.remove(random_row)
            for i in random_row:
                print("Q. "+i)
        print("\n")

#function to prefer examination type
    def examination_type(cls):
        print("Generating Question Paper for?")
        print('''1. Internal Exam
2. End Semester Exam''')
        user_input=input(">>")

#if input==2 
        if(user_input== "2"):
            MAR2023=connection_maker()
            MAR2023.connection_establisher() 
            MAR2023.table_to_access_unit_1()
            MAR2023.table_to_access_unit_2()
            MAR2023.table_to_access_unit_3()
            MAR2023.table_to_access_unit_4()
            
            MAR2023.unit1_generator()
            MAR2023.unit2_generator()
            MAR2023.unit3_generator()
            MAR2023.unit4_generator()
        else:
            MAR2023=connection_maker()
            MAR2023.connection_establisher()
            MAR2023.table_to_access_unit_1()
            MAR2023.table_to_access_unit_2()
            MAR2023.unit1_generator()
            MAR2023.unit2_generator()
            
        
test=connection_maker()
test.examination_type()
#MAR2023=connection_maker()
#MAR2023.connection_establisher()
#MAR2023.table_to_access()
#MAR2023.unit1_generator()
#MAR2023.unit2_generator()
#MAR2023.unit3_generator()
#MAR2023.unit4_generator()


   
