# encoding: utf-8
import random

with open("元文本_必修.txt","r",encoding="utf-8") as f:
	text = f.read()
text = text.replace("\n",'').replace('\u3000','')

poem_list = text.split("||")
# print(poem_list)
marks = "　·~！@#￥%……&*（）——+-=、|】｝【｛；‘：“”、。，《》？`~!@#$%^&*()-_=+\\|]}[{;:'/?.>,<"

poem_list_processed = []
for p in poem_list:
	for m in marks:
		p=p.replace(m," ")
	p = [x for x in p.split(" ") if x!=""]
	poem_list_processed.append(p)
poem_list.clear()
text=""
# print(poem_list_processed)
# quit()



def test():
	# while True:
	choose_poem = random.choice(poem_list_processed)
	# choose_poem = poem_list_processed[34]
	# print(choose_poem)	
	test_index = random.randint(0,len(choose_poem)-1)
	test_hint = ""
	if test_index==0:
		test_hint = f"________  {choose_poem[1]}"
	elif test_index==len(choose_poem)-1:
		test_hint = f"{choose_poem[-2]}  ________"
	else:
		a = random.randint(0,1)
		if a:
			test_hint = f"{choose_poem[test_index-1]}  ________"
		else:
			test_hint = f"________  {choose_poem[test_index+1]}"

	return test_hint,choose_poem[test_index]


tests=[]
answers=[]
for i in range(8):
	t,a = test()
	tests.append(t)
	print(t)
	answers.append(a)
# print(tests,answers)
print("\n\n\n\n\n\n\n\n",answers,"\n\n\n\n\n\n\n\n")
for t in tests:
	print(t)
