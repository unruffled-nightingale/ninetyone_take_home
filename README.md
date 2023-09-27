# NinetyOne Take Home


### Run

To run the application (with the example file), run: 

`python3 -m ninetyone_take_home.main ./tests/resources/TestData.csv`

To run the application (with a different file), run: 

`python3 -m ninetyone_take_home.main <YOUR FILE PATH>` 

### Test

To test the application, run `pip install pytest && pytest tests`


## Design decisions

#### Use of a dataclass schema
I have chosen to load the data into a python dataclass. This makes the code
readable and allows us to centralise expectations about our Score data. 
I would normally use pydantic's BaseModel which I am more familiar with but avoided it
in this instance to reduce the dependencies.

#### Use of a generator
I have chosen to use generators to allow us to process very large files. 


## Presumptions

#### Data
The Score schema presumes that the data does not contain nulls and is well-formed. 