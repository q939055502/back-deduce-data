import random


def generate_10_integers(target_avg: float) -> list:
    """
    生成10个整数，平均值等于target_avg
    
    参数：
        target_avg: 目标平均值
        
    返回：
        10个整数的列表
    """
    min_val = int(target_avg - 10)
    max_val = int(target_avg + 10)
    middle_count = 10
    
    middle_sum = int(round(target_avg * middle_count))
    
    attempts = 10000
    middle = []
    for _ in range(attempts):
        remaining_sum = middle_sum
        temp = []
        
        for i in range(middle_count - 1):
            max_available = remaining_sum - (middle_count - 1 - i) * min_val
            val = random.randint(min_val, min(max_val, max_available))
            temp.append(val)
            remaining_sum -= val
        
        last_val = remaining_sum
        if min_val <= last_val <= max_val:
            temp.append(last_val)
            
            actual_avg = sum(temp) / 10
            if round(actual_avg, 1) == round(target_avg, 1):
                middle = temp
                return middle
    return []


def generate_16_integers_until_success(target_avg: float) -> list:
    while True:
        result = generate_10_integers(target_avg)
        
        if result:
            if round(sum(result) / 10, 1) == round(target_avg, 1):
                max_val = max(result)
                min_val = min(result)
                max_list =[]
                min_list = []
                #生成一个1-5的随机整数
                for _ in range(3):
                    max_list.append(max_val+random.randint(1, 5))
                    min_list.append(min_val-random.randint(1, 5))


                final_result = min_list + result + max_list
                return final_result
    return []        
            


if __name__ == '__main__':
    test_avg = 50.1
    result = generate_16_integers_until_success(test_avg)
    print(result)
    print(sum(result[3:13]) / 10)
    exit(0)
    print(f"个数: {len(result)}")
    print(f"平均值: {sum(result) / 10}")
    print(f"目标平均值: {test_avg}")
