from xiaoai import *
import random


def outputJson(toSpeakText, is_session_end, openMic=True):
    xiaoAIResponse = XiaoAIResponse(to_speak=XiaoAIToSpeak(type_=0, text=toSpeakText), open_mic=openMic)
    response = xiaoai_response(XiaoAIOpenResponse(version="1.0",
                                                  is_session_end=is_session_end,
                                                  response=xiaoAIResponse))
    return response


def main(event):
    req = xiaoai_request(event)

    # return outputJson("感谢使用 I am ghostsf. type = " + str(req.request.type), True, False)

    if req.request.type == 0:
        return outputJson("欢迎来到智慧办公 by ghostsf", False)
    elif req.request.type == 1:
        if ((not hasattr(req.request, "slot_info")) or (not hasattr(req.request.slot_info, "intent_name"))):
            return outputJson("抱歉，我没有听懂", False)
        else:
            if req.request.slot_info.intent_name == 'open':

                return outputJson("已为您打开灯", False)
            elif req.request.slot_info.intent_name == 'close':
                return outputJson("已为您关闭灯", False)
            else:
                return outputJson("抱歉，我没有听懂", False)
    else:
        return outputJson("感谢使用智慧办公，下次再见", True, False)