TreeDiary API文档
===
## 通用
### 获取七牛云token
- GET /api/qtoken
- 参数：
	"file_name": 要上传的图片的文件名，注意应该保证文件名唯一，否则无法保证七牛云上资源文件不被覆盖
- 返回值：
    qtoken

## v1
### 使用SNS登录
- POST /api/v1/snsLogin/
- 参数：
    "sns_type": "1"/"2"/"3"(其中1是微博，2是QQ，3是微信);
    "nickname": 用户SNS上的昵称;
    "head_url": 头像地址;
    "open_id": 识别用户的唯一凭证
- 返回值：
    id, sns_type, nickname, head_url, open_id, token
    此token用来识别用户身份，需要用户身份识别的时候都需要POST这个token到服务端
    
### 发布纯文字状态
- POST /api/v1/status/text/
- 参数：
    "content": 文字
    "token"
- 返回值：
    "status_id"
    
### 发布文字和图片状态
- POST /api/v1/status/mix
- 参数:
    "token"
    "content"
    "pic_num"
    "pic_urls"
- 返回值:
    "status_id"
    
## v2
### 使用SNS登录
- POST /api/v2/snsLogin/
- sns_type(1:微博 2:QQ 3:微信), nickname, head_url, open_id
- 返回值:
    "token"(是后面用户认证的凭证)
    
### 发状态
- POST /api/v2/status/
- token, status_type(1:yellow 2:green 3:red), text, pic_url_str(将图片链接以']'分隔拼接起来),
    has_pic(1或0), pic_num
- 返回值:
    "status_id"一个字符串
    
### 删除状态
- DELETE /api/v2/status/<status_id>/
- token
- 返回值:
    空字符串或"status not exist"
    
### 修改用户信息
- PATCH /api/v2/user/
- token, token, yellow, green, blue, level, 除token外其余可选
- 返回值:
    空字符串