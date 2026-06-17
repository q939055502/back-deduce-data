import csv
import os


def write_dict_to_csv(data_dict: dict, file_path: str = None) -> bool:
    if not data_dict:
        return False
    
    if file_path is None:
        project_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(project_dir, '输出数据.csv')
    
    try:
        with open(file_path, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            for row_dict in data_dict.keys():
                row = [row_dict, data_dict[row_dict]['avg']]
                row.append(data_dict[row_dict]['sd'])
                row.append(data_dict[row_dict]['min_val'])
                row.append(data_dict[row_dict]['estimated'])
                i=0
                for num in data_dict[row_dict]['num_16_avg']:
                    for item in data_dict[row_dict][num]:
                        row.append(item)
                    row.append(num)
                    row.append(data_dict[row_dict]['num_10_revise'][i])
                    i+=1
                writer.writerow(row)
        return True
    except Exception as e:
        print(f"写入文件失败: {e}")
        return False




if __name__ == '__main__':
    test_data = {
        '首层柱 4XB': {'name': '首层柱 4XB', 'avg': '50.1', 'sd': '6.94', 'min_val': '39.2', 'estimated': '38.7', 
                     'num_10_revise': ['39.2', '50.0', '44.5', '49.4', '51.2', '59.5', '46.8', '51.8', '45.9', '62.8'], 
                     'num_16_avg': ['42.5', '48.2', '45.4', '47.9', '48.8', '52.7', '46.6', '49.1', '46.1', '54.2'], 
                     '42.5': [49, 34, 52, 53, 32, 29, 48, 56, 29, 47, 56, 46, 37, 48, 28, 32], 
                     '48.2': [50, 38, 56, 43, 57, 51, 51, 43, 37, 60, 61, 33, 35, 38, 60, 55],
                     '45.4': [35, 48, 39, 48, 34, 58, 47, 31, 58, 51, 32, 40, 43, 53, 50, 56],
                     '47.9': [35, 37, 46, 57, 61, 58, 58, 45, 50, 51, 40, 54, 53, 46, 33, 34],
                     '48.8': [61, 63, 39, 57, 60, 37, 54, 43, 53, 36, 46, 39, 57, 42, 58, 38],
                     '52.7': [49, 61, 58, 38, 65, 55, 59, 67, 62, 48, 64, 38, 47, 38, 45, 43],
                     '46.6': [33, 57, 52, 50, 61, 41, 31, 38, 53, 42, 56, 43, 55, 36, 34, 59],
                     '49.1': [42, 45, 37, 47, 55, 43, 55, 38, 40, 53, 59, 61, 37, 54, 59, 57],
                     '46.1': [51, 33, 54, 44, 36, 54, 38, 53, 49, 33, 54, 51, 48, 43, 41, 43],
                     '54.2': [46, 45, 53, 64, 69, 59, 57, 46, 66, 66, 42, 41, 60, 60, 52, 44]},
        '首层柱 5XB': {'name': '首层柱 5XB', 'avg': '48.5', 'sd': '5.23', 'min_val': '40.1', 'estimated': '39.0', 
                     'num_10_revise': ['40.1', '45.0', '48.5', '49.4', '51.2', '59.5', '46.8', '51.8', '45.9', '62.8'], 
                     'num_16_avg': ['42.5', '48.2'], 
                     '42.5': [49, 34, 52, 53, 32, 29, 48, 56, 29, 47, 56, 46, 37, 48, 28, 32], 
                     '48.2': [50, 38, 56, 43, 57, 51, 51, 43, 37, 60, 61, 33, 35, 38, 60, 55]}
    }
    
    success = write_dict_to_csv(test_data)
    print(f"写入结果: {'成功' if success else '失败'}")




