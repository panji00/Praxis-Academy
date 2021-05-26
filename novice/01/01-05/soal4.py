# latihan 1
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print(a[::])

# Latihan 2
#     a = [1.32, 22.1, 2.34]
#     b = ['1', '13b', 'aa1']
#     c = [3, 40, 100]
#     # combine list
#     .......
# Expected Output :

# [ [1.32, 22.1, 2.34], [3, 40, 100], ['1', '13b', 'aa1'] ]

# # Latihan 3
# code 
#     a = [
#         [5, 9, 8],
#         [0, 0, 6]
#         ]
#     # subsetting list
#     ......

# Expected Output :

# [0, 6]

# # Latihan 4
# code
#     p = [0, 5, 2, 10, 4, 9]
#     # ordered list
#     print(....(p, reverse=False))
#     # get max value of list
#     print(....(p))

# Expected Output :

# [0, 2, 4, 5, 9, 10]

# 10

# # Latihan 5
# code
#     a = [1, 3, 5]
#     b = [5, 1, 3]
#     # combine list
#     .......

# Expected Output :

# [5, 1, 3, 1, 3, 5]

# # Latihan 6
# code
#     a = [
#         [5, 9, 8],
#         [0, 0, 6]
#         ]
#     # change list value
#     .....
#     # change list value
#     .....
#     print(a)

# Expected Output :

# [ [5, 9, 10], [11, 0, 6] ]

# # Latihan 7
# code
#     areas = ["hallway", 11.25, "kitchen", 18.0,
#             "chill zone", 20.0, "bedroom", 10.75,
#             "bathroom", 10.50, "poolhouse", 24.5,
#             "garage", 15.45]

#     # Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code
#     ........
#     print(areas)

# Expected Output:

# ['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'poolhouse', 24.5, 'garage', 15.45]

# # Latihan 8
# code
#     S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#     T = .......

#     print(T)

# Expected Output:

# [0, 4, 16, 36, 64]

# # Latihan 9
# code
#     europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

#     # print semua key yang ada di objek europe
#     .....
#     # print nilai dari key franche
#     .....

# Expected Output:

# dict_keys(['spain', 'france', 'germany', 'norway'])

# paris

# # Latihan 10
# code
#     europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

#     # tambahkan key itali ke objek dictionary dengan value roma
#     ..........

#     # cek apakah itali ada di dalam objek dictionary
#     print(........)

# Expected Output:

# True

# # Latihan 11
# code
#     europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
#             'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
#             'australia':'vienna' }

#     # update nilai ibukota german ke berlin
#     .........

#     # remove australia dari europa
#     ........

#     print(europe)

# Expected Output:

# {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw'}

# # Latihan 12
# code
#     country = { 
#             'spain': { 'capital':'madrid', 'population':46.77 },
#             'france': { 'capital':'paris', 'population':66.03 },
#             'germany': { 'capital':'berlin', 'population':80.62 },
#             'norway': { 'capital':'oslo', 'population':5.084 } 
#             }

#     # berapa populasi dari kota german?
#     print(......)

#     # update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250


#     print(country)

# Expected Output:

# 80.62

# {'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'indonesia': {'capital': 'jakarta', 'population': 250}}

# # Latihan 13
# code 
#     country = { 
#             'spain': { 'capital':'madrid', 'population':46.77 },
#             'france': { 'capital':'paris', 'population':66.03 },
#             'germany': { 'capital':'berlin', 'population':80.62 },
#             'norway': { 'capital':'oslo', 'population':5.084 },
#             'indonesia' : {'capital':'jakarta', 'population':250}
#             }

#     for ....... in .......:
#         print('Ibukota '+.....+' adalah '+......)

# Expected Output:

# Ibukota spain adalah madrid

# Ibukota france adalah paris

# Ibukota germany adalah berlin

# Ibukota norway adalah oslo

# Ibukota indonesia adalah jakarta