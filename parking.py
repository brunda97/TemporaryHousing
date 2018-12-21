#To read from input file
input_file = open("input.txt", "r")

#no of beds available in LAHSA
beds=int(input_file.readline())

#No of Parking spaces available by SPLA
spaces=int(input_file.readline())

#Total no of applicants choosen by LAHSA
lahsa=int(input_file.readline())
#List of applicants ID choosen by LAHSA if lahsa>0
lahsa_app=[]
if(lahsa>0):
  
  for i in range(0,lahsa):
    input1=input_file.readline().strip()
    lahsa_app.append(input1)
  #print lahsa_app

    

#Total no of applicants choosen by SPLA
spla=int(input_file.readline())
spla_app=[]
#List of applicants ID choosen by SPLA if spla>0
if(spla>0):
  
  for i in range(0,spla):
    spla_app.append(input_file.readline().strip())
  #print spla_app

#Total no of applicants
total=int(input_file.readline())

#Total no of applicants greater than 0 then read all the remaining lines
if(total>0):
  total_app=[]
  while True:
      line=input_file.readline().strip()
      if line == '':
          break
      total_app.append(line)
#print total_app

#Beds taken in LAHSA
beds_taken_lahsa=[0,0,0,0,0,0,0]
#Parking spaces taken in SPLA
space_taken_spla=[0,0,0,0,0,0,0]
returnval=0
path=[]
splalen=0
lahsalen=0
#to find the maximum count
def findMaxSubarraySum(arr, n, s,list1,present): 
  # To store current sum and 
  # max sum of subarrays
  present1=[0,0,0,0,0,0,0]
  present1[:]=present[:] 
  curr_sum=arr[0]
  max_sum=0
  start = 0
  total=0
  #current_count=0
  list1.append(curr_sum)
  flag=0
  #print "Present",present
  for val in range(13,len(curr_sum)):
      if int(curr_sum[val])+present1[val-13]>s:
        flag=1
        break
  for val in range(13,len(curr_sum)):
      total+=int(present1[val-13])
  
  if(flag==0):
      for val in range(13,len(curr_sum)):
        present1[val-13]+=int(curr_sum[val])
        total+=int(curr_sum[val])
        #current_count+=int(curr_sum[val])
  
  for i in range(1,n):
    

    while (total > 7*s and start < i and flag==1): 
      start=start+1
      for val in range(13,len(curr_sum)):
        present1[val-13]-=int(curr_sum[val])
        total-=int(curr_sum[val])
      list1.remove(curr_sum)
      
    # Update max_sum if it becomes 
    # greater than curr_sum 
    if(max_sum < total): 
        
        max_sum = total
    # Add elements to curr_sum 
    curr_sum=arr[i]
    flag=0
    #print "Array now considering", curr_sum
    #current_count=0
    for val in range(13,len(curr_sum)):
      if int(curr_sum[val])+present1[val-13]>s:
        flag=1
        break
    if(flag==0):
      #print "Yipeee i reach here"
      for val in range(13,len(curr_sum)):
        #print present[val-13]
        present1[val-13]+=int(curr_sum[val])
        total+=int(curr_sum[val])
        #current_count=int(curr_sum[val])
    #print total
    list1.append(curr_sum)
    #curr_sum = arr[i] 
    #list1.append(curr_sum)
  if (total <= 7*s): 
      if(max_sum < total): 
        max_sum = total 
  #print "Max sum",max_sum
  return max_sum 

