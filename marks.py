import HashTable
t1=HashTable.HashTable(10)
t1.Insert("18B-001-SE",11)
t1.Insert("18B-002-SE",12)
t1.Insert("18B-003-SE",13)
t1.Insert("18B-004-SE",14)
t1.Insert("18B-005-SE",15)
t1.Insert("18B-006-SE",17)
t1.Insert("18B-007-SE",16)
t1.Insert("18B-008-SE",14)
t1.Insert("18B-009-SE",16)
t1.PrintTable()
print('Marks obtianed by 18B-006-SE:', t1.Search("18B-006-SE"))

print('--------------------------------')
print('18B-008-SE has left, deleting their marks...')
t1.Delete('18B-008-SE')
t1.PrintTable()