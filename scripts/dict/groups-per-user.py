def groups_per_user(ht):
    res = {}
    for key in ht:
        listing = ht[key]
        for i in range(len(listing)):
            user = listing[i]
            if user not in res:
                res[user] = [key]
            else:
                res[user].append(key)
    return res


print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
