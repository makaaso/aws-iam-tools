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
* IAMユーザ名を変更する
* IAMユーザ作成機能にパスワード設定機能を追加
* 指定されたIAMユーザのポリシーをデタッチする

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
python aws-iam-tools.py --profile <PROFILE> --create-user --user <USER> --password <PASSWORD>
python aws-iam-tools.py --profile <PROFILE> --create-user --user <USER> --password <PASSWORD> --reset-required
```

##### IAMユーザポリシーアタッチ

```
python aws-iam-tools.py --profile <PROFILE> --attach-user-policy --user <USER> --policy <POLICY>
```

##### IAMユーザポリシーリスト表示

```
python aws-iam-tools.py --profile <PROFILE> --list-user
```

##### IAMユーザ名変更

```
python aws-iam-tools.py --profile <PROFILE> --modify-user-name --user <USER> --newuser <NEWUSER>
```

##### IAMユーザポリシーデタッチ

```
python aws-iam-tools.py --profile <PROFILE> --detach-user-policy --user <USER> --policy <POLICY>
```

