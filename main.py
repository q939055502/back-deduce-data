

from step1_read_data import read_all_txt_files
from step2_back_deduce_10 import verify_and_retry
from step3_back_deduce_16 import generate_16_integers_until_success
from step4_to_write_file import write_dict_to_csv
import random
import math

nane_and_data, tan_hua, tan_hua_re = read_all_txt_files()

for i in range(1, 500):
    str1=str(i/10+21)
    str2=str(round(0.78741 * 0.034488 * ((i/10+21) ** 1.94),1))
    tan_hua.append([str1, str2])
    tan_hua_re.append([str2, str1])

unique_data1 = [list(t) for t in set(tuple(item) for item in tan_hua)]
unique_data2 = [list(t) for t in set(tuple(item) for item in tan_hua_re)]
# print(len(tan_hua))
# print(len(tan_hua_re))
# print(len(unique_data1))
# print(len(unique_data2))
# exit(0)

tan_hua_re_dict = {row[0]: row[1] for row in unique_data2}


tan_hua=[]
tan_hua_re=[]

for tan_hua_re_dict_item in tan_hua_re_dict:
    tan_hua_re.append([tan_hua_re_dict_item, tan_hua_re_dict[tan_hua_re_dict_item]])
    tan_hua.append([tan_hua_re_dict[tan_hua_re_dict_item], tan_hua_re_dict_item])


# print(len(tan_hua))
# print(len(tan_hua_re))
# print(len(tan_hua_re_dict))
# print(len(unique_data1))
# print(len(unique_data2))
# print(tan_hua_re)
# print('======================')

# # print(tan_hua_re_dict.keys())
# for k in tan_hua_re_dict.keys():
#     print(k)
# exit(0)

# # print(tan_hua_re_dict.keys())
# for k in tan_hua_re:
#     print(k[0])
# exit(0)










# tan_hua_dict = {row[0]: row[1] for row in tan_hua}
data_re_scope_str = [] # 记录所有数据的范围
for row in tan_hua_re:
    data_re_scope_str.append(row[0])

nane_and_data_dict_list = []
nane_and_data_dict={}
for nane_and_data_item in nane_and_data:
    dic1={}
    dic1['name'] = nane_and_data_item[0]
    dic1['avg'] = nane_and_data_item[1]
    dic1['sd'] = nane_and_data_item[2]
    dic1['min_val'] = nane_and_data_item[3]
    dic1['estimated'] = nane_and_data_item[4]
    nane_and_data_dict_list.append(dic1)
    nane_and_data_dict[nane_and_data_item[0]]=dic1

print('********************') # 记录基本信息
ss=''
for k in nane_and_data_dict.keys():
    name=k
    avg=nane_and_data_dict[k]['avg']
    sd=nane_and_data_dict[k]['sd']
    min_val=nane_and_data_dict[k]['min_val']
    estimated=nane_and_data_dict[k]['estimated']
    avg2 = None
    sd2 = None
    min_val2 = None
    result = verify_and_retry(name, avg, sd, min_val, estimated, data_re_scope_str)
    result = [float(x) for x in result]
    if result:
        avg2 = round(sum(result)/len(result), 1)
        sd2 = round(math.sqrt(sum((x-sum(result)/len(result))**2 for x in result)/(len(result)-1)), 2)
        min_val2 = min(result)
        if avg2 == float(avg) and sd2 == float(sd) and min_val2 == float(min_val):
            nane_and_data_dict[k]['num_10_revise']=[str(x) for x in result]
            revise_value_list = []
            for num in nane_and_data_dict[k]['num_10_revise']:
                revise_value_list.append(tan_hua_re_dict[num])
            nane_and_data_dict[k]['num_16_avg']=revise_value_list
            print(f"{name}: 满足条件--10")

            for result_item in revise_value_list:
                while True:
                    numlist1 = generate_16_integers_until_success(float(result_item))
                    if numlist1:
                        random.shuffle(numlist1)
                        nane_and_data_dict[k][str(result_item)] = numlist1
                        break
                    print(f"生成{nane_and_data_dict[k]['num_10']} 的 {result_item}的16个整数失败，重新生成")
        else:
            print(f"\n{name}: 不满足条件")
            print(f"目标: 平均值={avg}, 标准差={sd}, 最小值={min_val}")
            print(f"实际: 平均值={avg2}, 标准差={sd2}, 最小值={min_val2}")

# print(nane_and_data_dict['首层柱 4XB'][ss])
# print(ss)
# print(nane_and_data_dict)

success = write_dict_to_csv(nane_and_data_dict)
print(f"写入结果: {'成功' if success else '失败'}")





    
# if __name__ == '__main__':






