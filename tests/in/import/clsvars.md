@link _="prodcompany" _inherit="_template_" href="https://prodcompany.com" _text="Production Company"
// Remove __REMOVETHIS__ from in front of the mailto: so that the
// mailto: link is formed correctly. Can't have this for testing,
// because it generates different output every time the script runs
@link _="producer" _inherit="_template_" href="__REMOVETHIS__mailto:joe@prodcompany.com"
@var producer="Producer"
@var _="Joe Producer" _format="Joe Producer"
@var FancyJoe="{:.bigandbold}Joe Producer"
@var pcphone="555.867.5309"
@var sigjoe="[FancyJoe]<br />Producer<br />[Production Company]<br />[pcphone]<br />[joe@prodcompany.com]"
@var sigpc="[link.prodcompany._qlink(_qtext="prodcompany.com")]<br />[pcphone]"
@var signature="<br /><div class="extras"><p>[sigjoe]</p></div>"
@var sig1="<div class="extras"><p>[sigjoe]</p></div>"
@var sigwho="<div class="extras"><p>[{{_which_sig}}]</p></div>"
