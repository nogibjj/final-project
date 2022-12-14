# IDS 706 Final project
By Charlene Han, Keyu Chen, Fangting Ma
     
     
     
## Introduction
The project used a pokemon dataset found on GitHub: [lgreski](https://github.com/lgreski/pokemonData/blob/master/Pokemon.csv) and created a pokemon database.    
A Fastapi web microservice is built with default Swagger Documentation that performs various querying using SQL Query.  
Information in this pokedex include:  
Pokemon's  ```ID```,```Name```,```Form```,```Type1```,```Type2```,```Total```,```HP```,```Attack```,```Defense```,```Sp_Atk```,```Sp_Def```,```Speed```,```Generation```.     
    

<img width="1430" alt="Screen Shot 2022-12-13 at 10 50 18 PM" src="https://user-images.githubusercontent.com/45677438/207501202-981bf693-23fe-4683-a098-43bc148f393d.png">




     
## Instructions
To run this, use command:
```make all```. 
     
     
     
## Path Parameters Accepted
### /all
To see a complete list of pokemon.
   
   
### /query
To see a list of pokemons of the 9th generation.
   
     
### /query/COLUMN_NAME/SPECIFIC_ITEM
To query for specific items.  
Example: ```/query/generation/9```.  
   
If it is a Pokemon name or type name, please use "".  
Example: ```/query/Name/"Pikachu"```.  
      
       
### /order_by/COLUMN_NAME/RULE
To apply sorting based on given column name and rule (```DESC``` or ```ASC```) on **previously fetched result**.   
Example: ```/order_by/Attack/DESC```.   
    
    
### /filter/COLUMN_1/COLUMN_2/COLUMN_3/COLUMN_4/COLUMN_5/COLUMN_6
To apply filters to show up to six columns on previously fetched result.  
Example1: ```/filter/Name/Type1/""/""/""/""```.  
Example2: ```/filter/Name/Type1/Total/Generation/""/""```.       
