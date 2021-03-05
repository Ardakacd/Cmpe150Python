
my_file=open("crime_scene.txt")
line_number=0
evidence_value=[]
evidence_id=[]
evidence_weight=[]
evidence_time=[]
for line in my_file:
    stripped_line=line.strip()

    if(line_number==0):
        list1=line.split()

        max_weight=int(list1[0])
        max_time =int(list1[1])


    if(line_number==1):
        list2=line.split()
        evidence_number=int(line[0])
    if(line_number>1):
        list3=line.split()
        if(list3!=[]):
            evidence_id.append(int(list3[0]))
            evidence_weight.append(int(list3[1]))
            evidence_time.append(int(list3[2]))
            evidence_value.append(int(list3[3]))
    line_number+=1

def decent_writing(lst):
    if(len(lst)==0):
        return ""
    val1=str(lst[0])
    val2=str(decent_writing(lst[1:]))
    return val1+" "+val2


def for_sort(lst):
    for x in range(len(lst)):
        for y in range(0,len(lst)-1):
            if(lst[y]>lst[y+1]):
                lst[y],lst[y+1]=lst[y+1],lst[y]

    return lst

def for_weight(remaining_limit,i,n,evidence_weight,evidence_value,evidence_id):
    if(i==n):
        return 0,[],0

    if remaining_limit - evidence_weight[i]>=0:
        collected_weight,collected_list,collected_value=for_weight(remaining_limit-evidence_weight[i],i+1,n,evidence_weight,evidence_value,evidence_id)
        collected_weight+=evidence_weight[i]
        collected_value+=evidence_value[i]
        collected_list.append(evidence_id[i])
    else:
        collected_weight=0
        collected_list=[]
        collected_value=0
    collected_weight_dont_take,collected_list_dont_take,collected_value_dont_take=for_weight(remaining_limit,i+1,n,evidence_weight,evidence_value,evidence_id)
    if(collected_value>collected_value_dont_take):
        return collected_weight,collected_list,collected_value
    else:
        return collected_weight_dont_take,collected_list_dont_take,collected_value_dont_take

total_weight,total_list_weight,total_value_weight= for_weight(max_weight,0,evidence_number,evidence_weight,evidence_value,evidence_id)
total_list_weight=for_sort(total_list_weight)
total_list_weight=decent_writing(total_list_weight)

file_for_weight=open('solution_part1.txt',"w")
file_for_weight.write(str(total_value_weight)+"\n")
file_for_weight.write(total_list_weight)
file_for_weight.close()

def for_time(remaining_limit,i,n,evidence_time,evidence_value,evidence_id):
    if(i==n):
        return 0,[],0

    if remaining_limit - evidence_time[i]>=0:
        collected_time,collected_list,collected_value=for_time(remaining_limit-evidence_time[i],i+1,n,evidence_time,evidence_value,evidence_id)
        collected_time+=evidence_time[i]
        collected_value+=evidence_value[i]
        collected_list.append(evidence_id[i])
    else:
        collected_time=0
        collected_list=[]
        collected_value=0
    collected_time_dont_take,collected_list_dont_take,collected_value_dont_take=for_time(remaining_limit,i+1,n,evidence_time,evidence_value,evidence_id)
    if(collected_value>collected_value_dont_take):
        return collected_time,collected_list,collected_value
    else:
        return collected_time_dont_take,collected_list_dont_take,collected_value_dont_take

total_time,total_list_time,total_value_time= for_time(max_time,0,evidence_number,evidence_time,evidence_value,evidence_id)
total_list_time=for_sort(total_list_time)
total_list_time=decent_writing(total_list_time)

file_for_time=open('solution_part2.txt',"w")
file_for_time.write(str(total_value_time)+"\n")
file_for_time.write(total_list_time)
file_for_time.close()


def for_both(remaining_limit_weight,remaining_limit_time,i,n,evidence_time,evidence_weight,evidence_value,evidence_id):
    if(i==n):
        return 0,0,[],0

    if remaining_limit_weight - evidence_weight[i]>=0 and remaining_limit_time-evidence_time[i]>=0:
        collected_weight,collected_time,collected_list,collected_value=for_both(remaining_limit_weight-evidence_weight[i],remaining_limit_time-evidence_time[i],i+1,n,evidence_time,evidence_weight,evidence_value,evidence_id)
        collected_weight+=evidence_weight[i]
        collected_time+=evidence_time[i]
        collected_value+=evidence_value[i]
        collected_list.append(evidence_id[i])
    else:
        collected_weight=0
        collected_time=0
        collected_list=[]
        collected_value=0
    collected_weight_dont_take,collected_time_dont_take,collected_list_dont_take,collected_value_dont_take=for_both(remaining_limit_weight,remaining_limit_time,i+1,n,evidence_time,evidence_weight,evidence_value,evidence_id)
    if(collected_value>collected_value_dont_take):
        return collected_weight,collected_time,collected_list,collected_value
    else:
        return collected_weight_dont_take,collected_time_dont_take,collected_list_dont_take,collected_value_dont_take

total_both_weight,total_both_time,total_list_both,total_value_both= for_both(max_weight,max_time,0,evidence_number,evidence_time,evidence_weight,evidence_value,evidence_id)
total_list_both=for_sort(total_list_both)
total_list_both=decent_writing(total_list_both)

file_for_weight=open('solution_part3.txt',"w")
file_for_weight.write(str(total_value_both)+"\n")
file_for_weight.write(total_list_both)
file_for_weight.close()


my_file.close()



