import copy

def make_users_dynamic(user_list,base_id):
    users = copy.deepcopy(user_list)
    for i,u in enumerate(users):
        uid =  base_id + i
        u["id"] = uid
        u["username"] = f"user{uid}"
        print(u["username"])
        u["email"] = f"user{uid}@gmail.com"
    return users
