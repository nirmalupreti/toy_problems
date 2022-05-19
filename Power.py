'''f = open(
    "/Users/nirmal/PycharmProjects/toy_problems/dummy_data_transformation_master/resources/test/inputs/dummy_power_generation_contracts_plant.csv",
    "r")
print(f.read())

#f = open("/Users/nirmal/PycharmProjects/toy_problems/dummy_data_transformation_master/resources/test/outputs/output_sample_power_generation_contracts_unit1.csv",
    #"w")

g = open("/Users/nirmal/PycharmProjects/toy_problems/dummy_data_transformation_master/resources/test/outputs/output_sample_power_generation_contracts_unit1.csv", "w")
g.write(f.read())'''



#reading from file1 and writing to file2
with open("/Users/nirmal/PycharmProjects/toy_problems/dummy_data_transformation_master/resources/test/inputs/dummy_power_generation_contracts_plant.csv", "r") as file1:
    with open("/Users/nirmal/PycharmProjects/toy_problems/dummy_data_transformation_master/resources/test/outputs/output_sample_power_generation_contracts_unit1.csv", "w") as file2:
        file2.write(file1.read())


#reading from file1
with open("/Users/nirmal/PycharmProjects/toy_problems/dummy_data_transformation_master/resources/test/outputs/output_sample_power_generation_contracts_unit1.csv") as file2:
    print(file2.read())






