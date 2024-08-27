# Open the input file for reading
with open("input_tutorial1.txt", "r") as input_file:
    # Read each line from the input file
    line1 = input_file.readline()
    input_file.readline()
    line_left = input_file.readlines()


with open("input_tutorial1.txt", "r") as input_file:
    lines = input_file.readlines()
    
    
    
    
    
    
    
    
# string = '1,2,3\n'

# splited_string = string.strip().split(',')

# splited_string_int = [int(x) for x in splited_string]








# Open the input file for reading
with open("input_tutorial1.txt", "r") as input_file:
    lines = input_file.readlines()
    
# line = lines[0]
# splited_line = [int(i) for i in line.strip().split(";")]


matrix1 = []
for line in lines:
    splited_line = [int(i) for i in line.strip().split(";")]
    matrix1.append(splited_line)
    
    
    
    
    
    
    
    
# A = [[1,2,3],[4,5,6]]
# B = [[2,4,10],[11,8,7]]

# sum_AB = [[A[i][j]+B[i][j]for j in range(len(A[0]))] for i in range(len(A))]










A = [[1,2,10,58], [1,3,10], [10,9,1,5,7,9,7],[3]]
# with open("output_mean_1.txt","w") as output_file:
#     for entry in A:
#         mean = sum(entry)/len(entry)
#         output_file.write(f"{mean}\n")
        


# mean_list = []
# for entry in A:
#     mean = sum(entry)/len(entry)
#     mean_list.append(mean)

# with open("output_mean_1_.txt","w") as output_file:
#     for mean in mean_list:
#         output_file.write(f"{mean}\n")





# # Open the input file for reading
# with open("input_tutorial2.txt", "r") as input_file:
#     # Read each line from the input file
#     lines = input_file.readlines()
    

# matrix2 = []
# for line in lines:
#     splited = line.strip().split("|")
#     splited_line = [int(i) for i in splited]
#     matrix2.append(splited_line)



# with open("output_mean_2.txt","w") as output_file:
#     for entry in matrix2:
#         mean = sum(entry)/len(entry)
#         output_file.write(f"{mean}\n")