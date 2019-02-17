var mqtt = require('mqtt')
var url = process.argv[2]
var port = 443
var topic = '/topics/tests/my-aws-signv4-mqtt'
var messageRecieved = false
var client  = mqtt.connect(url,
    { 
        connectTimeout:5*1000,
        port: port,
    })
 
client.on('connect', function () {
  console.log('connected')
  client.subscribe(topic, function (err) {
    if (!err) {
      client.publish(topic, 'Hello mqtt')
    }
  })
})

client.on('close', function () {
    console.log('close')
    client.end()
    if(messageRecieved == false){
        throw new Error('Failed: Closed connection')
    }
  })

client.on('error', function () {
    console.log('error')
    client.end()
    throw new Error('Failed: Did not receive connection ack')
  })

  client.on('end', function () {
    console.log('end')
    client.end()
  })
 
client.on('message', function (topic, message) {
  console.log(message.toString())
  messageRecieved = true
  client.end()
})