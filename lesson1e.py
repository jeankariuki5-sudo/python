# tuple - collection of items that is immuttable(cannot change)
# we access items using indexing starting from index 0
# we use parentthesis t0 denote it

counties = ("Nakuru", "Nyandarua", "Kericho", "Meru", "Murang'a", "Uasin Gishu")

# Kericho
print(counties[2])

# Nyandarua to Murang'a
print(counties[1:5])

# Meru to Uasin Gishu
print(counties[3:])

# Nakuru to Meru
print(counties[:4])