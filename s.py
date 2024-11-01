import	time
import	zenoh
conf	=	zenoh.Config.from_json5("""
							   {"id":"222222","mode":	"client","connect":{"endpoints":["tcp/127.0.0.1:7447"]}}
							   """)
session	=	zenoh.open(conf)
def	callback(sample):
	print("('{}':	'{}')".format(sample.key_expr,str(sample.payload.to_bytes())))
key_expr	="demo/example/**"
sub	= session.declare_subscriber(key_expr,callback)
while	True:
	time.sleep(1.0)