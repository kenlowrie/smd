WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
-----------
Current tag should be 'link': [code.wrap_stack(w="*")]
@wrap li
@wrap ul
@wrap code
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'code': [code.wrap_stack(w="*")]
@parw 25
Current tag should be 'link': [code.wrap_stack(w="*")]
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
-----------
@wrap li
@wrap ul
@wrap code
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'code': [code.wrap_stack(w="*")]
@parw *
Current tag should be 'link': [code.wrap_stack(w="*")]
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
-----------
@wrap li
@wrap ul
@wrap code
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'code': [code.wrap_stack(w="*")]
@parw
@parw
@parw
@parw
Current tag should be 'link': [code.wrap_stack(w="*")]
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]

@wrap ol
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'ol': [code.wrap_stack(w="*")]
@import '$/wrap2.md'
@debug toggle="stdin"
Returned from wrap2 ...
Current tag should be 'ol': [code.wrap_stack(w="*")]
WRAP1.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]


