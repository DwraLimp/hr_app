import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dwra1998!!"
    #database = "HR"
    
)

DB_NAME = "HR.employees" # the name of the created database

class Employee:
    
    def __init__(self, kwdikos, onoma, email, tel, dieuthinsi, misthos):
        self.kwdikos = kwdikos
        self.onoma = onoma
        self.email = email
        self.tel = tel
        self.dieuthinsi = dieuthinsi
        self.misthos = misthos
   
    def __str__(self):
        sstr = "Ypallilos - Kwdikos: "+str(self.kwdikos)+" ,Onoma: "+self.onoma+ " ,email:"+self.email+ \
        " ,Tel: "+self.tel+" ,dieuthinsi: "+self.dieuthinsi+" ,Misthos: "+self.misthos
        return sstr
    
################################ Functions definition #######################
        
def Prosthiki_upallhloy(): 
  
    kwdikos = int(input("Dwse kwdiko upallhloy:"))
    onoma = input("Dwse onoma upallhloy:")
    email = input("Dwse email:")
    tel = input("Dwse thlefono upallhloy:")
    dieuthinsi = input("Dwse dieuthinsi upallhloy:")
    misthos = input("Dwse misthos upallhloy:")
    
    return Employee(kwdikos, onoma, email, tel, dieuthinsi, misthos)


def epeksergasia_ypallilou(emp, cursor):
    
    choice= 0
    
    while choice != 5:
        
        print("*** Epeksergasia Ypallilou ***")
        print(emp)

        print("-------------------------------------------------------------")
        print("Dwste mia apo tis parakatw epiloges:")
        print("1:Onoma / 2:email / 3:tel / 4:dieuthinsi / 5:Eksodos")
        
        choice = int(input("Dwste arithmo:"))
        if choice == 1:
            emp.onoma = input("Dwste to kainourio onoma tou ypallilou: ")
            cursor.execute("UPDATE "+DB_NAME+" SET name = %s WHERE id = %s", (emp.onoma, emp.kwdikos))

            
        if choice == 2:
            emp.email = input("Dwste to kainourio email tou ypallilou: ")
            cursor.execute("UPDATE "+DB_NAME+" SET email = %s WHERE id = %s", (emp.email, emp.kwdikos))

            
        if choice == 3:
            emp.tel = input("Dwste to kainourio til tou ypallilou: ")
            cursor.execute("UPDATE "+DB_NAME+" SET tel = %s WHERE id = %s", (emp.tel, emp.kwdikos))

            
        if choice == 4:
            emp.dieuthinsi = input("Dwste to kainouria dieuthinsi tou ypallilou: ")
            cursor.execute("UPDATE "+DB_NAME+" SET address = %s WHERE id = %s", (emp.dieuthinsi, emp.kwdikos))

           
        if choice == 5:
            print("Eksodos epeksergasias")
            
    mydb.commit() # Insert record to the database     
    print("Oi allages kataxwrhuikan sthn DB")
    
    return emp

def diagrafi_ypallilou(emp, cursor):
    
    cursor.execute("DELETE FROM "+DB_NAME+" WHERE id = %s" %emp.kwdikos)
    mydb.commit() # Insert record to the database   
    return Employee(0,"","","","","")     


def anazitisi_ypallilou(emp, cursor):
    
     name = input("Epilekste onoma xrhsth : ") # Give username
     cursor.execute("SELECT * FROM "+DB_NAME+ " WHERE name = '%s'" %name) # search for the given username
     value = cursor.fetchone() # parse the record to the value
     if value != None: # if the record exist
         emp = Employee(*value)   # parse the choosen record to the Employee class
         print(emp)
     else:
         print("Den yparxei to onoma ",name," sthn DB")
     return emp
         
    
########################### Init variables ##################################   
epilogh = 0
emp = Employee(0,"","","","","")
cursor = mydb.cursor(buffered=True) # create cursor object
#############################################################################

while epilogh != 6:

    if epilogh == 1:
        print("*** Dwse stoixeia upallhloy ***")
        emp = Prosthiki_upallhloy()
        cursor.execute("INSERT INTO "+DB_NAME+" VALUES(%s,%s,%s,%s,%s,%s)",
                       (emp.kwdikos, emp.onoma,emp.email, emp.tel, emp.dieuthinsi, emp.misthos))
        mydb.commit() # Insert the new record to the database
        
    if epilogh == 2:
        print(emp) # Print the Eployee status
        
    if epilogh == 3:
        emp = epeksergasia_ypallilou(emp, cursor) # Edit the selected employee and add it to the database  
        
    if epilogh == 4:
        diagrafi = input("Eiste sigouros gia thn diagrafh ths kataxvrhshs ? (Y/N)")
        if diagrafi == "Y":
            emp = diagrafi_ypallilou(emp, cursor)
            print("H kataxwrhsh Diagrafike epitixws!!!")
        
    if epilogh == 5:
        emp = anazitisi_ypallilou(emp, cursor) # Choose Employee from the Database
        
    if epilogh == 6:
        print("Eksodos programatos")
        cursor.close() # close the DB connection

    print("-----------------------------------------------------------------")
    print("1. Prosthiki upallhloy : ")
    print("2. Provoli stoixeiwv upallhloy : ")
    print("3. Epeksergasia upallhloy : ")
    print("4. Diagrafh upallhloy  : ")
    print("5. Anazhthsh upallhloy : ")
    print("6. Eksodos")
        
    epilogh = int(input("Dwse epilogh :"))  # Give a selection 
    print("-----------------------------------------------------------------")