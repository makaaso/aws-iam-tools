#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#[aws-iam-tools.py]
#
#Copyright (c) 2015 Masaru Kawabata
#
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

"""
[概要]
AWS-IAM関連ツール

[機能]
 - 指定されたIAMユーザを削除する
 - IAMユーザリストを表示する
"""

__authour__ = "masaru.kawabata"
__version__ = 0.11

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

    """ Argument Create User """
    parser.add_argument(
        '--create-user',
        type = str,
        dest = 'create_user',
        default = '',
        help = 'AWS Create IAM User'
    )

    """ Argument Delete User """
    parser.add_argument(
        '--delete-user',
        type = str,
        dest = 'delete_user',
        default = '',
        help = 'AWS Delete IAM User'
    )

    """ Argument List User """
    parser.add_argument(
        '--list',
        action = 'store_true',
        dest = 'list',
        help = 'AWS List IAM User'
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
    引数で指定されたIAMユーザの情報取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        userinfo = iam.get_user(UserName=user)
    except:
        info_log(sys._getframe().f_code.co_name, "IAM User Not Found: " + user)
        return 1

    info_log(sys._getframe().f_code.co_name, "IAM User Exist: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return 0

def iam_list_groups_for_user(user):
    """
    引数で指定されたIAMユーザにAttachされているグループリストを取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        group = iam.list_groups_for_user(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Get IAM User Group List: " + user)
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Get IAM User Group List: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return group['Groups']

def iam_list_access_keys(user):
    """
    引数で指定されたIAMユーザのAccessKeyリストを取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        accesskey = iam.list_access_keys(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Get IAM User AccessKey List: " + user)
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Get IAM User AccessKey List: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return accesskey['AccessKeyMetadata']

def iam_list_attached_user_policies(user):
    """
    引数で指定されたIAMユーザにAttachされているポリシーリストを取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        policy = iam.list_attached_user_policies(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Get IAM User Policy List: " + user)
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Get IAM User Policy List: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return policy['AttachedPolicies']

def iam_list_attached_user_policies(user):
    """
    引数で指定されたIAMユーザにAttachされているポリシーリストを取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        policy = iam.list_attached_user_policies(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Get IAM User Policy List: " + user)
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Get IAM User Policy List: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return policy['AttachedPolicies']

def iam_list_user_policies(user):
    """
    引数で指定されたIAMユーザ所有のポリシーリストを取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    try:
        inpolicy = iam.list_user_policies(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Get IAM User Inline Policy List: " + user)
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Get IAM User Inline Policy List: " + user)
    info_log(sys._getframe().f_code.co_name, "End")
    return inpolicy['PolicyNames']

def iam_create_user(user):
    """
    引数で指定されたIAMユーザを作成
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    userinfo = iam_get_user(user)
    if(userinfo == 0):
        return 1

    """ Create IAM User """
    try:
        response = iam.create_user(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Create IAM User Error")
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Create IAM User: " + user)
    info_log(sys._getframe().f_code.co_name, "End")

def iam_delete_user(user):
    """
    引数で指定されたIAMユーザを削除
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User """
    userinfo = iam_get_user(user)
    if(userinfo == 1):
        return 1

    """ Delete IAM User AccessKey """
    accesskey = iam_list_access_keys(user)

    for i in range(len(accesskey)):
        response = iam.delete_access_key(UserName = user, AccessKeyId = accesskey[i]['AccessKeyId'])
        info_log(sys._getframe().f_code.co_name, "Remove AccessKey: " + accesskey[i]['AccessKeyId'])
        
    """ Detach IAM User Group """
    group = iam_list_groups_for_user(user)

    for i in range(len(group)):
        response = iam.remove_user_from_group(GroupName = group[i]['GroupName'], UserName = user)
        info_log(sys._getframe().f_code.co_name, "Detach Group: " + group[i]['GroupName'])
        
    """ Detach IAM User Policy """
    policy = iam_list_attached_user_policies(user)

    for i in range(len(policy)):
        response = iam.detach_user_policy(UserName = user, PolicyArn = policy[i]['PolicyArn'])
        info_log(sys._getframe().f_code.co_name, "Detached Policy: " + policy[i]['PolicyName'])
        
    """ Delete IAM User Inline Policy """
    inpolicy = iam_list_user_policies(user)

    for i in range(len(inpolicy)):
        response = iam.delete_user_policy(UserName = user, PolicyName = inpolicy[i])
        info_log(sys._getframe().f_code.co_name, "Delete Policy: " + inpolicy[i])
        
    """ Delete IAM User Login Profile """
    try:
        response = iam.delete_login_profile(UserName=user)
    except:
        info_log(sys._getframe().f_code.co_name, "Login Profile Not Found ")
    else:
        info_log(sys._getframe().f_code.co_name, "Delete Login Profile: " + user)

    """ Delete IAM User """
    try:
        response = iam.delete_user(UserName=user)
    except:
        error_log(sys._getframe().f_code.co_name, "Delete IAM User Error")
        sys.exit(1)

    info_log(sys._getframe().f_code.co_name, "Deleted IAM User: " + user)
    info_log(sys._getframe().f_code.co_name, "End")

def iam_list_users():
    """
    IAMユーザリストを取得
    """
    info_log(sys._getframe().f_code.co_name, "Start")

    """ Get IAM User List """
    try:
        users = iam.list_users()
    except:
        error_log(sys._getframe().f_code.co_name, "Get IAM User Error")
        sys.exit(1)

    """ Display IAM User List """
    for i in range(len(users['Users'])):
        print(users['Users'][i]['UserName'])

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

    """ Create IAM User """
    if(args.create_user != ""):
        iam_create_user(args.create_user)
        info_log(__name__, "End")
        sys.exit(0)

    """ Delete IAM User """
    if(args.delete_user != ""):
        iam_delete_user(args.delete_user)
        info_log(__name__, "End")
        sys.exit(0)

    """ List IAM User """
    if(args.list == True):
        iam_list_users()
        info_log(__name__, "End")
        sys.exit(0)

    info_log(__name__, "Nothing to do")
    sys.exit(0)

