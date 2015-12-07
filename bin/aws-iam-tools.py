#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#[aws-iam-tools]
#
#Copyright (c) 2015 Masaru Kawabata
#
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

"""
[概要]
AWS-IAM関連ツール

[機能]
 - 指定されたIAMユーザーを削除する
"""

__authour__ = "masaru.kawabata"
__version__ = 0.1

from argparse import ArgumentParser
import boto3
import datetime
import logging
import logging.config
from logging import FileHandler
from logging import Formatter
from logging import StreamHandler
import os
import subprocess
import sys
import time
import yaml

def info_log(function_name, message):
    """
    インフォメーションレベルログ出力
    """
    logger.info(function_name + ' ' + message)

def error_log(function_name, message):
    """
    エラーレベルログ出力
    """
    logger.error(function_name + ' ' + message)

def get_os_env():
    """ OS環境変数を取得 """
    os.environ.items()
    if(os.environ['AWSIAMTOOLS'] != 'PRO' and os.environ['AWSIAMTOOLS'] != 'DEV'):
        print("Get Config Error")
        sys.exit(1)

    return os.environ['AWSIAMTOOLS']

def usage():
    """
    引数チェック
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ コマンドエラー時に表示する文字列 """
    desc = '{0} [Args] [Options]\nDetailed options -h or --help'.format(__file__)

    parser = ArgumentParser(description=desc)

    """ Argument Profile """
    parser.add_argument(
        '--profile',
        type = str,                          # 受け取る値の型を指定する
        dest = 'profile',                    # 保存先変数名
        required = True,                     # 必須項目
        help = 'AWS Account Profile Name'    # --help時に表示する文
    )

    """ Argument Delete User """
    parser.add_argument(
        '--delete-user',
        type = str,
        dest = 'delete_user',
        default = '',
        help = 'AWS Delete User'
    )

    """ 引数を解析 """
    args = parser.parse_args()

    return args    # オプションで指定した値は args.<変数名>で取得できる

def get_config():
    """
    config.ymlより各種設定を取得
    """
    if(osenv == "PRO"):
        with open("../conf/config.yml", 'r') as ymlfile:
            conf = yaml.load(ymlfile)
    else:
        with open("../conf/config_dev.yml", 'r') as ymlfile:
            conf = yaml.load(ymlfile)

    return conf

def iam_get_user(user):
    """
    引数で指定されたIAMユーザを削除
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        response = iam.get_user(UserName=user)
    except:
        info_log(sys._getframe().f_code.co_name, "IAM User Not Found: " + user)
        return 1

    info_log(sys._getframe().f_code.co_name, "IAM User Exist: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return 0

def iam_delete_user(user):
    """
    引数で指定されたIAMユーザを削除
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Check IAM User """
    user_flg = iam_get_user(user)

    if(user_flg == 1):
        info_log(sys._getframe().f_code.co_name, "End")
        sys.exit(1)
        
    """ Delete IAM User """
    try:
        response = iam.delete_user(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Delete IAM User Error")
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Deleted IAM User: " + user)
    info_log(sys._getframe().f_code.co_name, "End")

if __name__ == "__main__":
    """ Get OS ENV """
    osenv = get_os_env()

    """ Get Config """
    conf = get_config()

    logging.config.dictConfig(yaml.load(open(conf['logfile']).read()))
    logger = logging.getLogger(__name__)

    info_log(__name__, "Start")

    """ Argument Check """
    args = usage()

    """ Create Session """
    try:
        session = boto3.Session(profile_name = args.profile)
    except:
        print('Connection Error')
        sys.exit(1)

    """ Create Session Resource """
    try:
        iam = session.client('iam')
    except:
        print('Connection Error')
        sys.exit(1)

    """ Delete IAM User """
    if(args.delete_user != ""):
        iam_delete_user(args.delete_user)

    info_log(__name__, "End")
    sys.exit(0)

