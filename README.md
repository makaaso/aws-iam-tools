aws-iam-tools
------------

#### 概要

* AWS-IAM関連ツール

#### 機能

* 指定されたIAMユーザーを削除する

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

