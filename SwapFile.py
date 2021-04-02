#Creating the inputs for the user
FirstFileName = str(input("Name Of First file"))
SecondFileName = str(input("Name Of Second file"))

def SwapFiles(FirstFilePath, SecondFilePath):
    #File Object stored in the variable in read mode
    File_1_OBJ = open(FirstFilePath , 'r')
    File_2_OBJ = open(SecondFilePath , 'r')
    
    #Reading the lines and stoaring them them
    File_1_Lines = File_1_OBJ.readlines()
    File_2_Lines = File_2_OBJ.readlines()

    File1_Lines_Data = ''
    File2_Lines_Data = ''
    
    #Running through the words and storing the words in a variable
    for words in File_1_Lines:
        File1_Lines_Data = words

    for words in File_2_Lines:
        File2_Lines_Data = words

    #Opening the files in editMode and writing the data using .write() function
    File_1_Edited = open(FirstFilePath, "w")
    File_1_Edited.write(File2_Lines_Data)

    File_2_Edited = open(SecondFilePath, "w")
    File_2_Edited.write(File1_Lines_Data)

#Calling and using the new function 
SwapFiles(FirstFileName, SecondFileName)