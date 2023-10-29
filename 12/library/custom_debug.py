#!/usr/bin/python

DOCUMENTATION = '''
module: custom_debug
short_description: no thanks
options:
	msg:
		description: message
		required: True
'''

EXAMPLES = '''
# Example
custom_debug:
	msg: test message
'''

try: 
	import json
except ImportError:
	import simplejson as json

from ansible.module_utils.basic import AnsibleModule
import time
import sys

def main():
	module_args = dict(
		msg=dict(required=True, type='str')
	)

	result = dict(
		changed=False,
		return_msg=''
		)

	module = AnsibleModule (
		argument_spec = module_args
		)

	result['return_msg'] = module.params['msg']

	try: #could also use module.exit_json and module.fail_json
		module.exit_json(**result)
		sys.exit(0)
	except Exception as e:
		module.fail_json(msg=e)
		sys.exit(1)


if __name__ =='__main__':
	main()
