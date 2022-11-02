import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'recipedb')
mycursor = mydb.cursor()
while True:

    print("select an option from the menu")

    print("1 add recipe")

    print("2 view all recipe")  

    print("3 search a recipe")

    print("4 update the recipe")    

    print("5 delete a recipe")

    print("6 exit")

   

    choice = int(input('enter an option:'))

    if(choice==1):

        print('recipe enter selected')
        
        
        

        name = input('enter the name')

        category = input('enter the category')

        taste = input('enter the taste ')

        price = input('enter the price')
        
        
        
        sql = 'INSERT INTO `recipe`( `name`, `category`, `taste`, `price`) VALUES (%s,%s,%s,%s)'

        

        data = (name,category,taste,price)

        mycursor.execute(sql , data)

        mydb.commit()
        
        

    elif(choice==2):

        print('view recipe')
    
        
        sql = 'SELECT * FROM `recipe`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

        print('view recipe')

    elif(choice==3):

        print('search recipe')

    elif(choice==4):

        print('update recipe')

    elif(choice==5):

        print('delete recipe')

    elif(choice==6):

        break