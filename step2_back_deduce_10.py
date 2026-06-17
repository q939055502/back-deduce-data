from step1_read_data import read_all_txt_files
import numpy as np
from scipy.optimize import minimize
import math


def generate_sample(mean_target, std_target, min_target, n=10):
    """
    第一步：生成n个数值，满足样本均值、标准差、最小值约束
    使用约束优化方法
    """
    x0 = np.random.normal(mean_target, std_target, n)
    x0[0] = min_target
    
    def objective(x):
        return 0
    
    def constraint_mean(x):
        return np.mean(x) - mean_target
    
    def constraint_std(x):
        return np.std(x, ddof=1) - std_target
    
    def constraint_min(x):
        return np.min(x) - min_target
    
    constraints = [
        {'type': 'eq', 'fun': constraint_mean},
        {'type': 'eq', 'fun': constraint_std},
        {'type': 'eq', 'fun': constraint_min}
    ]
    
    bounds = [(min_target, None) for _ in range(n)]
    
    result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints, options={'maxiter': 1000})
    
    if result.success:
        return result.x
    else:
        return None


def check_values_in_scope(values, data_re_scope_str):
    """
    第二步：检查生成的数值是否存在于取值范围中
    处理浮点精度问题：乘以10转换为整数比较
    """
    scope_integers = set()
    for v in data_re_scope_str:
        try:
            val = float(v)
            scope_integers.add(int(round(val * 10)))
        except:
            continue
    
    for val in values:
        val_int = int(round(val * 10))
        if val_int not in scope_integers:
            return False
    
    return True


def back_deduce_values(
    str_name: str,
    str_avg: str,
    str_sd: str,
    str_min: str,
    str_str_Estimated_value: str,
    data_re_scope_str: list
) -> list:
    avg = float(str_avg)
    sd = float(str_sd)
    min_val = float(str_min)
    sample_size = 10
    
    scope_values = [float(v) for v in data_re_scope_str]
    
    if min_val not in scope_values:
        closest_val = min(scope_values, key=lambda x: abs(x - min_val))
        print(f"警告: 最小值 {min_val} 不在范围内，使用最接近的值 {closest_val}")
        min_val = closest_val
    
    attempts = 800
    for _ in range(attempts):
        sample = generate_sample(avg, sd, min_val, sample_size)
        
        if sample is None:
            continue
        
        if check_values_in_scope(sample, data_re_scope_str):
            return [round(v, 1) for v in sample]
    
    return []


def verify_and_retry(
    str_name: str,
    str_avg: str,
    str_sd: str,
    str_min: str,
    str_str_Estimated_value: str,
    data_re_scope_str: list
) -> list:
    avg = float(str_avg)
    sd = float(str_sd)
    min_val = float(str_min)
    sample_size = 10
    
    avg_decimals = len(str_avg.split('.')[1]) if '.' in str_avg else 0
    sd_decimals = len(str_sd.split('.')[1]) if '.' in str_sd else 0
    
    def is_valid(result):
        if not result:
            return False
        
        current_avg = sum(result) / sample_size
        current_var = sum((x - current_avg) ** 2 for x in result) / (sample_size - 1)
        current_sd = math.sqrt(current_var)
        
        return (round(current_avg, avg_decimals) == avg and
                round(current_sd, sd_decimals) == sd and
                min(result) == min_val)
    i=0
    while True:
        result = back_deduce_values(str_name, str_avg, str_sd, str_min, str_str_Estimated_value, data_re_scope_str)
        print(i)
        i+=1
        if is_valid(result):
            return result


if __name__ == '__main__':
    nane_and_data, tan_hua, tan_hua_re = read_all_txt_files()
    tan_hua_re_dict = {row[0]: row[1] for row in tan_hua_re}

    data_re_scope_str = []
    for row in tan_hua_re:
        data_re_scope_str.append(row[1])

    for row in nane_and_data:
        name = row[0]
        avg = row[1]
        sd = row[2]
        min_val = row[3]
        estimated = row[4]
        print(name, avg, sd, min_val, estimated)
        result = back_deduce_values(name, avg, sd, min_val, estimated, data_re_scope_str)
        
        if result:
            print(f"\n{name}:")
            print(f"目标: 平均值={avg}, 标准差={sd}, 最小值={min_val}")
            print(f"结果: {result}")
            print(f"实际平均值: {sum(result)/len(result):.2f}")
            print(f"实际标准差: {math.sqrt(sum((x-sum(result)/len(result))**2 for x in result)/(len(result)-1)):.2f}")
            print(f"实际最小值: {min(result)}")
        else:
            print(f"\n{name}: 未找到满足条件的组合")
        if name == '首层柱 5XB':
           break 
    
    print('-----------------')
