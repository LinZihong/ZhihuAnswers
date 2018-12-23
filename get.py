import json
import urllib.request

qid = input('Please enter question id:')
init_req_url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset=0&platform=desktop&sort_by=default".format(qid)
result = open("results/Q{}.md".format(qid),'w')
response = urllib.request.urlopen(init_req_url).read()
parsed = json.loads(response)

result.write('# '+parsed['data'][0]['question']['title']+'\n\n');

while parsed['paging']['is_end'] == False:
	for answer in parsed['data']:
		content = answer['content']
		author_name = answer['author']['name']
		result.write('### '+author_name+'\n')
		result.write(content+'\n')
	response = urllib.request.urlopen(parsed['paging']['next']).read()
	parsed = json.loads(response)
	print("make 20/{}".format(parsed['paging']['total']))

result.close()