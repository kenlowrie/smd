WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
wrap2.md import file
@html _="pre"
-----------
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'ol': [code.wrap_stack(w="*")]
@wrap li
@wrap ul
@wrap table
@wrap tr
@wrap td
@wrap pre
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'pre': [code.wrap_stack(w="*")]
@parw 250
Current tag should be 'ol': [code.wrap_stack(w="*")]
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
-----------
@wrap li
@wrap ul
@wrap table
@wrap tr
@wrap td
@wrap pre
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'pre': [code.wrap_stack(w="*")]
@parw *
Current tag should be 'ol': [code.wrap_stack(w="*")]
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
-----------
@wrap li
@wrap ul
@wrap table
@wrap tr
@wrap td
@wrap pre
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag should be 'pre': [code.wrap_stack(w="*")]
@parw
@parw
Intentionally leave extra items on to make sure they are cleared before returning to wrap1.md
Current tag should be 'tr': [code.wrap_stack(w="*")]
WRAP2.MD -- Current wrap stack level is: [code.wrap_stack(w="#")]
@debug toggle="stdin"
