#!/usr/bin/env python3.7
# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
import re
from AliPay.response_data import *
from Pay.myrsa import rsa_sign, rsa_verify
import time
import datetime
import random
code_now = "10000"
msg_now = "Succuss"
delay = 0


# Create your views here.

def pay(request):
    action = "alipay_trade_pay_response"
    # 验证请求签名
    verrify_ok = verify_sign(request)
    # 读取请求数据 写入到响应数据中
    if code_now == "10000" and verrify_ok:
        response = pay_request2response(request)
    elif not verrify_ok:
        response = response_pay_tmp_fail
        response[action]["code"] = "40002"
        response[action]["msg"] = "Illegal parameters"
        response[action]["sub_code"] = "isv.invalid-signature"
        response[action]["sub_msg"] = "Invalid signature"
    else:
        response = response_pay_tmp_fail
        response[action]["code"] = code_now
        response[action]["msg"] = msg_now
    # 生成响应签名
    response["sign"] = create_sign(action, response)
    # 转为json
    res = json.dumps(response)

    return HttpResponse(_delay(res))


def refund(request):
    action = "alipay_trade_refund_response"
    # 验证签名
    verrify_ok = verify_sign(request)
    # 读取请求数据 写入到响应数据中
    if code_now == "10000" and verrify_ok:
        response = refund_request2response(request)
    elif not verrify_ok:
        response = response_pay_tmp_fail
        response[action]["code"] = "40002"
        response[action]["msg"] = "Illegal parameters"
        response[action]["sub_code"] = "isv.invalid-signature"
        response[action]["sub_msg"] = "Invalid signature"
    else:
        response = response_refund_tmp_fail
        response[action]["code"] = code_now
        response[action]["msg"] = msg_now
    # 生成响应签名
    response["sign"] = create_sign(action, response)
    # 转为json
    res = json.dumps(response)

    return HttpResponse(_delay(res))


def cancel(request):
    action = "alipay_trade_cancel_response"
    # 验证签名
    verrify_ok = verify_sign(request)
    # 读取请求数据 写入到响应数据中
    if code_now == "10000" and verrify_ok:
        response = cancel_request2response(request)
    elif not verrify_ok:
        response = response_pay_tmp_fail
        response[action]["code"] = "40002"
        response[action]["msg"] = "Illegal parameters"
        response[action]["sub_code"] = "isv.invalid-signature"
        response[action]["sub_msg"] = "Invalid signature"
    else:
        response = response_cancel_tmp_fail
        response[action]["code"] = code_now
        response[action]["msg"] = msg_now
    # 生成响应签名
    response["sign"] = create_sign(action, response)
    # 转为json
    res = json.dumps(response)

    return HttpResponse(_delay(res))


def query(request):
    action = "alipay_trade_query_response"
    # 验证签名
    verrify_ok = verify_sign(request)
    # 读取请求数据 写入到响应数据中
    if code_now == "10000" and verrify_ok:
        response = query_request2response(request)
    elif not verrify_ok:
        response = response_pay_tmp_fail
        response[action]["code"] = "40002"
        response[action]["msg"] = "Illegal parameters"
        response[action]["sub_code"] = "isv.invalid-signature"
        response[action]["sub_msg"] = "Invalid signature"
    else:
        response = response_query_tmp_fail
        response[action]["code"] = code_now
        response[action]["msg"] = msg_now
    # 生成响应签名
    response["sign"] = create_sign(action, response)
    # 转为json
    res = json.dumps(response)

    return HttpResponse(_delay(res))

def _delay(res):
    if delay > 0:
        time.sleep(float(delay / 1000.0))
    return res


def setting(request):
    return render(request, 'alipay/setting_response.html')


def save_setting(request):  # 配置响应结果setting
    result = request.POST.get('result')
    response_delay = request.POST.get('response_delay')
    global code_now, msg_now, delay
    code_now = result
    msg_now = code_msg[code_now]
    delay = int(response_delay)
    print("set code=", code_now, ",msg=", msg_now, ",delay=", delay)
    return render(request, 'alipay/setting_result.html')


def pay_request2response(request):
    response = response_pay_tmp_succuss
    rq = request.POST
    biz_str = rq.get('biz_content')
    biz_str = re.sub('\'', '\"', biz_str)
    biz_data = json.loads(biz_str)
    time1 = time.strftime("%Y%m%d%H%M%S")
    num = random.randint(10000000000000, 99999999999999)
    num = str(num)
    trade_no = time1+num
    response['trade_no'] = trade_no
    response['out_trade_no'] = biz_data['out_trade_no']
    response['total_amount'] = biz_data['total_amount']
    if 'discountable_amount' in biz_data:
        real_amount = float(response['total_amount']) - float(biz_data['discountable_amount'])
        response['receipt_amount'] = str(real_amount)
    else:
        response['receipt_amount'] = biz_data['total_amount']
    response['gmt_payment'] = rq['timestamp']
    return response


def refund_request2response(request):
    response = response_refund_tmp_succuss
    rq = request.POST
    biz_str = rq.get('biz_content')
    biz_str = re.sub('\'', '\"', biz_str)
    biz_data = json.loads(biz_str)
    response['out_trade_no'] = biz_data['out_trade_no']
    response['trade_no'] = biz_data['trade_no']
    return response


def cancel_request2response(request):
    response = response_cancel_tmp_succuss
    rq = request.POST
    biz_str = rq.get('biz_content')
    biz_str = re.sub('\'', '\"', biz_str)
    biz_data = json.loads(biz_str)
    response['out_trade_no'] = biz_data['out_trade_no']
    response['trade_no'] = biz_data['trade_no']
    return response


def query_request2response(request):
    response = response_query_tmp_succuss
    rq = request.POST
    time1 = time.strftime("%Y%m%d%H%M%S")
    num = random.randint(10000000000000, 99999999999999)
    num = str(num)
    trade_no = time1 + num
    response['trade_no'] = trade_no
    biz_str = rq.get('biz_content')
    biz_str = re.sub('\'', '\"', biz_str)
    biz_data = json.loads(biz_str)
    response['out_trade_no'] = biz_data['out_trade_no']
    #response['trade_no'] = biz_data['trade_no']
    return response


def verify_sign(request):
    sign = request.POST.get('sign')
    message = request.POST.get('app_id')
    return rsa_verify(sign, message)


def create_sign(action, response):
    message = response[action]
    message = json.dumps(message)
    sign = rsa_sign(message)
    return sign.decode("utf-8")
