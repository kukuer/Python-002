#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/8/8
# @Author  : xh.w
# @File    : pmap.py

import os
import re
import json
import socket
import argparse
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def ping(host: str):

    command_line = f'ping {host}'
    with os.popen(command_line, 'r', 1) as f:
        ping_result = f.read()

    result = {}
    if not host:
        raise ValueError('入参不能为空')
    elif not isinstance(host, str):
        raise TypeError('入参类型不是字符串')

    if '往返行程的估计时' in ping_result:
        print(f'Server: {host}, 可以正常ping通')
        result[host] = 'Success'
        return result
    else:
        print(f'无法访问: {host}，请检查网络或者服务IP')
        result[host] = 'Fail'
        return result


def tcp(host: str, port: str):

    result = {}
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        print(f'Server({host}开放端口{port})')
        result[f'{host}:{port}'] = 'Success'
        return result
    except Exception as e:
        print(f'Connect to {host}:{port} {e}')
        result[f'{host}:{port}'] = 'Fail'
        return result
    finally:
        sock.close()


def ip_split(arg: str):
    """根据命令行参数分割IP段"""
    ip_list = []
    start_ip, end_ip = arg.split('-')

    start_ip1, start_ip2, start_ip3, start_ip4 = start_ip.split('.')
    end_ip_split_list = end_ip.split('.')

    loop_num = int(end_ip_split_list[3]) - int(start_ip4) + 1

    for i in range(loop_num):
        tmp = int(start_ip4) + i
        ip_list.append(f'{start_ip1}.{start_ip2}.{start_ip3}.{str(tmp)}')

    return ip_list


def process_schema(num, action, ip_str, save_file=None):

    resutl = {}
    future_list = []
    with ProcessPoolExecutor(max_workers=num) as executor:
        try:
            if action == 'ping':
                ip_list = ip_split(ip_str)
                if save_file:
                    for ip in ip_list:
                        future = executor.submit(ping, ip)
                        future_list.append(future.result())
                    resutl['ping'] = future_list
                    save_result(save_file, json.dumps(resutl))
                else:
                    executor.map(ping, ip_list)
            else:
                if save_file:
                    for port in range(21, 24):
                        future = executor.submit(tcp, ip_str, port)
                        future_list.append(future.result())
                    resutl['tcp'] = future_list
                    save_result(save_file, json.dumps(resutl))
                else:
                    for port in range(21, 24):
                        executor.submit(tcp, ip_str, port)
        except:
            pass


def thread_schema(num, ip_str, save_file=None):
    resutl = {}
    future_list = []
    with ThreadPoolExecutor(max_workers=num) as executor:
        try:
            # if action == 'ping':
            if isinstance(ip_str, list):
                ip_list = ip_split(ip_str)
                if save_file:
                    for ip in ip_list:
                        future = executor.submit(ping, ip)
                        future_list.append(future.result())
                    resutl['ping'] = future_list
                    save_result(save_file, json.dumps(resutl))
                else:
                    executor.map(ping, ip_list)
            else:
                if save_file:
                    for port in range(21, 24):
                        future = executor.submit(tcp, ip_str, port)
                        future_list.append(future.result)
                    resutl['tcp'] = future_list
                    save_result(save_file, json.dumps(resutl))
                else:
                    for port in range(21, 24):
                        executor.submit(tcp, ip_str, port)
        except:
            pass


def save_result(save_file, rt_value):
    with open(f'./{save_file}', 'a+', encoding='utf-8') as f:
        f.write(rt_value + '\n')


def check_ip(ip_str):
    compile_ip = re.compile(
        r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|'
        r'[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|'
        r'[0-1]\d{2}|[1-9]?\d)')
    if compile_ip.match(ip_str):
        return True
    else:
        print(compile_ip)
        return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='一个基于多进程或多线程模型的主机扫描器'
    )

    parser.add_argument(
        '-m',
        '--schema',
        type=str,
        help='通过参数 [-m proc|thread] 指定扫描器使用多进程或多线程模型'
    )
    parser.add_argument(
        '-n',
        '--num',
        default=1,
        type=int,
        help='指定并发数量, 默认并发数：1'
    )
    parser.add_argument(
        '-f',
        '--action',
        type=str,
        help='根据参数进行基于ping的IP网段检测，或者基于tcp的端口扫描'
    )
    parser.add_argument(
        '-ip',
        '--ip',
        type=str,
        help='连续 IP 地址, 支持格式例: -f tcp: xxx.xxx.xxx.xxx 或'
             '-f ping : xxx.xxx.xxx.xxx-xxx.xxx.xxx.xxx'
    )
    parser.add_argument('-w', '--save', type=str, help='扫描结果进行保存')
    args = parser.parse_args()

    if not args.schema:
        raise ValueError('请正确输入扫描模式，详见帮助：-m')

    if not args.ip:
        raise ValueError('请正确输入ip地址，详见帮助：-ip')

    if args.schema.lower() == 'thread':

        if args.action.lower() == 'ping':

            if args.ip.count('-', 0, len(args.ip)) != 1:
                raise ValueError('请根据扫描模式(-f)输入ip地址，详见帮助：-ip')

            start_ip, end_ip = args.ip.split('-')

            thread_schema(args.num, 'ping', args.ip, args.save)
        elif args.action.lower() == 'tcp':

            if not check_ip(args.ip):
                raise ValueError('请根据扫描模式(-f)输入ip地址，详见帮助：-ip')

            thread_schema(args.num, 'tcp', args.ip, args.save)

    elif args.schema.lower() == 'proc':

        if args.num > cpu_count():
            raise ValueError(f'proc模式下并发数<=当前系统cpu数量：{cpu_count()}')

        if args.action.lower() == 'ping':

            if args.ip.count('-', 0, len(args.ip)) != 1:
                raise ValueError('请根据扫描模式(-f)输入ip地址，详见帮助：-ip')

            process_schema(args.num, 'ping', args.ip, args.save)
        elif args.action.lower() == 'tcp':

            if not check_ip(args.ip):
                raise ValueError('请根据扫描模式(-f)输入ip地址，详见帮助：-ip')

            process_schema(args.num, 'tcp', args.ip, args.save)
        else:
            raise ValueError('请正确输入扫描模式，详见帮助：-m')
    else:
        print('请正确输入-m（proc/thread）')





