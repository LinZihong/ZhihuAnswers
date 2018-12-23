import json
import urllib.request

qid = input('Please enter question id:')
limit = int(input('Please enter the limit on the number of answers, if any (if none, put 0):'))
i = 0
init_req_url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset=0&platform=desktop&sort_by=default".format(qid)
result = open("results/Q{}.md".format(qid),'w')
response = urllib.request.urlopen(init_req_url).read()
parsed = json.loads(response)

result.write('# '+parsed['data'][0]['question']['title']+'\n\n');

while parsed['paging']['is_end'] == False and (limit == 0 or 20*i < limit):
	for answer in parsed['data']:
		content = answer['content']
		author_name = answer['author']['name']
		result.write('### '+author_name+'\n')
		result.write(content+'\n')
	response = urllib.request.urlopen(parsed['paging']['next']).read()
	parsed = json.loads(response)
	print("make 20/{}".format(parsed['paging']['totals']))
	i += 1

result.close()