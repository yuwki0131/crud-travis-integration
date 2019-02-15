# travis内でdockerを起動させるテスト

[![Build Status](https://travis-ci.org/yuwki0131/crud-travis-integration.svg?branch=master)](https://travis-ci.org/yuwki0131/crud-travis-integration)

1. docker(db)を起動
   docker-compose up
1. db migration/初期化
   alembic
1. DBアクセスを行うテストコード実行
   python3
