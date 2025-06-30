import os 
CHANNEL_ACCESS_TOKEN=os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET=os.getenv("CHANNEL_SECRET")


from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    TemplateMessage,
    ButtonsTemplate,
    PostbackAction, 
    ConfirmTemplate,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    MessageAction,
    URIAction,
    DatetimePickerAction,
    CameraAction,
    CameraRollAction,
    LocationAction
)
from linebot.v3.webhooks import (
    MessageEvent,
    FollowEvent,
    UnfollowEvent,
    TextMessageContent,
    PostbackEvent
)

app = Flask(__name__)

configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)

lineHandler = WebhookHandler(CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        lineHandler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 加好友
@lineHandler.add(FollowEvent)
def handle_follow(event):
    print(f'新增 {event.type}')
# 解除好友
@lineHandler.add(UnfollowEvent)
def handle_un_follow(event):
    print(f'新增 {event.type}')    


@lineHandler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        
        if event.message.text == '開始作答':
            # url = request.url_root + 'static/q1.jpg'
            # url = url.replace("http", "https")
            # app.logger.info("url=" + url)
            buttons_template = ButtonsTemplate(
                # thumbnail_image_url=url,
                title='1/40',
                text="一、我是一個：",
                actions=[
                    # URIAction(label='連結', uri='https://www.facebook.com/NTUEBIGDATAEDU'),
                    # PostbackAction(label='回傳值', data='ping', displayText='傳了'),
                    PostbackAction(label='A.勤勞的人，不停的工作', data='A1', text='A-1'),
                    PostbackAction(label='B.活力充沛的人，總是充滿活力', data='B1', text='B-1'),
                    PostbackAction(label='C.和氣的人，易相處', data='C1', text='C-1'),
                    PostbackAction(label='D.完美主義者，希望事物都要有秩序', data='D-1', text='D1')
                    # DatetimePickerAction(label="選擇時間", data="時間", mode="datetime"),
                    # CameraAction(label='拍照'),
                    # CameraRollAction(label='選擇相片'),
                    # LocationAction(label='選擇位置')
                ]
            )
            template_message = TemplateMessage(
                alt_text="This is a buttons template",
                template=buttons_template
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[template_message]
                )
            )
        elif event.message.text.endswith('-1'):           
            buttons_template = ButtonsTemplate(
                title='2/40',
                text="二、生活中，我總是表現得：",
                actions=[                    
                    PostbackAction(label='A.不斷進取，希望推動改變', data='A2', text='A-2'),
                    PostbackAction(label='B.生機勃勃，對生活充滿熱情與興奮', data='B2', text='B-2'),
                    PostbackAction(label='C.滿足現狀，容易接受任何情況與環境', data='C2', text='C-2'),
                    PostbackAction(label='D.謹慎小心，對周圍的人事過分關心和敏感', data='D2', text='D-2')                    
                ]
            )
            template_message = TemplateMessage(
                alt_text="This is a buttons template",
                template=buttons_template
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[template_message]
                )
            )
        elif event.message.text.endswith('-2'):          
            buttons_template = ButtonsTemplate(              
                title='3/40',
                text="三、我覺得自己屬於：",
                actions=[                  
                    PostbackAction(label='A.喜歡挑戰，願意面對新事物', data='A3', text='A-3'),
                    PostbackAction(label='B.讓人開心，喜歡與他人相處', data='B3', text='B-3'),
                    PostbackAction(label='C.適應能力強', data='C3', text='C-3'),
                    PostbackAction(label='D.善於分析', data='D3', text='D-3')                  
                ]
            )
            template_message = TemplateMessage(
                alt_text="This is a buttons template",
                template=buttons_template
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[template_message]
                )
            )   
        elif event.message.text.endswith('-3'):          
            buttons_template = ButtonsTemplate(              
                title='4/40',
                text="四、對於任務，我願意做：",
                actions=[                  
                    PostbackAction(label='A.指揮者，自己身先士卒', data='A4', text='A-4'),
                    PostbackAction(label='B.發動者，發動和鼓勵別人參與', data='B4', text='B-4'),
                    PostbackAction(label='C.跟隨者，跟隨他人持續做下去', data='C4', text='C-4'),
                    PostbackAction(label='D.計畫者，先做計畫，並嚴格進行', data='D4', text='D-4')                  
                ]
            )
            template_message = TemplateMessage(
                alt_text="This is a buttons template",
                template=buttons_template
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[template_message]
                )
            )    
        elif event.message.text.endswith('-40'):
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='感謝您的作答，祝您面試順利')]
            ))           
        elif event.message.text.endswith('關鍵字'):
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='公司官網'),TextMessage(text='財務報表')]
            ))           
        elif event.message.text.endswith('公司官網'):
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='https://www.darwinprecisions.com/zh-tw')]
            ))  
        elif event.message.text.endswith('財務報表'):
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='https://www.darwinprecisions.com/zh-tw/investors-2.php')]
            ))  
          
              
        else:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='請輸入：開始作答')]
            ))

@lineHandler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'postback':
        print('Postback event is triggered')


if __name__ == "__main__":
    app.run()