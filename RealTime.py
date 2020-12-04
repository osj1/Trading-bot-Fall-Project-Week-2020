import config
import websocket, json

#API_Key = "PKRJJ2QQ0IU0TXNKXFCU"
#Secret_Key = "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm"

def on_open(ws):
	print("Opened")
	auth_data = {
		"action": "authenticate",
		"data": {"key_id": config.API_Key, "secret_key": config.Secret_Key}
	} 

	ws.send(json.dumps(auth_data)) 

	listen_message = {"action": "listen", "data": {"streams": ["AM.TSLA"]}}

	ws.send(json.dumps(listen_message))


def on_message(ws, message): 
	print("Recieved a message")
	print(message)

def on_close(ws):
	print("Closed connection")


socket = "wss://data.alpaca.markets/stream" 

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()


#https://www.youtube.com/watch?v=Mv6c_9FqNx4
#Line 10: Signals that the interface is ready to recieve data, logs into Alpaca with personal key id and secret key
	#creates variable auth_data, defienes course of action in order to log into alpaca 
#Line 13: sends message, .dumps converts it to json stream. json - receives, stores, and transports data


	#channel_data = {
		#"action": "subscribe"
		#"params": "AM.TSLA"
	#}
#Line 17: websocket creates a two way stream between the server and terminal/browser, 'dumps' variable listen_message into new enviroment
#the code 'ws.send(json.dumps(...)' is important to pulling data and displaying data because it signals the relationship
#between the stream and my terminal
#Line 19: the websocket recieves a message and that message is displayed