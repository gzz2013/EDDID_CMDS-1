import time
import hmac
import hashlib
import base64
import urllib
import json
import requests
import logging

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


def is_not_null_and_blank_str(content):
    if content and content.strip():
        return True
    else:
        return False


class DingtalkRobot(object):
    def __init__(self, webhook, sign=None):
        super(DingtalkRobot, self).__init__()
        self.webhook = webhook
        self.sign = sign
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.times = 0
        self.start_time = time.time()

    # 加密签名
    def __spliceUrl(self):
        timestamp = int(round(time.time() * 1000))
        secret = self.sign
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = f"{self.webhook}&timestamp={timestamp}&sign={sign}"
        return url

    def send_text(self, msg, is_at_all=False, at_mobiles=[]):
        data = {"msgtype": "text", "at": {}}
        if is_not_null_and_blank_str(msg):
            data["text"] = {"content": msg}
        else:
            logging.error("text类型，消息内容不能为空！")
            raise ValueError("text类型，消息内容不能为空！")

        if is_at_all:
            data["at"]["isAtAll"] = is_at_all

        if at_mobiles:
            at_mobiles = list(map(str, at_mobiles))
            data["at"]["atMobiles"] = at_mobiles

        logging.debug('text类型：%s' % data)
        return self.__post(data)

    # def send_text(self, msg, is_at_all=False, at_mobiles=[]):
    #     # data = {"msgtype": "text", "at": {}}
    #     localtime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    #     data = {
    #         "msgtype": "link",
    #         "link": {
    #             "text": localtime,
    #             # 钉钉机器人签名
    #             "title": {},
    #             "picUrl": "",
    #             # 自动化测试报告URL
    #             "messageUrl":at_mobiles
    #             # "messageUrl": "http://192.168.57.23:8080/job/cdm_automated_testing/HTML_20Report/"
    #         }
    #     }
    #     if is_not_null_and_blank_str(msg):
    #         data["link"] = {"content": msg}
    #     else:
    #         logging.error("text类型，消息内容不能为空！")
    #         raise ValueError("text类型，消息内容不能为空！")
    #
    #     if is_at_all:
    #         data["at"]["isAtAll"] = is_at_all
    #
    #     if at_mobiles:
    #         at_mobiles = list(map(str, at_mobiles))
    #         data["link"]["messageUrl"] = at_mobiles
    #
    #     logging.debug('text类型：%s' % data)
    #     return self.__post(data)



    def __post(self, data):
        """
        发送消息（内容UTF-8编码）
        :param data: 消息数据（字典）
        :return: 返回发送结果
        """
        self.times += 1
        if self.times > 20:
            if time.time() - self.start_time < 60:
                logging.debug('钉钉官方限制每个机器人每分钟最多发送20条，当前消息发送频率已达到限制条件，休眠一分钟')
                time.sleep(60)
            self.start_time = time.time()

        post_data = json.dumps(data)
        try:
            response = requests.post(self.__spliceUrl(), headers=self.headers, data=post_data)
        except requests.exceptions.HTTPError as exc:
            logging.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("消息发送失败, Request Exception!")
            raise
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                logging.error("服务器响应异常，状态码：%s，响应内容：%s" % (response.status_code, response.text))
                return {'errcode': 500, 'errmsg': '服务器响应异常'}
            else:
                logging.debug('发送结果：%s' % result)
                if result['errcode']:
                    error_data = {"msgtype": "text", "text": {"content": "钉钉机器人消息发送失败，原因：%s" % result['errmsg']},
                                  "at": {"isAtAll": True}}
                    logging.error("消息发送失败，自动通知：%s" % error_data)
                    requests.post(self.webhook, headers=self.headers, data=json.dumps(error_data))
                return result


if __name__ == '__main__':
    gg="http://192.168.57.23:8080/job/cdm_automated_testing/HTML_20Report/"
    URL = "https://oapi.dingtalk.com/robot/send?access_token=fb8e9870d1a020b0e0b4c139b9455c399d39c80030545c7ced062afa5b5dac6a"
    SIGN = "SEC9a6de92ce7dd912a35823cce657a94320f1e28d9282bcafbd26afd199ed8b8de"
    ding = DingtalkRobot(URL, SIGN)
    print(ding.send_text("Hello World",gg))