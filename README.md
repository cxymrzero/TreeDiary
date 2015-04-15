TreeDiary API文档
===
## 通用
### 获取七牛云token
- /api/qtoken
- 参数：
	"file_name": 要上传的图片的文件名，注意应该保证文件名唯一，否则无法保证七牛云上资源文件不被覆盖
- 返回值：
    qtoken

## v1
### 使用SNS登录
- /api/v1/snsLogin/
- 参数：
    "sns_type": "1"/"2"/"3"(其中1是微博，2是QQ，3是微信);
    "nickname": 用户SNS上的昵称;
    "head_url": 头像地址;
    "open_id": 识别用户的唯一凭证
- 返回值：
    id, sns_type, nickname, head_url, open_id, token
    此token用来识别用户身份，需要用户身份识别的时候都需要POST这个token到服务端