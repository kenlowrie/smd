[link.ug_samp_film]
[wrap_h.chapter(t="##Creating a Treatment for Film/Video")]

@var title="*Title of Project*"
@var artist="Artist Name"
@var thisproject="Music Video Treatment"
{:.blue.center}# [thisproject]
@var filmver="1f"
@var proj_desc="This is the proposed music video treatment for the upcoming **[artist]** single titled [title]."
@var slate="Title: [title][b]Artist: [artist][b]Directed by: Dan Director[b]Produced by: [link.prodcompany]"

@var image_path="[sys.root]/docs/samples/image"
@import '$/cls-noreviewer.md'

@import "[sys.imports]/avs/avs.md"

// import short version of commonly used tags for convenience
@import "[sys.imports]/avs/shotacro.md"

// code.cast_factory makes it easy to generate a cast member
// [nm] will be the character name; also accessible via [nm.name] or [nm.name_e] (escaped)
// [nm.actor] is the actor's real name
// [nm.fname] is the character full name
// Example: [cast_factory(nm="Jones" a="Harrison Ford" m="Indiana Jones")]

[cast_factory(nm="mom" c="MOM" a="Actor Name" m="Character Full Name")]
[cast_factory(nm="daughter" c="DAUGHTER" a="Actor Name" m="Character Full Name")]
[cast_factory(nm="son" c="SON" a="Actor Name" m="Character Full Name")]

// code.prop_factory creates prop variables to easily mark them up in the script
// [nm] is the propname; also [nm.prop]
// Example: [prop_factory(nm="phone" p="iPhone")]

[prop_factory(nm="grocerybags", p="Grocery Bags")]
[prop_factory(nm="keys" p="KEYS")]
[prop_factory(nm="thenote" p="The Note")]
[prop_factory(nm="food" p="Food items")]
[prop_factory(nm="cap" p="Baseball Cap")]
[prop_factory(nm="picture" p="Framed Family Picture")]

//-------------------------------------------------------------------
@var prodnotes="{:.indent}We want to shoot between August 13th - August 17th, based on schedules. Prefer if cast can be available to shoot any day/time (weekdays, evenings or weekends), but we will work around schedules. Primary location will be NE San Antonio."

[section_pbb(t="[title] Music Video Casting Call and Character Breakdown")]
**Production Title:** [title][b]**Independent/Student/Studio:** Independent[b]**Production Type:** Music Video[bb]**Production Location:** NE San Antonio[bb]**Production Start Date:** 08/05/2018[b]**Production Wrap Date:** 08/20/2018[b]**Production Schedule:** August 13 - 17 &lpar;*Preferred*&rpar;[bb][prodnotes]
**Producer&lpar;s&rpar;:/Director&lpar;s&rpar;:** [ProductionCompany]
**Synopsis:** "[title]" will be a combination narrative and performance video. The song is about ...

[plain(t="Character Breakdowns:")]

***All parts are non-speaking, and we are in search of actors that are able to emote well, especially for the role of [mom].***
Ethnicities aren't important, however, we will try to cast the [mom], [son] and [daughter] roles with actors that *could be* related.
@var familypix="*Must be available to take family pictures before production begins.*"
[mom] (Female, 35-45) This is the lead role in the video. Mother arrives home and discovers... In the various scenes, we follow her through ... This character will be a very emotional role throughout the video. [familypix]

[plain(t="Scene Breakdowns:")]

[IMG_SIZE_LARGE]
@var framegrab="*NEED FRAME GRAB FROM VIDEO HERE*"
@var ss="{{var.img_def.img_st_inline_border}}"
@var trythis="{:.red.bold}Try to get this shot"
@var beforeshoot="{:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION"

@image _id="needshot" src="[image_path]/needshot.png" style="[ss]"

// -------------------------------------------------------------------
[var.scene.with_content(t="Scene 1 - [narr] Location S:0 Instrumental"   \
       c="[wardrobe][bb][props] [grocerybags][bb][makeup][bb][cast] [mom], [daughter]" \
)]

[shot_factory(nm="shot0")]
[var.shot0._null_(d="[ws]Crane high shooting over car" c="yes" l="24mm")]
[img_factory(nm="shot0" s="[image_path]/shot0.jpg")]
[var.avshot.visual]
[var.shotinfo2(shotid="shot0")]
[var.avshot.audio]
[slate]
Probably just use the [title] and [artist] titles on this shot.
[note.nd(t="This needs to start high enough up that you can't see the trunk, and make sure the sky is NOT blown out! It comes down to reveal [mom] opening trunk and reaching in to grab groceries.")]
[var.avshot.end]

[shot_factory(nm="shot1")]
[var.shot1._null_(d="[ws]Crane Down to Mom removing groceries" c="yes" l="24mm")]
[img_factory(nm="shot1" s="[image_path]/shot1.jpg")]
[var.avshot.visual]
[var.shotinfo2(shotid="shot1")]
[var.avshot.audio]
[note.nd(t="Make sure [mom] is already moving when she comes into frame.")]
[var.avshot.end]

// -------------------------------------------------------------------
[section(t="[narr] continues - Location S:15 L:~14s-")]
[var.lyrics.with_content(t="**Song Lyrics**" c="[b]I'm sorry momma[b]that you're reading this[b]I always wanted to make you smile[b]so I must go on with this")]

// -------------------------------------------------------------------
[plain(t="Scene 99 - Random Stuff")]

@var stockshot="{{stock}}"

[avshot.shot_only(_s="WS: Describe your opening master shot here")]
[avshot.shot_with_desc(_s="[stockshot] Clips of moments from his life" _d="Various shots implying flashbacks to memories or moments of his life. *If needed*")]

[var.avshot.visual]
[stockshot] Possibly one w/[mom] comforting son
[var.avshot.audio]
Show his smile. Return to stock image. *If needed*
[var.avshot.end]

//
[section(t="Cast Headshots")]
@var headshots="[image_path]"
@var sTAW="Source: TAW"

@image _id="actress1" src="[headshots]/actress1.jpg" style="[ss]" _name="Actor1 Name" _source="[sTAW]"
@image _id="actress2" src="[headshots]/actress2.jpg" style="[ss]" _name="Actor2 Name" _source="[sTAW]"


[IMG_SIZE_SMALL]
@var backup="**BACKUP CAST MEMBER**"
@var tnted="**TNT SENT**"

[wrap_h(t="## For the part of [daughter]")]
[image.actress1] [actress1._name] - [actress1._source]
[image.actress2] [actress2._name] - [actress2._source]

[wrap_h(t="## Proposed shooting schedule")]

Originally, production was planned for August 2018, but it has been delayed until September due to scheduling conflicts of both cast and crew. We are anticipating two to three (1/2) days for production as follows:

[var.scene.wc_open(t="Scene 3 EXT")]
    Cast: [mom], [daughter], [son][bb]Info: One (1) production day, evening shoot, *call time **5pm**, wrap time **8pm***.
[var.scene.wc_close]

[var.scene.with_content(t="Scene 1 EXT & Scene 2 INT" \
    c="Cast: [mom], [daughter][bb]Info: 1/2 Production day, *call time **8a**, wrap time **12pm** (noon)*")]

[var.scene.with_content("Scene 4 INT & Scene 5 EXT" \
    c="Cast: [mom][bb]Info: 1/2 Production day, *call time **3p**, wrap time **8p***. This could be scheduled the same day as Scenes 1 and 2 if the actor is available and prefers this option (longer day)" \
)]

**NOTE:** Actual shoot days will be scheduled according to cast availability

