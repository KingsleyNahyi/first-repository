#input is in the form <name>:<comma- separated answers>"
#["Ama:True,false,True "," "Eric:False,False]
vowels = "aeiouAEIOU"
def scored_reports(list_of_students:list)->list:
    def data_processing(list_of_student_responses):
        new_list = [response.strip() for response in list_of_student_responses if response[0] in vowels]
        return new_list
    def split_responses(list):
        reports = []
        for response in list:
            the_split = response.split(":")
            name = the_split[0]
            answers = the_split[1]
            last_three_characters = name[-4:-1]
            reverse = last_three_characters[::-1]
            ID = reverse + str(len(name))
            tokens = answers.split(",")
            convertion =[]
            kept_answers = ""
            for token in tokens:
                if token=="True":
                    new = 1
                    convertion.append(new)
                elif token=="False":
                    new =0
                    convertion.append(new)
                else:
                    pass
            if len(convertion)>1:
                 for i in convertion:
                    if i==0 and i in convertion[i+1:]:
                        convertion.remove(i)
            else:
                pass
            student_score = 0
            maximum = len(convertion)
            for item in convertion:
                student_score+=item
                kept_answers = kept_answers+str(item)
        
            Report_string = f"[{ID}|{kept_answers}|{student_score}/{maximum}]"
            reports.append(Report_string)
        return reports

#question 2
def pivot_shuffle(data:list,k:int):
    #partitioning
    left = data[0:k] 
    right = data[-k:]
    middle = data[k:-k]
    #rearranging
    new_data = [right, middle, left]
    #reversing k elements present in first list in nw_data
    new_data[0] = right[::-1]
    
    actual_list = [number for item in new_data for number in item]
    #using set to remove duplicates
    set(actual_list)
    
