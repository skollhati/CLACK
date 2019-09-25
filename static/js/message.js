var current_speech = "";
var last_date = ""; // 현재 대비 3일전
function previous_message(parentTag,messages)
{
    $.each(messages,function(index,value)
    {
        receive_message(parentTag,value);
    });
}

function receive_message(parentTag,message)
{
    if(last_date !== message.datetime)
    {
        $('#'+parentTag).appendTo($(

        ));
        last_date = message.datetime;
    }
    if(current_speech !== message.id)
    {
        $('#'+parentTag).appendTo($(
            "<div class='d-inline-flex'>"
                +"<div name='profile-image'>"
                    + message.datetime
                + "</div>"
                + "<div class='flex-fill'>"
                    + "<div>" + message.id +" "+message.datetime
                    + "</div>"
                    + "<div>"
                    + message.message
                    + "</div>"
                + "</div>"
            +"</div>"));
        current_speech = message.id;
    }else{
        $('#'+parentTag).appendTo($("<div class='d-inline-flex'>"
            +"<div class='message-col-1' name='datetime'>"
            + message.datetime
            + "</div>"
            + "<div class='flex-fill'>"
            + message.message
            + "</div>"
            +"</div>"));
    }


}