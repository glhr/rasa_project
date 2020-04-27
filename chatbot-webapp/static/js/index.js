import * as socket from './socketio_client.js';

export function addUserMessage(msg) {
	addUserMessageToList(msg);
	socket.sendUserMessage(msg);
}

export function receivedBotMessage(data) {
	console.log("-> receivedBotMessage")
	if (data.text) {
		console.log('Data:'+data.text)
		addBotMessageToList(data.text, 'text');
	}
	else if (data.attachment) {
		if (data.attachment.type == 'image') {
			addBotMessageToList(data.attachment.payload.src, 'image');
		}

	}
}

import 'materialize-css/dist/css/materialize.min.css'
import 'materialize-css/dist/js/materialize.min.js'

var $ = require("jquery");

function scrollDown() {
	var d = $('#msg_ul');
	d.scrollTop(d.prop("scrollHeight"));
}

function addBotMessageToList(data, type) {
		if (type == 'text') {
			console.log("-> addBotMessageToList " + type)
			$('#msg_ul').append('<li class="collection-item botmsg_li"><span class="botmsg_span speech-bubble speech-bubble-right">'+data+'</span></li>');
		}
		else if (type == 'image') {
			console.log("-> addBotMessageToList " + type)
			$('#msg_ul').append('<li class="collection-item botmsg_li"><span class="botmsg_span speech-bubble speech-bubble-right"><img src="'+data+'"></span></li>');
		}
		scrollDown();
}

function addUserMessageToList(data) {
	console.log("-> addUserMessageToList")
    $("#msg_ul").append('<li class="collection-item usermsg_li"><span class="usermsg_span speech-bubble speech-bubble-left">'+data+'</span></li>');
		scrollDown();
}

$('#user_input_form').submit(function(e) {
    // get all the inputs into an array.
		e.preventDefault();
		var msg = $("#user_input").val();
		console.log("user input " + msg);
		addUserMessage(msg);
		$("#user_input").val('');
});
