import os
import PyParagraph

#get file names to process
file_names = ['paragraph_1.txt','paragraph_2.txt']

for value in file_names:
    #read values into list, calculate total months and revenue
    result = PyParagraph.process_text(value)

    n = len(value) - 4
    outfile = f"{value[:n]}_summary.txt"
    outpath = os.path.join('output',outfile).replace("\\","/")
    
    with open(outpath,'w') as textfile:
        for key,value in result.items():
            textfile.write(f"{key}: {value}\n")




