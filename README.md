aws-iam-tools
------------

#### 概要

* AWS-IAM関連ツール

#### 機能

* 指定されたIAMユーザを削除する
* IAMユーザリストを表示する
* 指定されたIAMユーザを作成する
* 指定されたIAMユーザにポリシーをアタッチする
* 指定されたIAMユーザのポリシーリストを表示する

#### 前提条件

* virtualenvwrapperインストール済み
* ~/.boto にプロファイル登録済み

#### 動作確認環境

* Ubuntu14.04
* python3.4

#### 環境設定

```
mkdir /opt/aws/aws-iam-tools/log
export AWSIAMTOOLS=<PRO or DEV>
mkvirtualenv reporting3.4 --python=/usr/local/bin/python3.4
workon reporting3.4
pip install boto3
pip install pyyaml
pip install argparse
```

#### 使用方法

##### IAMユーザ削除

```
python aws-iam-tools.py --profile <PROFILE> --delete-user --user <USER>
```

##### IAMユーザリスト表示

```
python aws-iam-tools.py --profile <PROFILE> --list-user
```

##### IAMユーザ作成

```
python aws-iam-tools.py --profile <PROFILE> --create-user --user <USER>
```

##### IAMユーザポリシーアタッチ

```
python aws-iam-tools.py --profile <PROFILE> --attach-user-policy --user <USER> --policy <POLICY>
```

##### IAMユーザポリシーリスト表示

```
python aws-iam-tools.py --profile <PROFILE> --list-user
```

