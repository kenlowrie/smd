@import "$/testsetup.md"

[var.testavdoc.begin(title="film.md" desc="Testing film related items")]

@var title="*Title of Project*"
@var artist="Artist Name"
@var thisproject="Music Video Treatment"
{:.blue.center}# [thisproject]
@var filmver="1f"
@var proj_desc="This is the proposed music video treatment for the upcoming **[artist]** single titled [title]."
@var slate="Title: [title][b]Artist: [artist][b]Directed by: Dan Director[b]Produced by: [link.prodcompany]"

@var imports="../in/import"
@import '$/import/cls-noreviewer.md'
@import '[sys.imports]/avs/shortcuts.md'
@import '[sys.imports]/avs/film.md'

@var ns="[var.tags.ns]"
@var narr="[var.tags.narr]"
@var perf="[var.tags.perf]"
@var stock="[var.tags.stock]"
@var unk="[var.tags.unk]"
@var ws="[var.fs.ws]"
@var ews="[var.fs.ews]"
@var els="[var.fs.els]"
@var ms="[var.fs.ms]"
@var cu="[var.fs.cu]"
@var mcu="[var.fs.mcu]"
@var ecu="[var.fs.ecu]"
@var ra="[var.fs.ra]"
@var ha="[var.fs.ha]"

@var wardrobe="[var.tags.wardrobe]"
@var makeup="[var.tags.makeup]"
@var props="[var.tags.props]"
@var cast="[var.tags.cast]"


@var mom="{:.cast}MOM"
@var daughter="{:.cast}DAUGHTER"
@var son="{:.cast}SON"
@var grocerybags="{:.props}Grocery Bags"
@var keys="{:.props}KEYS"
@var note="{:.props}The Note"
@var food="{:.props}Food items"
@var cap="{:.props}Baseball Cap"
@var picture="{:.props}Framed Family Picture"

@wrap _div_extras_

@var _="wrap_kludge" c="default content" _format="<p>{{self.c}}</p>"
@var divx_kludge="@@[html._div_extras_.<]" close="@@[html._div_extras_.>]"

//-------------------------------------------------------------------
@var prodnotes="{:.indent}We want to shoot between August 13th - August 17th, based on schedules. Prefer if cast can be available to shoot any day/time (weekdays, evenings or weekends), but we will work around schedules. Primary location will be NE San Antonio."

[section_pbb(t="[title] Music Video Casting Call and Character Breakdown")]
[wrap_kludge(c="**Production Title:** [title][b]**Independent/Student/Studio:** Independent[b]**Production Type:** Music Video[bb]**Production Location:** NE San Antonio[bb]**Production Start Date:** 08/05/2018[b]**Production Wrap Date:** 08/20/2018[b]**Production Schedule:** August 13 - 17 &lpar;*Preferred*&rpar;[bb][prodnotes]")]
[wrap_kludge(c="**Producer&lpar;s&rpar;:/Director&lpar;s&rpar;:** [Cloudy Logic Studios]")]
[wrap_kludge(c="**Synopsis:** \"[title]\" will be a combination narrative and performance video. The song is about ...")]

@var lp="&lpar;"
@var rp="&rpar;"

[plain(t="Character Breakdowns:")]

[wrap_kludge(c="***All parts are non-speaking, and we are in search of actors that are able to emote well, especially for the role of [mom].***")]
[wrap_kludge(c="Ethnicities aren't important, however, we will try to cast the [mom], [son] and [daughter] roles with actors that *could be* related.")]
@var familypix="*Must be available to take family pictures before production begins.*"
[wrap_kludge(c="[mom] [lp]Female, 35-45[rp] This is the lead role in the video. Mother arrives home and discovers... In the various scenes, we follow her through ... This character will be a very emotional role throughout the video. [familypix]")]

//several She goes from panic and alarm to anger and depression, and then to acceptance. 

@import '[sys.imports]/avs/image.md'
@import '[sys.imports]/avs/shot.md'
@import "[sys.imports]/avs/avs.md"
[IMG_SIZE_LARGE]
@var framegrab="*NEED FRAME GRAB FROM VIDEO HERE*"
@var ss="{{var.img_def.img_st_inline_border}}"
@var trythis="{:.red.bold}Try to get this shot"
@var beforeshoot="{:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION"