selected="00000" #track of best App ID
max_spla=0
max_lahsa=0 #Comparision 
path1=[]
list_id={}
list_id_min={}
#minimax function to get efficiency
def minimax(lahsa_choice,spla_choice,max1,beds,spaces,depth):
  global beds_taken_lahsa
  global space_taken_spla
  global splalen
  global lahsalen
  global selected #track of best App ID
  global max_spla
  global max_lahsa 
  global returnval
  global path1
  global list1

  if (max1):
    if(len(spla_choice)==0):
      #print "When spla_choice is 0:"
      val=0
      remaining=[]
      if (len(lahsa_choice)>0):
        for x1 in lahsa_choice:
          #print x1
          if x1 not in path:
            remaining.append(x1)
        #print "remaining LAHSA",remaining
        if remaining==[]:
          val=0
          #val=0
        else:
          list1=[]
          val=findMaxSubarraySum(remaining, len(remaining), beds,list1,beds_taken_lahsa) 
          #print "\" REMAINING VALUES1\"",remaining
          templahsa=lahsalen
          lahsalen=val
      list2=[ ]
      list2.append(splalen)
      list2.append(lahsalen)
      
      if path[0][0:5] in list_id.keys():
        #for v in 
        if list_id[path[0][0:5]][1]< lahsalen:
          list_id[path[0][0:5]]=list2
      else:
        list_id[path[0][0:5]]=list2
      
      if path[0][0:5] in list_id_min.keys():
        #for v in 
        if list_id_min[path[0][0:5]][1]> lahsalen:
          list_id_min[path[0][0:5]]=list2
      else:
        list_id_min[path[0][0:5]]=list2
      if(remaining!=[ ]):
          lahsalen=templahsa

        #return val
      return 0
    for x in spla_choice:
      index1=spla_choice.index(x)
      flag=0
      #print space_taken_spla
      for val in range(13,len(x)):
        if int(x[val])+space_taken_spla[val-13]>spaces:
          flag=1
      if x in path or flag==1 :
          #print "Removed from SPLA list as its already in path:",x
          spla_choice.remove(x)
          returnval=minimax(lahsa_choice,spla_choice,True,beds,spaces,depth)
          if returnval==None or returnval==0:
            returnval=lahsalen
          spla_choice.insert(index1,x)
      elif flag==0:
        spla_choice.remove(x)
        #print "Since ", x,"is not in path  we are adding it path now"
        path.append(x)
       # print "PAth",path
        count=0
        for val in range(13,len(x)):
          count+=int(x[val])
          space_taken_spla[val-13]+=int(x[val])
        
        
        #print count
        #print splalen
        splalen=splalen+count
        minimax(lahsa_choice,spla_choice,False,beds,spaces,depth+1)
        
        path.remove(x)
        #print space_taken_spla
        
        for val in range(13,len(x)):
          space_taken_spla[val-13]-=int(x[val])
        
        
        #splalen=tempspla-count
        #splalen=splalen-count-returnval
        splalen=splalen-count
        #print "After Return my status Length:",splalen
        #print "SPAce occupied" ,space_taken_spla
        spla_choice.insert(index1,x)
  else:
    if(len(lahsa_choice)==0):
      #print "When len(lahsa_choice)==0"
      val=0
      remaining=[]
      if (len(spla_choice)>0):
        for x1 in spla_choice:
          if x1 not in path:
            remaining.append(x1)
        #print "Remaining SPLA",remaining
        if remaining==[]:
          val=0
        else:
          list1=[]
          #Max spaces that can fit sum
          #print space_taken_spla
          val=findMaxSubarraySum(remaining, len(remaining),spaces,list1,space_taken_spla)
          tempspla=splalen
          splalen=val
      list2=[ ]
      list2.append(splalen)
      list2.append(lahsalen)
      #list3=[]
      #list3.append(path[0][0:5])
      #list3.append(list2)
      if path[0][0:5] in list_id.keys():
        if list_id[path[0][0:5]][1]< lahsalen:
          list_id[path[0][0:5]]=list2
      else:
        list_id[path[0][0:5]]=list2
      
      if path[0][0:5] in list_id_min.keys():
        #for v in 
        if list_id_min[path[0][0:5]][1]> lahsalen:
          list_id_min[path[0][0:5]]=list2
      else:
        list_id_min[path[0][0:5]]=list2

      if remaining !=[]:
        splalen=tempspla
      return 0
    for x in lahsa_choice:
      index1=lahsa_choice.index(x)
      #print x,"at depth ",depth
      flag=0
      for val in range(13,len(x)):
        if int(x[val])+beds_taken_lahsa[val-13]>beds:
          flag=1
          break
      if x in path or flag==1:
          lahsa_choice.remove(x)
          returnval=minimax(lahsa_choice,spla_choice,False,beds,spaces,depth)
          if returnval==None or returnval==0:
            returnval=splalen
          lahsa_choice.insert(index1,x)
      elif flag==0:
        lahsa_choice.remove(x)
        path.append(x)
        count=0
        for val in range(13,len(x)):
          beds_taken_lahsa[val-13]+=int(x[val])
          count+=int(x[val])
        lahsalen=lahsalen+count 
        returnval=minimax(lahsa_choice,spla_choice,True,beds,spaces,depth+1)
        if returnval==None or returnval==0:
          returnval=lahsalen
        path.remove(x)
        #print "Beds Taken",beds_taken_lahsa
        #print x
        for val in range(13,len(x)):
          beds_taken_lahsa[val-13]-=int(x[val])
        lahsalen=lahsalen-count
        lahsa_choice.insert(index1,x)

