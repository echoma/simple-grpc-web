# 说明

协议文件用的就是grpc官方的Echo服务的例子。

grpc的数据流是这样的：`grpc-web的客户端`->`envoy gateway`->`server.py服务端`

## envoy网关

#### 启动envoy

```shell
sudo docker run -d -p 8080:8080 -p 9901:9901 echo/envoy
```

#### 其他

###### 构建envoy镜像

```shell
sudo docker build -t echo/envoy -f ./envoy.Dockerfile .
```

## 服务端

服务端是基于Python3.7的，监听端口是1443

#### python安装依赖

```shell
python -m pip install -r requirements.txt
```

#### 启动服务端

```bash
python3.7 ./server.py
```

#### 其他

###### 编译proto

注意编译前，先安装grpcio-tools。可以在[官方链接](https://grpc.io/docs/tutorials/basic/python/)里看到grpcio-tools的安装和使用方法。

```shell
# 在仓库根目录执行
python3.7 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ echo.proto
```

## 客户端

客户端是基于WEB的网页+js，连接envoy的8080端口

#### 启动HTTP服务器

HTTP服务用于加载页面、js等静态资源，我们这里用了`nginx`，使用仓库里`grpc-web-test.conf`这个配置就可以

#### 其他

###### 编译proto

注意编译前，先安装protoc的grpc-web插件。可以在[官方链接](https://github.com/grpc/grpc-web)看到安装和使用方法。

```shell
protoc -I=./ echo.proto --js_out=import_style=commonjs:./ --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./
```

###### webpack打包js

```shell
# 在仓库根目录执行
npm install
npx webpack client.js
```