@image _id="needshot" src="[imports]/needshot.png" style="[ss]"

// -------------------------------------------------------------------
[var.scene.with_content(t="Scene 1 - [narr] Location S:0 Instrumental"   \
       c="[wardrobe][bb][props] [grocerybags][bb][makeup][bb][cast] [mom], [daughter]" \
)]

[shot_factory(nm="shot0")]
[var.shot0._null_(d="[ws]Crane high shooting over car" c="yes" l="24mm")]
[img_factory(nm="shot0" s="[imports]/shot0.jpg")]
[var.avshot.visual]
[var.shotinfo2(shotid="shot0")]
[var.avshot.audio]
[slate]
Probably just use the [title] and [artist] titles on this shot.
[comment(t="This needs to start high enough up that you can't see the trunk, and make sure the sky is NOT blown out! It comes down to reveal [mom] opening trunk and reaching in to grab groceries.")]
[var.avshot.end]

[shot_factory(nm="shot1")]
[var.shot1._null_(d="[ws]Crane Down to Mom removing groceries" c="yes" l="24mm")]
[img_factory(nm="shot1" s="[imports]/shot1.jpg")]
[var.avshot.visual]
[var.shotinfo2(shotid="shot1")]
[var.avshot.audio]
[comment(t="Make sure [mom] is already moving when she comes into frame.")]
[var.avshot.end]

// -------------------------------------------------------------------
[section(t="[narr] continues - Location S:15 L:~14s-")]

[var.lyrics(lyric="I'm sorry momma[b]that you're reading this[b]I always wanted to make you smile[b]so I must go on with this")]

// -------------------------------------------------------------------
[plain(t="Scene 99 - Random Stuff")]

@var stockshot="{{stock}}"

[var.avshot.visual]
[stockshot] - Clips of moments from his life
[var.avshot.audio]
Various shots implying flashbacks to memories or moments of his life. *If needed*
[var.avshot.end]

[var.avshot.visual]
[stockshot] - Possibly one w/[mom] comforting son
[var.avshot.audio]
Show his smile. Return to stock image. *If needed*
[var.avshot.end]

//
[section(t="Cast Headshots")]
@var headshots="[imports]"
@var sTAW="Source: TAW"

@image _id="actress1" src="[headshots]/actress1.jpg" style="[ss]" _name="Actor1 Name" _source="[sTAW]"
@image _id="actress2" src="[headshots]/actress2.jpg" style="[ss]" _name="Actor2 Name" _source="[sTAW]"


[IMG_SIZE_SMALL]
@var backup="**BACKUP CAST MEMBER**"
@var tnted="**TNT SENT**"

[divx_kludge]
## For the part of [daughter]
[divx_kludge.close]
[wrap_kludge(c="[image.actress1] [actress1._name] - [actress1._source]")]
[wrap_kludge(c="[image.actress2] [actress2._name] - [actress2._source]")]

[divx_kludge]
{:.pbb} ## Proposed shooting schedule
[divx_kludge.close]
[wrap_kludge(c="Originally, production was planned for August 2018, but it has been delayed until September due to scheduling conflicts of both cast and crew. We are anticipating two to three [lp]1/2[rp] days for production as follows:")]

[var.scene.with_content(t="Scene 3 EXT" \
    c="Cast: [mom], [daughter], [son][bb]Info: One (1) production day, evening shoot, *call time **5pm**, wrap time **8pm***.")]

[var.scene.with_content(t="Scene 1 EXT & Scene 2 INT" \
    c="Cast: [mom], [daughter][bb]Info: 1/2 Production day, *call time **8a**, wrap time **12pm** (noon)*")]

[var.scene.with_content("Scene 4 INT & Scene 5 EXT" \
    c="Cast: [mom][bb]Info: 1/2 Production day, *call time **3p**, wrap time **8p***. This could be scheduled the same day as Scenes 1 and 2 if the actor is available and prefers this option (longer day)" \
)]

@@[divxp(c="**NOTE:** Actual shoot days will be scheduled according to cast availability")]

@var dump_ns_list="image=\".\" var=\".\" link=\".\" html=\".\""
@parw

[var.testavdoc.end]