#remaining to choose from total list
remaining=total_app[:]
for i in total_app:
  app_id=i[0:5]
  #print app_id
  if app_id in spla_app:
    for j in range(13,20):
      if(int(i[j])==1):
        space_taken_spla[j-13]=space_taken_spla[j-13]+1
    remaining.remove(i)
  if app_id in lahsa_app:
    for j in range(13,20):
      if(int(i[j])==1):
        beds_taken_lahsa[j-13]=beds_taken_lahsa[j-13]+1
    remaining.remove(i)


#check if all the spaces for all the week are allocated if all spaces are allocated then selected is set to 00000
count_increment=0
for i in range(0,7):
  if (space_taken_spla[i]==spaces):
    count_increment+=1
if count_increment==7:
  selected="00000" 
  
spla_choice=[]
lahsa_choice=[]
for i in remaining:
  app_id=i[0:5]
  gender=i[5].upper()
  age=i[6:9]
  pets=i[9].upper()
  condition=i[10].upper()
  car=i[11].upper()
  license=i[12].upper()
  days=i[13:]
  #print i[13:14]
  if car=='Y' and license=='Y' and condition=='N':
    count_increment=0
    for j in range(0,7):
      #print space_taken_spla[j]
      #print spaces
      if (space_taken_spla[j] + int(i[j+13:j+14])>spaces):
        count_increment+=1
    if count_increment==0:
      spla_choice.append(i)
  if gender=='F' and age>17 and pets=='N':
    count_increment=0
    for j in range(0,7):
      if (beds_taken_lahsa[j]+int(i[j+13:j+14])>beds):
        count_increment+=1
    if count_increment==0:
      lahsa_choice.append(i)

for v in beds_taken_lahsa:
    lahsalen+=v
for v in space_taken_spla:
    splalen+=v
if spla_choice==[]:
  selected="00000"
else:
  #print space_taken_spla
  minimax(lahsa_choice,spla_choice,True,beds,spaces,0)
  templistdiff={}

for x in list_id_min.keys():
  templistdiff[x]=int(list_id[x][1])-int(list_id_min[x][1])
minval=min(templistdiff.values())
#tempmax={}
maxval=0
maxlist=[]

for x in list_id:
  if maxval<list_id[x][0]:
    #maxlist[x]=list_id[x][0]
    maxval=list_id[x][0]

for x in list_id:
  if maxval==list_id[x][0]:
    maxlist.append(x)



#print maxlist

select=maxlist
#print maxval
select1=""

#print select
if(len(select)==1):
  select1= select[0]
else:
  select1=select[0]
  #print select1
  for x in range(1,len(select)):
    if(int(select1)>int(select[x])):
      select1=select[x]
  #print select1

f1=open("output.txt","w")
f1.write("%s"%select1)
f1.close()


