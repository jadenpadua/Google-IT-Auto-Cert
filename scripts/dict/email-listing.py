def email_list(domains):
  res = []
  for key in domains:
    listing = domains[key]
    for i in range(len(listing)):
      res.append(listing[i] + '@' + key)
  return res

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
