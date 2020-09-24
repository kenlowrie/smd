@var stuffing="{{var.code.wcopen(t=\"my heading\")}}"
@var fatty="" \
    open="{{code.pushlines(t=\"{{fatmargin._open}}\n{{self.stuffing}}\")}}" \
    close="{{code.pushlines(t=\"{{var.code.wc_close}}\n{{fatmargin._close}}\")}}" \
    head="my heading" \
    stuff="(t=\"{{self.head}}\")"
[mk]
[fatty.open]
my fatty content
[fatty.close]
[mk]
