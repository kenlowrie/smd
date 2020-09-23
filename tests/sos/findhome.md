The following code is an example of how you can dynamically add elements to @wrap.
It was used in divs.md _lists_ as one way to implement the desired behavior of _lists_ derivatives,
before the _tag_ and _wrap_ extensions were put in place...

//    {{var._lists_.get_wrap}}
//    get_wrap="@wrap [!code.wrap_stack(w=\"tag.<\")!],html.li"
//    wc_open_inline="{{code.pushlines(t=\"@wrap li\n@@{{self._open_inline}}\")}}"
//    wc_close_inline="{{code.pushlines(t=\"@@{{self._close_inline}}\n@parw 1\")}}"

------------
