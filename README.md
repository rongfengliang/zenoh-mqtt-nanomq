# zenoh mqtt plugin with nanomq 

> for support share subscription

## test command

* pub  topic message

```code
 mqttx pub -h 'localhost' -p 1883   --topic demo -s --stdin --multiline
```

* sub

```code
mqttx sub -h 'localhost' -p 1883 --topic 'demo/demo'

share topic

mqttx sub -h 'localhost' -p 2883 --topic '$share/app/demo'
```

## some links

[zenoh-mqtt](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt)

[mqttx](https://mqttx.app/zh)

[introduction-to-mqtt5-protocol-shared-subscription](https://www.emqx.com/zh/blog/introduction-to-mqtt5-protocol-shared-subscription)
