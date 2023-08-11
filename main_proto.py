import proto


class Callback(proto.Message):
    phone_number = proto.Field(proto.STRING, number=1)
    send_time = proto.Field(proto.STRING, number=2)
    report_time = proto.Field(proto.STRING, number=3)
    success = proto.Field(proto.BOOL, number=4)
    err_code = proto.Field(proto.STRING, number=5)
    err_msg = proto.Field(proto.STRING, number=6)
    sms_size = proto.Field(proto.STRING, number=7)
    biz_id = proto.Field(proto.STRING, number=8)
    out_id = proto.Field(proto.STRING, number=9)


class SendVerifyCodeResponse(proto.Message):
    Message = proto.Field(proto.STRING, number=1)
    RequestId = proto.Field(proto.STRING, number=2)
    Code = proto.Field(proto.STRING, number=3)
    BizId = proto.Field(proto.STRING, number=4)


class SmsSendDetailDTO(proto.Message):
    ErrCode = proto.Field(proto.STRING, number=1)
    TemplateCode = proto.Field(proto.STRING, number=2)
    OutId = proto.Field(proto.STRING, number=3)
    ReceiveDate = proto.Field(proto.STRING, number=4)
    SendDate = proto.Field(proto.STRING, number=5)
    PhoneNum = proto.Field(proto.STRING, number=6)
    Content = proto.Field(proto.STRING, number=7)
    SendStatus = proto.Field(proto.INT64, number=8)


class SmsSendDetailDTOs(proto.Message):
    SmsSendDetailDTO = proto.Field(SmsSendDetailDTO, number=1)


class CheckStatusResponse(proto.Message):
    Code = proto.Field(proto.STRING, number=1)
    Message = proto.Field(proto.STRING, number=2)
    RequestId = proto.Field(proto.STRING, number=3)
    TotalCount = proto.Field(proto.INT64, number=4)
    SmsSendDetailDTOs = proto.Field(SmsSendDetailDTOs, number=5)


