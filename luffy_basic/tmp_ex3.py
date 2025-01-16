# -*- coding: utf-8 -*-
"""
@Name:        tmp_ex3.py
@Describe:    XXX
@Time:        2025/01/16 17:48:05
@Author:      Ray
@Version:     1.0
"""
import pandas as pd
import os


def main():
    wages_path = './luffy_basic/inputs/salary.xlsx'  # 工资表文件路径
    df = pd.read_excel(wages_path)
    save_dir = './luffy_basic/outputs'

    # 如果目录不存在，则创建它
    os.makedirs(save_dir, exist_ok=True)  # 使用exist_ok参数简化目录创建

    for index, row in df.iterrows():
        # 定义新Excel文件的名称
        name = row['姓名']
        filename = os.path.join(save_dir, f'{name}_{index+1}.xlsx')  # 文件名定义

    # 保存新的Excel文件
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            row.to_frame().T.to_excel(writer, index=False, header=df.columns)
        print(f'文件已保存：{filename}')


print('所有工资数据文件已生成。')


if __name__ == '__main__':
    main()
