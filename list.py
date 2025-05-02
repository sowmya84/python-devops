s1 = "john"
s2 = "ram"
s3 = "sam"
s4 = "manu"

print(s1)
print(s2)
print(s3)
print(s4)

#List
s3_bucket_lists = ["abhi_demo_bucket", "shinny_demo_bucket", "ramu_demo_bucket", "tom_demo_bucket"]
print(s3_bucket_lists)
print(type(s3_bucket_lists ))
print(len(s3_bucket_lists))
print(s3_bucket_lists[1]) #to print any element use index

new_list = s3_bucket_lists[1:3] #slicing
print(new_list)

#adding one more item to list
s3_bucket_lists.append("new_s3_bucket")
print(s3_bucket_lists )
#removing a item from list
s3_bucket_lists.remove("tom_demo_bucket")
print(s3_bucket_lists )


#Tuple
s3_bucket_lists = ("abhi_demo_bucket", "shinny_demo_bucket", "ramu_demo_bucket", "tom_demo_bucket")
print(s3_bucket_lists)
print(type(s3_bucket_lists ))
print(len(s3_bucket_lists))
print(s3_bucket_lists[1])


print(s3_bucket_lists[0] + "****" + s3_bucket_lists[1])