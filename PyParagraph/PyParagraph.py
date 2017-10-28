import os  

def process_text(filename):
    filepath = os.path.join('raw_data',filename).replace("\\","/")
    with open(filepath,'r') as textfile:
        para = textfile.read()
        lines = para.rstrip(".").split(".")
        total_word_count = 0
        word_frequency = {}
        for line in lines:
            total_word_count += len(line.split())
            for word in line.split():
                if word in word_frequency.keys():
                    word_frequency[word] += 1
                else:
                    word_frequency.update({word:1})
        character_count = 0
        for word in word_frequency:
            character_count += len(word)
        
        result = {}

        result["File Name"] = filename
        result["Approximate Word Count"] = len(word_frequency)
        result["Approximate Sentence Count"] = len(lines)
        result["Average Letter Count"] = round(character_count/len(word_frequency),2)
        result["Average Sentence Length"] = round(total_word_count/len(lines),2)

        return result
