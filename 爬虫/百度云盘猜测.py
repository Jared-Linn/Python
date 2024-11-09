# vim: set fileencoding=utf-8:

import requests
import concurrent.futures

import itertools



def generate_combinations(characters, length, start, end):
    # 生成指定范围内的组合
    return [''.join(combination) for combination in itertools.product(characters, repeat=length) if
            len(combination) >= start and len(combination) <= end]


def generate_all_combinations(length=15):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'



    # 1
    # 使用itertools.product生成所有可能的组合
    for combination in itertools.product(characters, repeat=length):
        # 将元组转换为字符串
        yield ''.join(combination)

    # # 2
    # # 计算总组合数
    # total_combinations = len(characters) ** length
    # # 计算每个线程应该处理的组合数
    # combinations_per_thread = total_combinations // 4  # 假设我们使用4个线程
    # # 创建线程池
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    #     # 提交任务
    #     futures = []
    #     for i in range(0, total_combinations, combinations_per_thread):
    #         end = min(i + combinations_per_thread, total_combinations)
    #         futures.append(executor.submit(generate_combinations, characters, length, i, end))
    #
    #     # 等待所有任务完成
    #     # 收集结果并合并
    #     all_combinations = []
    #     for future in concurrent.futures.as_completed(futures):
    #         all_combinations.extend(future.result())
    #
    # return all_combinations


def get_combinations(base_url):
    #                               1vRo9npl000000000000000

    # 目标URL
    full_url = "https://pan.baidu.com/s/1vRo9npl"+base_url

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }


    # 发送GET请求
    response = requests.get(url=full_url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # print('请求成功！')
        return "请求成功" + full_url
        # 打印响应内容
        # print(response.text)
    else:
        # print('请求失败，状态码：', response.status_code)
        # return "请求失败", response.status_code
        return ""

# 调用函数并打印结果
if __name__ == "__main__":
    #
    # for i, combination in enumerate(generate_all_combinations()):
    #     print(f"{i + 1}: {combination}")
    #     # 打印一定数量的结果后停止，因为结果非常多
    #     if i >= 10:  # 这里只打印前10个结果作为示例
    #         break
    # reqs = get_combinations('combination')
    # print(reqs)

    all_combinations = generate_all_combinations()
    for i, combination in enumerate(all_combinations):

        reqs = get_combinations(combination)

        # print(f"{i + 1}: {combination}")
        # print(f"{i + 1}: {reqs}")
        print(reqs)
        # if i >= 10:  # 只打印前10个结果作为示例
        #     break
