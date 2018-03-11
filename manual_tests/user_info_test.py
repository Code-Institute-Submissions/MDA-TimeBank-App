import json


# User Info json dump test

temp_list = []


name = "pol"
email = "me@me.com"
score = 15

temp_list.append({
"name": name,
"email": email,
"score": int(score),
})


# stored_list = temp_list


with open('user_data.txt', 'a') as outfile:  
    json.dump(temp_list, outfile)




# dump_list = stored_list
# stored_list = []
# temp_list = []

name = "des"
email = "u@u.com"
score = 20

temp_list.append({
"name": name,
"email": email,
"score": int(score),
})

# stored_list = temp_list

with open('user_data.txt', 'a') as outfile:  
    json.dump(temp_list, outfile)




# dump_list = stored_list
# stored_list = []
# temp_list = []

name = "mark"
email = "three@three.com"
score = 30

temp_list.append({
"name": name,
"email": email,
"score": int(score),
})

# stored_list = temp_list

with open('user_data.txt', 'w') as outfile:  
    json.dump(temp_list, outfile)