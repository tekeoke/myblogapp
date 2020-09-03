# 参考記事
https://qiita.com/str416yb/items/7324b99b9f05b9089b80


# docker-compose をして作成された全てのものを削除
```
docker-compose down --rmi all --volumes
```

```
docker run --rm \
--mount type=bind,src=$(pwd),dst=/opt/apps \
django2.1
```