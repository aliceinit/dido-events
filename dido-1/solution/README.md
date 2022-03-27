# DIDO 1

## Problem Definition

**Input**: an orgmode file with the following structure
```
* Diary
** 2022
*** Today's entry
 :PROPERTIES:
 :CREATED:  [2022-03-20 Sun 16:56]
 :END:

Secret details!!
```
**Output**: Whenever you see the `:CREATED:` property, update the previous header with the timestamp and remove the properties block:

```
* Diary
** 2022
*** <2022-03-20 Sun 16:56> Today's entry

Secret details!!
```

**Bonus**: If there are additional properties in the properties block, preserve those properties and remove only the `:CREATED:` line


## Running the code

Inside the directory containing `main.py` and `test.py`, run tests with:  
`python3 -m unittest test.py`

Run your script with:   
`python3 main.py sample-dairy.txt`

