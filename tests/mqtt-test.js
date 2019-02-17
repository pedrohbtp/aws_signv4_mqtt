var mqtt = require('mqtt')
url = '<your_signed_url>'
port = 443
topic = '<your_topic>'
i = 0
 
var client  = mqtt.connect(url,
    { 
        connectTimeout:5*1000,
        port: port,
    })
 
client.on('connect', function () {
  client.subscribe(topic, function (err) {
    if (!err) {
      client.publish(topic, 'Hello mqtt')
    }
  })
})
 
client.on('message', function (topic, message) {
  console.log(message.toString())
  i = i+1
  client.publish(topic, 'Hello mqtt '+String(i))
})