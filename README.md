# 0x00. AirBnB_clone -The Console

ALX Project.

## About

The aim of this project is to create the AirBnB console.
The console will have a single use function to modify, create and delete objects in the storage. It acts like a sandbox.

## Prerequisites

`python3`

## Using the project

First you have to clone the repository using this command

`git clone git@github.com:Veralee225/AirBnB_clone.git`

`cd AirBnB_clone`

Then use this command

`./console.py`
or
python3 console.py

## Running Tests

### Running the test in an interactive mode

`python3 -m unittest discover tests`

#### Running the test in a non-interactive mode

`echo "python3 -m unittest discover tests" | bash`

The project makes use of command interpreters which is explained below :

The following commands are supported:

### create

  Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
  Ex:

  ```
  create BaseModel
  ```

### show

  Prints the string representation of an instance based on the class name and id.
  Ex:

  ```
  show BaseModel 1234-1234-1234.
  ```

### destroy

  Deletes an instance based on the class name and id (save the change into the JSON file).
  Ex:

  ```
  destroy BaseModel 1234-1234-1234.
  ```

### all

  Prints all string representation of all instances based or not on the class name.
  Example to show all instances

  ```
  all
  ```

  Example to show all instances of BaseModel only

  ```
  all BaseModel
  ```

### update

  Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
  Ex:

  ```
  update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
  ```

### quit

  Quit the shell

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming language

## ✍️ Authors <a name = "authors"></a>

- [@Ginakalu](https://github.com/Ginakalu) - Georgina Kalu
- [@Veralee](https://github.com/Veralee225) - Vera Adiele
