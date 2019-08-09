response_pay_tmp_succuss = {
    "alipay_trade_pay_response": {
        "code": "10000",
        "msg": "Success",
        "trade_no": "2019082011001004330000121536",
        "out_trade_no": "6823789339978248",
        "buyer_logon_id": "159****5620",
        "total_amount": 120.88,
        "receipt_amount": "88.88",
        "gmt_payment": "2014-11-27 15:45:57",
        "fund_bill_list": [
            {
                "fund_channel": "ALIPAYACCOUNT",
                "bank_code": "CEB",
                "amount": 10,
                "real_amount": 11.21
            }
        ],
        "buyer_user_id": "2088101117955611",

    },
    "sign": ""
}
response_pay_tmp_fail = {
    "alipay_trade_pay_response": {"code": "20000", "msg": "Service Currently Unavailable"},
    "sign": ""
}
response_refund_tmp_succuss= {
    "alipay_trade_cancel_response": {
        "code": "10000",
        "msg": "Success",
        "trade_no": "2013112011001004330000121536",
        "out_trade_no": "6823789339978248",
        "retry_flag": "N",
        "action": "close",
        "gmt_refund_pay": "2016-11-27 15:45:57",
        "refund_settlement_id": "2018101610032004620239146945"
    },
    "sign": ""
}
response_refund_tmp_fail = {
    "alipay_trade_refund_response": {"code": "20000", "msg": "Service Currently Unavailable"},
    "sign": ""
}
response_cancel_tmp_succuss = {
    "alipay_trade_cancel_response": {
        "code": "10000",
        "msg": "Success",
        "trade_no": "2013112011001004330000121536",
        "out_trade_no": "6823789339978248",
        "retry_flag": "N",
        "action": "close",
        "gmt_refund_pay": "2016-11-27 15:45:57",
        "refund_settlement_id": "2018101610032004620239146945"
    },
    "sign": ""
}
response_cancel_tmp_fail = {
    "alipay_trade_cancel_response": {"code": "20000", "msg": "Service Currently Unavailable"},
    "sign": ""
}
response_query_tmp_succuss = {
    "alipay_trade_query_response": {
        "code": "10000",
        "msg": "Success",
        "trade_no": "2013112011001004330000121536",
        "out_trade_no": "6823789339978248",
        "buyer_logon_id": "159****5620",
        "trade_status": "TRADE_CLOSED",
        "total_amount": 88.88,
        "trans_currency": "TWD",
        "settle_currency": "USD",
        "settle_amount": 2.96,
        "pay_currency": 1,
        "pay_amount": "8.88",
        "settle_trans_rate": "30.025",
        "trans_pay_rate": "0.264",
        "buyer_pay_amount": 8.88,
        "point_amount": 10,
        "invoice_amount": 12.11,
        "send_pay_date": "2014-11-27 15:45:57",
        "receipt_amount": "15.25",
        "store_id": "NJ_S_001",
        "terminal_id": "NJ_T_001",
        "fund_bill_list": [
            {
                "fund_channel": "ALIPAYACCOUNT",
                "bank_code": "CEB",
                "amount": 10,
                "real_amount": 11.21
            }
        ],
        "store_name": "证大五道口店",
        "buyer_user_id": "2088101117955611",
        "charge_amount": "8.88",
        "charge_flags": "bluesea_1",
        "settlement_id": "2018101610032004620239146945",
        "trade_settle_info": {
            "trade_settle_detail_list": [
                {
                    "operation_type": "replenish",
                    "operation_serial_no": "2321232323232",
                    "operation_dt": "2019-05-16 09:59:17",
                    "trans_out": "208811****111111",
                    "trans_in": "208811****111111",
                    "amount": 10
                }
            ]
        },
        "auth_trade_pay_mode": "CREDIT_PREAUTH_PAY",
        "buyer_user_type": "PRIVATE",
        "mdiscount_amount": "88.88",
        "discount_amount": "88.88",
        "buyer_user_name": "菜鸟网络有限公司",
        "subject": "Iphone6 16G",
        "body": "Iphone6 16G",
        "alipay_sub_merchant_id": "2088301372182171",
        "ext_infos": "{\"action\":\"cancel\"}"
    },
    "sign": "ERITJKEIJKJHKKKKKKKHJEREEEEEEEEEEE"
}
response_query_tmp_fail = {
    "alipay_trade_query_response": {"code": "20000", "msg": "Service Currently Unavailable"},
    "sign": ""
}
code_msg = {"10000": "Succuss",
            "20000": "Service Currently Unavailable",
            "20001": "Insufficient authorization",
            "40001": "Missing required parameters",
            "40002": "Illegal parameters",
            "40004": "Business processing failed",
            "40006": "Insufficient permissions"
            }
request_data_tmp = {
    "TransId": "OT001",
    "app_id": "2017083008461617",
    "biz_content": {
        "out_trade_no": "bryan190729153342983",
        "scene": "bar_code",
        "auth_code": "281853223323927209",
        "subject": "ali pay",
        "total_amount": "00000000.01",
        "store_id": "NJ1"
    },
    "charset": "gbk",
    "format": "JSON",
    "insUrl": "https://openapi.alipay.com/gateway.do",
    "method": "alipay.trade.pay",
    "sign_type": "RSA2",
    "timestamp": "2019-07-29 15:30:44",
    "version": "1.0",
    "webId": "2017083008461617_20190729153044000000078221",
    "sign": "D8znPnnNh5XC28r0tLa6qb7Qw9ooU9yoszM4RavujDx"
            "+lthnDGO9F7HdxHCfSMfkDVoT2OGfy61w4ThNfJqJkWVs5I9n3zktbS9qiKSyuXmTSZblfYXZ+++6TlpJzH8Y9o/WARkwrqme"
            "/SCoP26d1U8Bx6DxwueDFFokQh0v7OQroFdX4B8xML7eQfTXVja+3vzbSG2YtXvIkb7xd7zHta44QszjuHYTabHvakV67dMfW"
            "+c1MHKa3zm0ylBxafroOV1uqoJ4Jwgpz/Zpjk5QvkXvZvcLdRI+anEKznl5zPp7mMD5m/wOi"
            "/vXvFJscJ3jasU4Co1K10CeZoOfsqwJkg== "
}
