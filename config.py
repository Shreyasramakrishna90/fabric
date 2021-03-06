import fabric.api as fabi

fabi.env.roledefs = {
	'all' : ['172.21.130.226:2222',
			 '172.21.130.227:2222',
			 '172.21.130.229:2222',
			 '172.21.130.228:2222',
			 '172.21.130.230:2222',
			 '172.21.130.231:2222',
			 '172.21.130.232:2222',
			 '172.21.130.233:2222',
			 '172.21.130.236:2222',
			 '172.21.130.234:2222',
			 '172.21.130.237:2222',
			 '172.21.130.238:2222',
			 '172.21.130.239:2222',
			 '172.21.130.240:2222',
			 '172.21.130.241:2222',
			 '172.21.130.242:2222',
			 '172.21.130.243:2222', #bbb-8014
			 '172.21.130.244:2222',
			 '172.21.130.245:2222', #bbb-96af
			 '172.21.130.246:2222', #bbb-6302
			 '172.21.130.248:2222',
			 '172.21.130.247:2222',
			 '172.21.130.249:2222',
			 '172.21.130.250:2222',
			 '172.21.130.252:2222',
			 '172.21.130.251:2222'],
	'ip1' : ['10.1.1.187',
		 '10.1.1.188',
		 '10.1.1.189',
		 '10.1.1.194',
		 '10.1.1.195',
		 '10.1.1.196',
		 '10.1.1.197',
		 '10.1.1.198'
		],
	'ip1:2222' : ['10.1.1.187:2222',
		 '10.1.1.188:2222',
		 '10.1.1.189:2222',
		 '10.1.1.194:2222',
		 '10.1.1.195:2222',
		 '10.1.1.196:2222',
		 '10.1.1.197:2222',
		 '10.1.1.198:2222'
		],
	'ip172_1_1' : [ '172.21.130.225', # 6302
					'172.21.130.223', # 8014
					'172.21.130.222', # 4c23
					'172.21.130.221', # 7d6a
		],
	'ip172_1_1:2222' : [ '172.21.130.225:2222', # 6302
					 	 '172.21.130.223:2222', # 8014
					 	 '172.21.130.222:2222', # 4c23
					 	 '172.21.130.221:2222', # 7d6a
		],
	'ip2' : ['10.1.2.192',
		 '10.1.2.193',
		 '10.1.2.194',
		 '10.1.2.195',
		 '10.1.2.196',
		 '10.1.2.197',
		 '10.1.2.199'
		],
	'ip2:2222' : ['10.1.2.192:2222',
		 '10.1.2.193:2222',
		 '10.1.2.194:2222',
		 '10.1.2.195:2222',
		 '10.1.2.196:2222',
		 '10.1.2.197:2222',
		 '10.1.2.199:2222'
		],
	'ip3_1' :['10.1.3.193',
		 '10.1.3.195',
		 '10.1.3.197',
		 '10.1.3.199'
		],
	'ip3_2' : ['10.1.3.187',
		 '10.1.3.188',
		 '10.1.3.196',
		 '10.1.3.198',
		],
	'ip3_1:2222' : ['10.1.3.193:2222',
		      '10.1.3.195:2222',
		      '10.1.3.197:2222',
		      '10.1.3.199:2222'
		],
	'ip3_2:2222' : ['10.1.3.187:2222',
		      '10.1.3.188:2222',
		      '10.1.3.196:2222',
		      '10.1.3.198:2222',
		],
	'ip4_2' : ['10.1.4.103',
		 '10.1.4.104',
		 '10.1.4.106',
		 '10.1.4.107'
		],
	'ip4_2:2222' : ['10.1.4.103:2222',
		 '10.1.4.104:2222',
		 '10.1.4.106:2222',
		 '10.1.4.107:2222'
		],
	'c1_1' : ['bbb-6302.local:2222',
		  'bbb-8014.local:2222',
		  'bbb-4c23.local:2222',
		  'bbb-7d6a.local:2222',
		],
	'c1_2' : ['bbb-235d.local:2222',
		'bbb-c473.local:2222',
		'bbb-95f9.local:2222',
		'bbb-b957.local:2222',
		],
	'c2_1' : ['bbb-96af.local:2222',
		  'bbb-bcf6.local:2222',
		  'bbb-22d9.local:2222',
		  'bbb-c189.local:2222',
		],
	'c2_2' : ['bbb-b152.local:2222',
		  'bbb-ed97.local:2222',
		  'bbb-bce4.local:2222',
		  'bbb-b4bc.local:2222',
		],

	'c3_1' : ['bbb-cb60.local:2222',
		  'bbb-c452.local:2222',
		  'bbb-adef.local:2222',
		  'bbb-ede8.local:2222',
		],
	'c3_2' : ['bbb-a702.local:2222',
		  'bbb-99b4.local:2222',
		  'bbb-1b70.local:2222',
		  'bbb-5eb7.local:2222',
		],
	'c4_2' : ['bbb-c434.local:2222',
		'bbb-e1ec.local:2222',
		'bbb-41b1.local:2222',
		'bbb-50c9.local:2222',
		],
	'opal' : ['bbb-a688.local',
		'bbb-b42d.local',
		'bbb-3f18.local',
		'bbb-a5b1.local'
		]
}
