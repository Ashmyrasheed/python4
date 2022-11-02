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
    print("6 total price of food")
    print("7 total price for each category")

    print("8 exit")

   

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
        
        category = input('enter category to search')
        
        sql = "SELECT `id`,`name`,`category`,`taste`,`price` FROM `recipe` WHERE `category` = '"+category+"'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)

    elif(choice==4):

        print('update recipe')
        
        name = input('enter the name of the recipe to be updated : ')

        category = input('enter the category such as veg or non-veg : ')

        taste = input('enter the taste you need : ')

        price = input('enter the price : ')

       

       
        sql = "UPDATE `recipe` SET `category`='"+category+"',`taste`='"+taste+"',`price`='"+price+"' WHERE `name`='"+name+"'"

        mycursor.execute(sql)

        mydb.commit()

        print('Updated sucessfully !!!')


    elif(choice==5):

            print('delete recipe')
        
            name = input('enter the name')

            name = input('enter the recipe to be deleting: ')

            sql = "DELETE FROM `recipe` WHERE `name`='"+name+"'"

            mycursor.execute(sql)

            mydb.commit()
            print("data deleted succesfully")

    elif(choice==6):
        
        

        print('total price')

        sql = 'SELECT SUM(`price`) FROM `recipe` '

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)
    elif(choice==7):
         

        print('total price for each category')

        sql = "SELECT `category`, SUM(`price`) FROM `recipe` GROUP BY `category`"

        mycursor.execute(sql)

        result = mycursor.fetchall()
    
        print(result)
    elif(choice == 8):
        break